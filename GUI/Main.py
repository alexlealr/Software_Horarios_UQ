import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.Login import Login


if __name__ == "__main__":
    app = QApplication([])
    index = QMainWindow()
    main_window = Login()
    main_window.setup_ui(index)
    index.show()
    sys.exit(app.exec_())
