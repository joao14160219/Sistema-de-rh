from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
import sys
from core.db import init_db

def main():
    # inicializa banco de dados
    init_db()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
