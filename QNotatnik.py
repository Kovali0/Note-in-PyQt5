from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import os

class MainWindow(QMainWindow):
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Filename', 
            'Write a filename:')
        if ok:
            return text
            
    def save_Note(self):
        #filename = self.showDialog()  + '.txt'
        filename = QFileDialog.getSaveFileName(self, "Save File", './', '.txt')[0]
        filename = filename + '.txt'
        print(filename)
        f = open(filename,'w')
        text = self.textareaP.toPlainText()
        #print("toto=>"+text)
        f.write(text)
        f.close
        #os.startfile(filename)
        
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Notatnikus")
        self.setGeometry(300, 300, 800, 650)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        newAct = QAction('New',self)
        fileMenu.addAction(newAct)
        openAct = QAction('Open',self)
        fileMenu.addAction(openAct)
        saveAct = QAction('&Save File',self)
        fileMenu.addAction(saveAct)
        saveAct.triggered.connect(self.save_Note)
        saveasAct = QAction('Save As ...',self)
        fileMenu.addAction(saveasAct)
        closeAct = QAction('Close',self)
        fileMenu.addAction(closeAct)
        editMenu = mainMenu.addMenu('Edit')
        cutAct = QAction('Cut',self)
        cutAct.setShortcut('Ctrl+c')
        editMenu.addAction(cutAct)
        copieAct = QAction('Copie',self)
        copieAct.setShortcut('Ctrl+x')
        editMenu.addAction(copieAct)
        pasteAct = QAction('Paste',self)
        pasteAct.setShortcut('Ctrl+v')
        editMenu.addAction(pasteAct)
        selectallAct = QAction('Select All',self)
        pasteAct.setShortcut('Ctrl+a')
        editMenu.addAction(pasteAct)

        self.toolbar = self.addToolBar('toolbar')

        newAct = QAction(QIcon('icons/notenew.png'), 'new', self)
        #exitAct.setShortcut('Ctrl+Q')
        #exitAct.triggered.connect(qApp.quit)
        self.toolbar.addAction(newAct)

        openAct = QAction(QIcon('icons/notefolder.png'), 'open', self)
        self.toolbar.addAction(openAct)
        searchAct = QAction(QIcon('icons/notesearch.png'), 'search', self)
        self.toolbar.addAction(searchAct)
        saveAct = QAction(QIcon('icons/notesave.png'), 'save', self)
        self.toolbar.addAction(saveAct)
        self.toolbar.addSeparator()
        undoAct = QAction(QIcon('icons/noteundo.png'), 'undo', self)
        self.toolbar.addAction(undoAct)
        redoAct = QAction(QIcon('icons/noteredo.png'), 'redo', self)
        self.toolbar.addAction(redoAct)
        self.toolbar.addSeparator()
        cutAct = QAction(QIcon('icons/notescissors.png'), 'cut', self)
        self.toolbar.addAction(cutAct)
        copieAct = QAction(QIcon('icons/notetwo.png'), 'copie', self)
        self.toolbar.addAction(copieAct)
        lastAct = QAction(QIcon('icons/notelasticon.png'), 'paste', self)
        self.toolbar.addAction(lastAct)
        self.toolbar.addSeparator()
        
        self.setWindowIcon(QIcon('noteicon.png'))
        self.statusBar().showMessage('Ready')
        
        self.form_widget = Central(self) 
        self.setCentralWidget(self.form_widget)

class Central(QWidget):
    def color_switch(self, color):
        print(color)
        pal = QPalette()
        bgc = QColor(color)
        pal.setColor(QPalette.Base, bgc)
        if(color=='#181818'):
            textclr = QColor(255, 255, 255)
            pal.setColor(QPalette.Text, textclr)
        self.textarea.setPalette(pal)


    def font_change(self, btn):
        if btn.text() == "Times New Roman":
            if btn.isChecked() == True:
                self.fnt = QFont("Times New Roman")
                #self.font.setFamily(self.fnt)
                self.textarea.setFont(self.fnt)
                #self.textarea.setStyleSheet("font-family: Times New Roman;")
        elif btn.text() == "Arial":
            if btn.isChecked() == True:
                self.fnt = QFont("Arial")
                self.textarea.setFont(self.fnt)
                #self.textarea.setStyleSheet("font-family: Arial;")
        else:
            if btn.isChecked() == True:
                self.fnt = QFont("Curier")
                self.textarea.setFont(self.fnt)
                #self.textarea.setStyleSheet("font-family: Curier;")

    def size_switch(self):
        self.textarea.setStyleSheet("font-size: "+self.combo.currentText()+"pt;")

    def get_color_switch_func(self, color):
        return lambda: self.color_switch(color)

    def get_font_change_func(self, btn):
        return lambda: self.font_change(btn)
        
    def __init__(self, parent):
        super().__init__(parent)
        self.hbox = QHBoxLayout()

        parent.textareaP = QTextEdit()
        self.textarea = parent.textareaP

        self.vbox = QVBoxLayout()

        self.combo = QComboBox(self)
        self.combo.addItem("8")
        self.combo.addItem("10")
        self.combo.addItem("12")
        self.combo.addItem("14")
        self.combo.addItem("16")
        self.combo.addItem("18")
        self.combo.addItem("20")
        self.combo.addItem("22")
        self.combo.addItem("24")
        self.combo.addItem("26")
        self.combo.currentIndexChanged.connect(self.size_switch)

        self.groupBox = QGroupBox()

        self.btnNR = QRadioButton('Times New Roman')
        self.btnNR.toggled.connect(self.get_font_change_func(self.btnNR))
        self.btnAR = QRadioButton('Arial')
        self.btnAR.toggled.connect(self.get_font_change_func(self.btnAR))
        self.btnCN = QRadioButton('Curier')
        self.btnCN.toggled.connect(self.get_font_change_func(self.btnCN))
        self.btnNR.setChecked(True)

        colors =['#181818','#808080', '#680000', '#F00000', '#CC6600',
                    '#ffffff', '#D0D0D0', '#CC6633', '#FF99FF', '#FFFF00',
                    '#FFFF66', '#99FF00', '#3399CC', '#330099', '#990099',
                    '#FFFF99', '#99FF66', '#66FFFF', '#6699FF', '#996699' ]
        colorbox = QGridLayout()
        for i, color in enumerate(colors):
            clrbtn = QPushButton()
            clrbtn.clicked.connect(self.get_color_switch_func(color))
            clrbtn.setStyleSheet("background-color:"+color+";");
            if(i < 5):
                colorbox.addWidget(clrbtn,0,i)
            elif(i >= 5 and i < 10):
                colorbox.addWidget(clrbtn,1,i-5)
            elif(i >= 10 and i < 15):
                colorbox.addWidget(clrbtn,2,i-10)
            elif(i >= 15):
                colorbox.addWidget(clrbtn,3,i-15)

        vboxfont = QVBoxLayout()
        vboxfont.addWidget(self.btnNR)
        vboxfont.addWidget(self.btnAR)
        vboxfont.addWidget(self.btnCN)
        self.groupBox.setLayout(vboxfont)
        
        self.vbox.addWidget(self.combo)
        self.vbox.addWidget(self.groupBox)
        self.vbox.addLayout(colorbox)

        self.hbox.addLayout(self.vbox)
        self.hbox.addWidget(self.textarea)
        self.hbox.setAlignment(self.vbox, Qt.AlignTop)

        self.setLayout(self.hbox)
        self.show()

    
if __name__ == '__main__':
        
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
