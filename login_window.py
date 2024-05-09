# Form implementation generated from reading ui file 'login_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 385)
        MainWindow.setMinimumSize(QtCore.QSize(500, 385))
        MainWindow.setMaximumSize(QtCore.QSize(500, 385))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_login_main = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_login_main.setGeometry(QtCore.QRect(0, 0, 600, 415))
        self.frame_login_main.setMinimumSize(QtCore.QSize(600, 415))
        self.frame_login_main.setMaximumSize(QtCore.QSize(600, 415))
        self.frame_login_main.setAutoFillBackground(False)
        self.frame_login_main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_login_main.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_login_main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_login_main.setObjectName("frame_login_main")
        self.werhere_image_label = QtWidgets.QLabel(parent=self.frame_login_main)
        self.werhere_image_label.setGeometry(QtCore.QRect(20, 30, 471, 71))
        self.werhere_image_label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.werhere_image_label.setText("")
        self.werhere_image_label.setPixmap(QtGui.QPixmap("werhere_image.png"))
        self.werhere_image_label.setObjectName("werhere_image_label")
        self.login_tabWidget = QtWidgets.QTabWidget(parent=self.frame_login_main)
        self.login_tabWidget.setGeometry(QtCore.QRect(30, 130, 421, 191))
        self.login_tabWidget.setMinimumSize(QtCore.QSize(421, 191))
        self.login_tabWidget.setMaximumSize(QtCore.QSize(421, 191))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        self.login_tabWidget.setFont(font)
        self.login_tabWidget.setStyleSheet("")
        self.login_tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.login_tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.login_tabWidget.setObjectName("login_tabWidget")
        self.user_login = QtWidgets.QWidget()
        self.user_login.setObjectName("user_login")
        self.user_login_groupBox = QtWidgets.QGroupBox(parent=self.user_login)
        self.user_login_groupBox.setGeometry(QtCore.QRect(0, 0, 391, 191))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        self.user_login_groupBox.setFont(font)
        self.user_login_groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.user_login_groupBox.setObjectName("user_login_groupBox")
        self.user_login_pushButton = QtWidgets.QPushButton(parent=self.user_login_groupBox)
        self.user_login_pushButton.setGeometry(QtCore.QRect(130, 140, 75, 24))
        self.user_login_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.user_login_pushButton.setObjectName("user_login_pushButton")
        self.user_exit_pushButton = QtWidgets.QPushButton(parent=self.user_login_groupBox)
        self.user_exit_pushButton.setGeometry(QtCore.QRect(220, 140, 75, 24))
        self.user_exit_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.user_exit_pushButton.setObjectName("user_exit_pushButton")
        self.user_name_label = QtWidgets.QLabel(parent=self.user_login_groupBox)
        self.user_name_label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.user_name_label.setObjectName("user_name_label")
        self.password_label = QtWidgets.QLabel(parent=self.user_login_groupBox)
        self.password_label.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.password_label.setObjectName("password_label")
        self.user_name_textEdit = QtWidgets.QTextEdit(parent=self.user_login_groupBox)
        self.user_name_textEdit.setGeometry(QtCore.QRect(120, 30, 181, 31))
        self.user_name_textEdit.setStyleSheet("QTextEdit:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QTextEdit:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.user_name_textEdit.setObjectName("user_name_textEdit")
        self.password_textEdit = QtWidgets.QTextEdit(parent=self.user_login_groupBox)
        self.password_textEdit.setGeometry(QtCore.QRect(120, 70, 181, 31))
        self.password_textEdit.setStyleSheet("QTextEdit:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QTextEdit:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.password_textEdit.setObjectName("password_textEdit")
        self.login_tabWidget.addTab(self.user_login, "")
        self.admin_login = QtWidgets.QWidget()
        self.admin_login.setObjectName("admin_login")
        self.admin_login_groupBox = QtWidgets.QGroupBox(parent=self.admin_login)
        self.admin_login_groupBox.setGeometry(QtCore.QRect(0, 0, 388, 183))
        self.admin_login_groupBox.setMinimumSize(QtCore.QSize(388, 181))
        self.admin_login_groupBox.setMaximumSize(QtCore.QSize(388, 183))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        self.admin_login_groupBox.setFont(font)
        self.admin_login_groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.admin_login_groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.admin_login_groupBox.setObjectName("admin_login_groupBox")
        self.admin_login_pushButton = QtWidgets.QPushButton(parent=self.admin_login_groupBox)
        self.admin_login_pushButton.setGeometry(QtCore.QRect(110, 140, 75, 24))
        self.admin_login_pushButton.setStyleSheet("\n"
"\n"
"QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0,               y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.admin_login_pushButton.setObjectName("admin_login_pushButton")
        self.admin_exit_pushButton = QtWidgets.QPushButton(parent=self.admin_login_groupBox)
        self.admin_exit_pushButton.setGeometry(QtCore.QRect(200, 140, 75, 24))
        self.admin_exit_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.admin_exit_pushButton.setObjectName("admin_exit_pushButton")
        self.admin_user_name_textEdit = QtWidgets.QTextEdit(parent=self.admin_login_groupBox)
        self.admin_user_name_textEdit.setGeometry(QtCore.QRect(120, 30, 181, 31))
        self.admin_user_name_textEdit.setStyleSheet("QTextEdit:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QTextEdit:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.admin_user_name_textEdit.setObjectName("admin_user_name_textEdit")
        self.admin_password_label = QtWidgets.QLabel(parent=self.admin_login_groupBox)
        self.admin_password_label.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.admin_password_label.setObjectName("admin_password_label")
        self.admin_password_textEdit = QtWidgets.QTextEdit(parent=self.admin_login_groupBox)
        self.admin_password_textEdit.setGeometry(QtCore.QRect(120, 70, 181, 31))
        self.admin_password_textEdit.setStyleSheet("QTextEdit:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QTextEdit:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.admin_password_textEdit.setObjectName("admin_password_textEdit")
        self.admin_user_name_label = QtWidgets.QLabel(parent=self.admin_login_groupBox)
        self.admin_user_name_label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.admin_user_name_label.setObjectName("admin_user_name_label")
        self.login_tabWidget.addTab(self.admin_login, "")
        self.welkomTextEdit_2 = QtWidgets.QTextEdit(parent=self.frame_login_main)
        self.welkomTextEdit_2.setGeometry(QtCore.QRect(0, 330, 501, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.welkomTextEdit_2.setFont(font)
        self.welkomTextEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.welkomTextEdit_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.welkomTextEdit_2.setObjectName("welkomTextEdit_2")
        self.welkomTextEdit = QtWidgets.QTextEdit(parent=self.frame_login_main)
        self.welkomTextEdit.setGeometry(QtCore.QRect(20, 0, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.welkomTextEdit.setFont(font)
        self.welkomTextEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.welkomTextEdit.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.welkomTextEdit.setObjectName("welkomTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.login_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


# Push Buton tıklama

        self.admin_login_pushButton.clicked.connect(self.admin_login_clicked)
        self.admin_exit_pushButton.clicked.connect(self.admin_exit_clicked)
        self.user_login_pushButton.clicked.connect(self.user_login_clicked)
        self.user_exit_pushButton.clicked.connect(self.user_exit_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.user_login_groupBox.setTitle(_translate("MainWindow", "User Login"))
        self.user_login_pushButton.setText(_translate("MainWindow", "Login"))
        self.user_exit_pushButton.setText(_translate("MainWindow", "Exit"))
        self.user_name_label.setText(_translate("MainWindow", "Username"))
        self.password_label.setText(_translate("MainWindow", "Password"))
        self.user_name_textEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\">Username</p></body></html>"))
        self.user_name_textEdit.setWhatsThis(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.login_tabWidget.setTabText(self.login_tabWidget.indexOf(self.user_login), _translate("MainWindow", "User"))
        self.admin_login_groupBox.setTitle(_translate("MainWindow", "Admin Login"))
        self.admin_login_pushButton.setText(_translate("MainWindow", "Login"))
        self.admin_exit_pushButton.setText(_translate("MainWindow", "Exit"))
        self.admin_password_label.setText(_translate("MainWindow", "Password"))
        self.admin_user_name_label.setText(_translate("MainWindow", "Username"))
        self.login_tabWidget.setTabText(self.login_tabWidget.indexOf(self.admin_login), _translate("MainWindow", "Admin"))
        self.welkomTextEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">copyright@WearehereAcademy-2024</span></p></body></html>"))
        self.welkomTextEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700;\">Welcome to</span></p></body></html>"))


# Butonların Fonsiyonlarının tanımlandığı yer.

    def admin_login_clicked(self):
        print("Admin Login düğmesine tıklandı!")

    def admin_exit_clicked(self):
        print("Admin exit düğmesine tıklandı")


    def user_login_clicked(self):
        print("User Login düğmesine tıklandı!")

    def user_exit_clicked(self):
        print("User exit düğmesine tıklandı")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
