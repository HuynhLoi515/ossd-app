import sys
from PyQt5.QtWidgets import QApplication
from gui.main_ui import MainGUI


def main():
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
