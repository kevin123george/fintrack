import argparse
import requests
from rich.console import Console
from rich.prompt import Prompt
from rich import print

BASE_URL = "http://localhost:8080/stocks"
WATCHLIST_URL = "http://localhost:8080/stocks-watch"

console = Console()

def add_stock():
    console.print("[bold green]📥 Add New Stock[/bold green]")
    symbol = Prompt.ask("Stock symbol (e.g., AAPL)")
    quantity = Prompt.ask("Quantity")
    buy_price = float(Prompt.ask("Buy price (€)"))
    buy_date = Prompt.ask("Buy date [yyyy-mm-dd]")
    current_price = float(Prompt.ask("Current price (€)"))

    payload = {
        "symbol": symbol,
        "quantity": quantity,
        "buyPrice": buy_price,
        "buyDate": buy_date,
        "currentPrice": current_price
    }

    try:
        res = requests.post(BASE_URL, json=payload)
        res.raise_for_status()
        print("[green]✅ Stock added successfully![/green]")
    except requests.RequestException as e:
        print(f"[red]❌ Failed to add stock:[/red] {e}")

def update_stock_price():
    console.print("[bold yellow]📤 Update Stock Price[/bold yellow]")
    stock_id = Prompt.ask("Enter Stock ID to update")
    new_price = Prompt.ask("New current price (€)")

    try:
        url = f"{BASE_URL}/{stock_id}?currentPrice={new_price}"
        res = requests.put(url)
        res.raise_for_status()
        print("[green]✅ Stock price updated successfully![/green]")
    except requests.RequestException as e:
        print(f"[red]❌ Failed to update stock:[/red] {e}")

def add_watch_stock():
    console.print("[bold blue]🔍 Add Stock to Watchlist[/bold blue]")
    symbol = Prompt.ask("Stock symbol (e.g., TSLA)")
    initial_price = float(Prompt.ask("Initial price (€)"))
    current_price = float(Prompt.ask("Current price (€)"))

    payload = {
        "symbol": symbol,
        "initialPrice": initial_price,
        "currentPrice": current_price
    }

    try:
        res = requests.post(WATCHLIST_URL, json=payload)
        res.raise_for_status()
        print("[green]✅ Stock added to watchlist![/green]")
    except requests.RequestException as e:
        print(f"[red]❌ Failed to add to watchlist:[/red] {e}")

def main():
    parser = argparse.ArgumentParser(description="FinTrack Stock Actions CLI")
    parser.add_argument("--add", action="store_true", help="Add a new stock")
    parser.add_argument("--update", action="store_true", help="Update existing stock price")
    parser.add_argument("--watch", action="store_true", help="Add stock to watchlist")

    args = parser.parse_args()

    if args.add:
        add_stock()
    elif args.update:
        update_stock_price()
    elif args.watch:
        add_watch_stock()
    else:
        console.print("[bold cyan]ℹ️ Use --add, --update, or --watch[/bold cyan]")

if __name__ == "__main__":
    main()
