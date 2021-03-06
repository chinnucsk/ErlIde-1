from PyQt4 import QtCore, QtGui


def open_tab(Tab,FileName):
        f = open(FileName, 'r')
        I = str(Tab.count())
        Name = ""
        try :
          Name = FileName[ FileName.rindex("/")+1:]
        except :
          Name = FileName

        tab = QtGui.QWidget()
        tab.setAutoFillBackground(True)
        tab.setObjectName("tab" + I)
        horizontalLayout = QtGui.QHBoxLayout(tab)
        
        horizontalLayout.setSpacing(1)
        horizontalLayout.setMargin(1)
        horizontalLayout.setObjectName("TabHorizontalLayout" + I)
        textEd = QtGui.QTextEdit(tab)
        textEd.setObjectName("textEdit"+I)
        horizontalLayout.addWidget(textEd)
        Tab.addTab(tab, "")
        Tab.setTabText(Tab.indexOf(tab), QtGui.QApplication.translate("MainWindow", Name, None, QtGui.QApplication.UnicodeUTF8))

        with f:
            data = f.read()
            textEd.setText(data)
            
            
