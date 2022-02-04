from PySide2.QtWidgets import QApplication
from controllers.main_window import Ventana

if __name__=="__main__":
    app = QApplication()
    window = Ventana()
    window.show()
    app.exec_()
    