import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from pathlib import Path

from mainPar import *
from PIL import Image


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        #-----------------------input text area-----------------------------
        self.b = QPlainTextEdit(self)
        self.b.resize(460,500)
        self.b.textChanged.connect(self.getText)
        self.b.setPlaceholderText("please write code here.")
        #---------------------output text area--------------------------------
        self.out = QPlainTextEdit(self)
        self.out.resize(450,500)
        self.out.move(470,0)
        self.out.textChanged.connect(self.getText)
        self.out.setReadOnly(True)
        self.out.setStyleSheet( """QPlainTextEdit {background-color: #333;color: #fff;}""")
        
        self.initUI()
        
        
    def initUI(self):
        #----------------main window-----------------
        self.setGeometry(50, 50, 900, 600)
        self.setWindowTitle('parser')  
        #-----------------scan button-----------------
        self.scan = QPushButton('run',self)
        self.scan.move(420,520)
        self.scan.resize(90,40)
        self.scan.clicked.connect(self.run)     
        #----------------info button-----------------
        self.info = QPushButton('',self)
        self.info.setIcon(QIcon("assets/Question_Mark-512.png"))
        self.info.setStyleSheet(( """QPushButton {background-color: #fff;color: #fff;border-radius:50%;}"""))
        self.info.setIconSize(QSize(45,45))
        self.info.move(850,520)
        self.info.resize(45,45)
        self.info.clicked.connect(self.getInfo)     
        #----------------open file button-----------------
        self.info = QPushButton('Open file',self)
        self.info.setIconSize(QSize(45,45))
        self.info.move(750,520)
        self.scan.resize(90,40)
        self.info.clicked.connect(self.openFileNameDialog)     
    
        self.show()


#----------------------------open file---------------
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            #print(str(fileName))
            f=open( Path(str(fileName)), "r")
            content =f.read()
            #print(content)
            self.b.document().setPlainText(content)
            f.close()


#--------------------------------write txt from gui to 'tiny.txt'-------------------------------------
    def getText(self):
        f= open("assets/tiny.txt","w+")
        f.write(self.b.document().toPlainText())
        f.close()

#-------------------------------write the output into gui------------------------------------------    
    def write(self):
        f=open("assets/output.txt", "r")
        content =f.read()
        self.out.document().setPlainText(content)
        f.close()

#--------------------------------run scanner function----------------------------------------
    def run(self):
        f=open("assets/output.txt", "w+")
        f.write('')
        f.close()
        runParser()
        img  = Image.open('assets/output.png')  
        f=open("assets/output.txt", "r")
        content =f.read()
        #print(content)
        f.close()
        if content == '':
            img.show()
        
        self.write()

#-------------------------------pop up msg from info.txt-----------------------------------------------------
    def getInfo(self):
        #print('in')
        f=open("assets/info.txt", "r")
        content =f.read()
        self.msg=QMessageBox.about(self, "about", content)
        f.close()

#-----------------------empty files before closing-----------------------------------------------
    def closeEvent(self, event):
        f=open("assets/output.txt", "w+")
        f.write("")
        f.close()
        f=open("assets/tiny.txt", "w+")
        f.write("")
        f.close()
        
        


    



    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w =  Example()
    

    sys.exit(app.exec_())