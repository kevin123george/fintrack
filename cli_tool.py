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

console = Console()

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def fetch_stats():
    try:
        res = requests.get(STATS_URL)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(Fore.RED + f"❌ Failed to fetch stats: {e}" + Style.RESET_ALL)
        return None

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

    invested = f"{data['totalInvested']:.2f}"
    value = f"{data['currentValue']:.2f}"
    profit = f"{data['totalProfit']:.2f}"
    profit_color = "green" if data['totalProfit'] >= 0 else "red"

    table.add_row("💰 Total Invested" if show_emoji else "Total Invested", invested)
    table.add_row("📈 Current Value" if show_emoji else "Current Value", value)
    table.add_row("💹 Total Profit" if show_emoji else "Total Profit", f"[{profit_color}]{profit}[/{profit_color}]")

    console.print(table)

def display_holdings(holdings, show_emoji=True):
    table = Table(title="📦 Current Holdings" if show_emoji else "Current Holdings", box=box.MINIMAL_DOUBLE_HEAD)

    table.add_column("Symbol", style="bold magenta")
    table.add_column("Qty", justify="right")
    table.add_column("Buy (€)", justify="right")
    table.add_column("Current (€)", justify="right")
    table.add_column("P/L (€)", justify="right")

    for h in holdings:
        pl = (h["currentPrice"] - h["buyPrice"]) * h["quantity"]
        pl_color = "green" if pl >= 0 else "red"
        table.add_row(
            h["symbol"],
            str(h["quantity"]),
            f"{h['buyPrice']:.2f}",
            f"{h['currentPrice']:.2f}",
            f"[{pl_color}]{pl:.2f}[/{pl_color}]"
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

            if stats:
                display_stats(stats, show_emoji=not args.no_emoji)
            if holdings:
                display_holdings(holdings, show_emoji=not args.no_emoji)
                display_profit_chart(holdings)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print(Fore.CYAN + "\n👋 Exiting FinTrack CLI. Goodbye!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
