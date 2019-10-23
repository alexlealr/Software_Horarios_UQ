import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from GUI.Login import Login
from DB.Conexion_DB import alta

if __name__ == "__main__":
    app = QApplication([])
    hola = QMainWindow()
    main_window = Login()
    main_window.setup_ui(hola)
    alta()
    hola.show()
    sys.exit(app.exec_())