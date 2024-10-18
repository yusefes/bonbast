import tkinter as tk
from tkinter import ttk
from bonbast.main import get_prices

class BonbastGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bonbast Currency, Coin, and Gold Prices")

        self.create_widgets()
        self.fetch_and_display_data()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("Type", "Name", "Sell", "Buy", "Price"), show="headings")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Sell", text="Sell")
        self.tree.heading("Buy", text="Buy")
        self.tree.heading("Price", text="Price")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.refresh_button = tk.Button(self.root, text="Refresh", command=self.fetch_and_display_data)
        self.refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.close_button = tk.Button(self.root, text="Close", command=self.root.quit)
        self.close_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def fetch_and_display_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        currencies, coins, golds = get_prices()

        for currency in currencies:
            self.tree.insert("", "end", values=("Currency", currency.name, currency.formatted_sell, currency.formatted_buy, ""))

        for coin in coins:
            self.tree.insert("", "end", values=("Coin", coin.name, coin.formatted_sell, coin.formatted_buy, ""))

        for gold in golds:
            self.tree.insert("", "end", values=("Gold", gold.name, "", "", gold.formatted_price))

if __name__ == "__main__":
    root = tk.Tk()
    app = BonbastGUI(root)
    root.mainloop()
