import argparse
import requests
import time
import os
from rich.console import Console
from rich.table import Table
from rich import box
from colorama import Fore, Style

STATS_URL = "http://localhost:8080/stocks/stats"
HOLDINGS_URL = "http://localhost:8080/stocks"
WATCHLIST_URL = "http://localhost:8080/stocks-watch"


console = Console()

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def fetch_watchlist():
    try:
        res = requests.get(WATCHLIST_URL)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(Fore.RED + f"❌ Failed to fetch watchlist: {e}" + Style.RESET_ALL)
        return []

def fetch_stats():
    try:
        res = requests.get(STATS_URL)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(Fore.RED + f"❌ Failed to fetch stats: {e}" + Style.RESET_ALL)
        return None

def display_watchlist(watchlist, show_emoji=True):
    table = Table(title="👀 Watchlist" if show_emoji else "Watchlist", box=box.SIMPLE)

    table.add_column("Symbol", style="bold yellow")
    table.add_column("Initial (€)", justify="right")
    table.add_column("Current (€)", justify="right")
    table.add_column("Δ (€)", justify="right")
    table.add_column("Δ (%)", justify="right")

    for stock in watchlist:
        initial = stock["initialPrice"]
        current = stock["currentPrice"]
        delta = current - initial
        percent_change = (delta / initial) * 100 if initial else 0
        delta_color = "green" if delta >= 0 else "red"

        table.add_row(
            stock["symbol"],
            f"{initial:.2f}",
            f"{current:.2f}",
            f"[{delta_color}]{delta:+.2f}[/{delta_color}]",
            f"[{delta_color}]{percent_change:+.2f}%[/{delta_color}]"
        )

    console.print(table)



def fetch_holdings():
    try:
        res = requests.get(HOLDINGS_URL)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(Fore.RED + f"❌ Failed to fetch holdings: {e}" + Style.RESET_ALL)
        return []

def display_stats(data, show_emoji=True):
    table = Table(title="📊 Portfolio Stats" if show_emoji else "Portfolio Stats", box=box.ROUNDED)

    table.add_column("Metric", style="bold cyan")
    table.add_column("Value (€)", justify="right", style="bold green")

    invested = data['totalInvested']
    value = data['currentValue']
    profit = data['totalProfit']
    profit_percent = (profit / invested * 100) if invested else 0
    profit_color = "green" if profit >= 0 else "red"

    table.add_row("💰 Total Invested" if show_emoji else "Total Invested", f"{invested:.2f}")
    table.add_row("📈 Current Value" if show_emoji else "Current Value", f"{value:.2f}")
    table.add_row("💹 Total Profit" if show_emoji else "Total Profit", f"[{profit_color}]{profit:.2f}[/{profit_color}]")
    table.add_row("📊 Total Return %" if show_emoji else "Total Return %", f"[{profit_color}]{profit_percent:+.2f}%[/{profit_color}]")

    console.print(table)


def display_holdings(holdings, show_emoji=True):
    table = Table(title="📦 Current Holdings" if show_emoji else "Current Holdings", box=box.MINIMAL_DOUBLE_HEAD)

    table.add_column("Symbol", style="bold magenta")
    table.add_column("Qty", justify="right")
    table.add_column("Buy (€)", justify="right")
    table.add_column("Current (€)", justify="right")
    table.add_column("P/L (€)", justify="right")
    table.add_column("P/L (%)", justify="right")

    for h in holdings:
        buy_price = h["buyPrice"]
        current_price = h["currentPrice"]
        quantity = h["quantity"]

        pl = (current_price - buy_price) * quantity
        pl_percent = ((current_price - buy_price) / buy_price * 100) if buy_price else 0

        pl_color = "green" if pl >= 0 else "red"

        table.add_row(
            h["symbol"],
            str(quantity),
            f"{buy_price:.2f}",
            f"{current_price:.2f}",
            f"[{pl_color}]{pl:.2f}[/{pl_color}]",
            f"[{pl_color}]{pl_percent:+.2f}%[/{pl_color}]"
        )

    console.print(table)


from rich.progress import BarColumn, Progress, TextColumn
from rich.panel import Panel

def display_profit_chart(holdings):
    console.print(Panel.fit("📈 Per-Holding Profit", style="bold cyan"))

    for h in holdings:
        pl = (h["currentPrice"] - h["buyPrice"]) * h["quantity"]
        pl_color = "green" if pl >= 0 else "red"
        bar_length = int(abs(pl) // 10)  # Scale bar size

        bar = "█" * bar_length if pl >= 0 else "░" * bar_length
        console.print(f"{h['symbol']:6} {f'{pl:+.2f} €':>10} [{pl_color}]{bar}[/{pl_color}]")


def main():
    parser = argparse.ArgumentParser(description="Live FinTrack Portfolio Stats CLI")
    parser.add_argument("--interval", type=int, default=10, help="Refresh interval in seconds (default: 10)")
    parser.add_argument("--no-emoji", action="store_true", help="Disable emojis in output")
    args = parser.parse_args()

    try:
        while True:
            clear_console()
            stats = fetch_stats()
            holdings = fetch_holdings()
            watchlist = fetch_watchlist()

            if stats:
                display_stats(stats, show_emoji=not args.no_emoji)
            if holdings:
                display_holdings(holdings, show_emoji=not args.no_emoji)
                display_profit_chart(holdings)
            if watchlist:
                display_watchlist(watchlist, show_emoji=not args.no_emoji)

            time.sleep(args.interval)
    except KeyboardInterrupt:
        print(Fore.CYAN + "\n👋 Exiting FinTrack CLI. Goodbye!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
