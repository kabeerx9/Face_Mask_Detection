from logging import PlaceHolder
import sys
from unittest.util import _MAX_LENGTH
from PyQt5 import QtWidgets as qtw 
from PyQt5 import QtGui as qtg 
from PyQt5 import QtCore as qtc


class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #add
        
        self.setWindowTitle('This is my title ')
        self.setWindowIcon(qtg.QIcon('./icon.png'))
        # self.setGeometry(100,100,600,400)
        self.setFixedSize(1200,600)
        
        
        #QLabel
        self.label1 = qtw.QLabel('<h1>Welcome to PyQt basic programming</h1>',self)
        self.label2 = qtw.QLabel("This demonstrates simple PyQt programming",self)
        
        self.label_img = qtw.QLabel('this is a label',self)
        self.label_img.setPixmap(qtg.QPixmap('./sample.jpg'))
        self.label_img.setScaledContents(True)
        
        
        # QLineEdit 
        self.line_edit = qtw.QLineEdit('default value',self,placeholderText='Enter Your Name',maxLength=20)
        
        # QPushButton 
        self.button = qtw.QPushButton('Select',self,clicked = self.changeImage)
        
        # QComboBox 
        self.combobox = qtw.QComboBox(self)
        self.combobox.addItems(['Naruto','Sauske','Kakashi','Sakura'])
        
        
        #Placing widgets i.e THE LAYOUT 
        hlayout = qtw.QHBoxLayout()  # this is horizontal layout 
        vlayout = qtw.QVBoxLayout()  # this is vertical layout 
        
        vlayout.addWidget(self.label1)
        vlayout.addWidget(self.label2)
        vlayout.addWidget(self.line_edit)
        vlayout.addWidget(self.button)
        
        #horizontal Layout 
        hlayout.addLayout(vlayout)
        hlayout.addWidget(self.label_img)   
        
        #end
        self.setLayout(hlayout) 


        #main ui
        self.show()
    
    def changeImage(self):
        textLineEdit = self.line_edit.text()
        currentText = self.combobox.currentText()
        print(textLineEdit,currentText)
        
        if(currentText == 'Naruto'):
            self.label_img.setPixmap(qtg.QPixmap('./images/lemon.jpg'))
        elif(currentText == 'Sasuke'):
            self.label_img.setPixmap(qtg.QPixmap('./images/peach.jpg'))
        elif(currentText == 'Kakashi'):
            self.label_img.setPixmap(qtg.QPixmap('./images/raddish.jpg'))
        else:
            self.label_img.setPixmap(qtg.QPixmap('./images/strawberry.jpg'))
            
        
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = mainWindow()
    sys.exit(app.exec())
    