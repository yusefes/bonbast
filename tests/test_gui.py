import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from bonbast.gui import BonbastGUI

class TestBonbastGUI(unittest.TestCase):

    @patch('bonbast.gui.get_prices')
    def setUp(self, mock_get_prices):
        self.root = tk.Tk()
        self.app = BonbastGUI(self.root)
        mock_get_prices.return_value = ([], [], [])

    @patch('bonbast.gui.get_prices')
    def test_fetch_and_display_data(self, mock_get_prices):
        mock_get_prices.return_value = (
            [MagicMock(name='USD', formatted_sell='1000', formatted_buy='900')],
            [MagicMock(name='Coin1', formatted_sell='2000', formatted_buy='1800')],
            [MagicMock(name='Gold1', formatted_price='3000')]
        )
        self.app.fetch_and_display_data()
        self.assertEqual(len(self.app.tree.get_children()), 3)

    @patch('bonbast.gui.get_prices')
    def test_refresh_button(self, mock_get_prices):
        mock_get_prices.return_value = (
            [MagicMock(name='USD', formatted_sell='1000', formatted_buy='900')],
            [MagicMock(name='Coin1', formatted_sell='2000', formatted_buy='1800')],
            [MagicMock(name='Gold1', formatted_price='3000')]
        )
        self.app.refresh_button.invoke()
        self.assertEqual(len(self.app.tree.get_children()), 3)

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
