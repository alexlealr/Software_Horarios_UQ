import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Templates.Login import Login


if __name__ == "__main__":
    app = QApplication([])
    hola = QMainWindow()
    main_window = Login()
    main_window.setupUi(hola)
    hola.show()
    sys.exit(app.exec_())