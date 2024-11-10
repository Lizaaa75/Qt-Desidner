from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from ui import Ui_MainWindow
import random
app = QApplication([])

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.example)

    def example(self):
        symbols = ""

        if self.ui.check_numbers.isChecked():
            symbols = "1234567890"
        if self.ui.check_letters.isChecked():
            symbols += "qwertyuiopasdfghjklzxcvbnm"

        password = ""
        for i in range(random.randint(5, 10)):
            password += random.choice(symbols)

        self.ui.label_result.setText(password)

window = Widget()
window.show()
app.exec_()