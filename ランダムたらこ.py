import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Form(QDialog):
    def __init__(self, parent=None):
        #親クラス
        super(Form, self).__init__(parent)
        
        #UI
        self.char1Label = QLabel()
        self.char1Label.setText("た")
        #self.char1Label.resize(100, 100)

        self.char2Label = QLabel()
        self.char2Label.setText("ら")
        #self.char2Label.resize(100, 100)
        self.char2Label.setAlignment(Qt.AlignCenter | Qt.AlignCenter)

        self.char3Label = QLabel()
        self.char3Label.setText("こ")
        #self.char3Label.resize(100, 100)

        self.adjustSpaceLabel = QLabel()
        self.adjustSpaceLabel.setText("                           ")
        #self.adjustSpaceLabel.resize(100, 100)

        self.CngrLabel = QLabel()
        self.CngrLabel.setText("")

        self.playSlotButton = QPushButton("　GO!　")
        self.playSlotButton.setFocusPolicy(Qt.NoFocus)  #enterで自動的に移動しない様にする

        #グリッドレイアウトで設置
        grid = QGridLayout()
        
        grid.setContentsMargins(20, 10, 20, 10)
        grid.addWidget(self.char1Label, 0, 1)
        grid.addWidget(self.char2Label, 0, 2)
        grid.addWidget(self.char3Label, 0, 3)
        grid.addWidget(self.CngrLabel, 1, 2)
        grid.addWidget(self.adjustSpaceLabel, 2, 2)
        grid.addWidget(self.playSlotButton, 3, 2)
        
        self.setLayout(grid)
        
        
        #イベント
        #self.char1Label.textChanged.connect(self.Congratulation)
        #self.char2Label.textChanged.connect(self.Congratulation)
        #self.char3Label.textChanged.connect(self.Congratulation)
        self.playSlotButton.clicked.connect(self.slotTRK)


    def slotTRK(self):
        self.CngrLabel.setText("")
        
        TARAKO = {1:"た",2:"ら",3:"こ"}

        #ramChar = [TARAKO[random.randint(1,3)] for char in range(3)]

        #word = "".join(ramChar)
        
        word = TARAKO[random.randint(1,3)]
        
        self.char1Label.setText(word)

        word = TARAKO[random.randint(1,3)]
        
        self.char2Label.setText(word)

        word = TARAKO[random.randint(1,3)]
        
        self.char3Label.setText(word)
        

    #def Congratulation(self):
        if self.char1Label.text() == "た" and self.char2Label.text() == "ら" and  self.char3Label.text() == "こ":
            self.CngrLabel.setText("Congratulations!!")



# プログラム実行
if __name__ == '__main__':
    font = QFont()
    font.setFamily("BIZ UDPゴシック")
    font.setPointSize(15)

    app = QApplication(sys.argv)
    app.setFont(font)
    form = Form()
    form.show()

    sys.exit(app.exec_())