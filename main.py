# This Python file uses the following encoding: utf-8
import random
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load('dialog.ui')
        self.ui.show()

        self.ui.btn_check.clicked.connect(self.Guess)
        self.ui.btn_new.clicked.connect(self.New)
        self.rand_number=int(random.randint(0,20))
        print(self.rand_number)
        self.guess=0


    def Guess(self):
        self.number = self.ui.lineEdit.text()
        if self.number.isnumeric():
            if self.rand_number ==int(self.number):
                self.ui.lbl_message.setText('شما برنده شدید🤩️')
            elif self.rand_number < int(self.number):
                self.guess += 1
                self.ui.lbl_message.setText('لطفا عدد کوچکتر حدس بزنید.')
            elif self.rand_number > int(self.number):
                self.guess += 1
                self.ui.lbl_message.setText('لطفا عدد بزرگتر حدس بزنید.')
            if self.guess >=5:
                self.ui.lbl_message.setText('متاسفانه باختید🤯️')
                self.New()
        else:
            self.ui.lbl_message.setText('لظفا عدد وارد کنید.')
        self.ui.lbl_guess.setText(" تعداد حدس ها: "+ str(self.guess))
    def New(self):
        self.guess = 0
        self.rand_number = int(random.randint(0, 20))
        print(self.rand_number)
        self.ui.lbl_guess.clear()
        self.ui.lbl_message.clear()
        self.ui.lineEdit.clear()
if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    # window.show()
    sys.exit(app.exec_())
