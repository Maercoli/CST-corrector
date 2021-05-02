import sys

from PySide2.QtWidgets import *
from ui_main import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Programa Corretor de CST")

        self.btn_select.clicked.connect(self.open_file)
        self.btn_correct.clicked.connect(self.fix_cst)

    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self, "Selecione o arquivo SPED")
        self.txt_file.setText(str(self.file[0]))

    def fix_cst(self):
        new_sped = []

        with open(self.txt_file.text(), 'r+') as line:
            for reg in line:

                if reg[:6] == '|C170|':
                    new_file = list(reg.split('|'))

                    for dados in new_file:
                        if dados == self.txt_cfop.text():
                            new_file[25] = self.txt_cst.text()
                            new_file[31] = self.txt_cst.text()

                    aux = ('|'.join(new_file))
                    new_sped.append(aux)
                    continue
                new_sped.append(reg)

        with open('fixed_efd.txt', 'w+') as fixed:

            for lin in new_sped:
                fixed.writelines(lin)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("'Correcao")
        msg.setText('Correcao do CST concluida')
        msg.exec_()

if __name__== '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
