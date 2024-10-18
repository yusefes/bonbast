from bonbast import main
import sys

def run() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        from bonbast.gui import BonbastGUI
        import tkinter as tk
        root = tk.Tk()
        app = BonbastGUI(root)
        root.mainloop()
    else:
        main.cli()

# NEEDED FOR `python -m bonbast`
if __name__ == '__main__':
    run()
