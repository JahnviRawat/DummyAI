from subprocess import run 
import speech_recognition as sr   #speech recognizing
import sys
from AssistantUI import Ui_AssistantUI
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer ,QTime , QDate
from PyQt5.uic import loadUiType
import hotword


class MainThread(QThread):
     

    def __init__(self):

        super(MainThread,self).__init__()
        

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        hotword.WakeUp()
             

startExe = MainThread()

class Gui_Start(QMainWindow):


    def __init__(self):
        super().__init__()

        self.gui = Ui_AssistantUI()
        self.gui.setupUi(self)

        self.gui.StartButton.clicked.connect(self.startTask)
        self.gui.ExitButton.clicked.connect(self.close)

    def startTask(self):

        self.gui.label1 = QtGui.QMovie("Gif1.gif")
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()


        startExe.start()


GuiApp = QApplication(sys.argv)
assistant_ui = Gui_Start()

assistant_ui.show()
            
exit(GuiApp.exec_())








 









     





