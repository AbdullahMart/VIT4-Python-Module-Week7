# Form implementation generated from reading ui file 'admin_preference_menu.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_admin_pref_men_MainWindow(object):
    def setupUi(self, admin_pref_men_MainWindow):
        admin_pref_men_MainWindow.setObjectName("admin_pref_men_MainWindow")
        admin_pref_men_MainWindow.resize(500, 500)
        admin_pref_men_MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        admin_pref_men_MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        admin_pref_men_MainWindow.setAcceptDrops(False)
        admin_pref_men_MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        admin_pref_men_MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=admin_pref_men_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.admin_preference_menu_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.admin_preference_menu_frame.setGeometry(QtCore.QRect(-150, -80, 721, 661))
        self.admin_preference_menu_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.admin_preference_menu_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.admin_preference_menu_frame.setObjectName("admin_preference_menu_frame")
        self.werhere_image_label = QtWidgets.QLabel(parent=self.admin_preference_menu_frame)
        self.werhere_image_label.setGeometry(QtCore.QRect(170, 110, 481, 101))
        self.werhere_image_label.setText("")
        self.werhere_image_label.setPixmap(QtGui.QPixmap("werhere_image.png"))
        self.werhere_image_label.setObjectName("werhere_image_label")
        self.application_page_pushButton = QtWidgets.QPushButton(parent=self.admin_preference_menu_frame)
        self.application_page_pushButton.setGeometry(QtCore.QRect(190, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.application_page_pushButton.setFont(font)
        self.application_page_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.application_page_pushButton.setObjectName("application_page_pushButton")
        self.mentor_interview_pushButton = QtWidgets.QPushButton(parent=self.admin_preference_menu_frame)
        self.mentor_interview_pushButton.setGeometry(QtCore.QRect(190, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.mentor_interview_pushButton.setFont(font)
        self.mentor_interview_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.mentor_interview_pushButton.setObjectName("mentor_interview_pushButton")
        self.Exit_pushButton = QtWidgets.QPushButton(parent=self.admin_preference_menu_frame)
        self.Exit_pushButton.setGeometry(QtCore.QRect(210, 470, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.Exit_pushButton.setFont(font)
        self.Exit_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.Exit_pushButton.setObjectName("Exit_pushButton")
        self.interviews_pushButton = QtWidgets.QPushButton(parent=self.admin_preference_menu_frame)
        self.interviews_pushButton.setGeometry(QtCore.QRect(190, 350, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.interviews_pushButton.setFont(font)
        self.interviews_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.interviews_pushButton.setObjectName("interviews_pushButton")
        self.back_menu_pushButton = QtWidgets.QPushButton(parent=self.admin_preference_menu_frame)
        self.back_menu_pushButton.setGeometry(QtCore.QRect(190, 410, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.back_menu_pushButton.setFont(font)
        self.back_menu_pushButton.setStyleSheet("QPushButton:hover {\n"
"\n"
"                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));\n"
"                  color: rgb(255, 255, 255);\n"
"                  }\n"
"\n"
"QPushButton:pressed {\n"
"                    background-color: rgb(255, 255, 255);\n"
"                    color: rgb(0, 0, 255);\n"
"                    }")
        self.back_menu_pushButton.setObjectName("back_menu_pushButton")
        admin_pref_men_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=admin_pref_men_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        admin_pref_men_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=admin_pref_men_MainWindow)
        self.statusbar.setObjectName("statusbar")
        admin_pref_men_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(admin_pref_men_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(admin_pref_men_MainWindow)

        self.application_page_pushButton.clicked.connect(self.application_page_clicked)
        self.mentor_interview_pushButton.clicked.connect(self.mentor_interview_clicked)
        self.interviews_pushButton.clicked.connect(self.interviews_clicked)
        self.back_menu_pushButton.clicked.connect(self.back_menu_clicked)
        self.Exit_pushButton.clicked.connect(self.Exit_clicked)

    def retranslateUi(self, admin_pref_men_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        admin_pref_men_MainWindow.setWindowTitle(_translate("admin_pref_men_MainWindow", "                                                          Admin Preference Menu "))
        self.application_page_pushButton.setText(_translate("admin_pref_men_MainWindow", "Applications"))
        self.mentor_interview_pushButton.setText(_translate("admin_pref_men_MainWindow", "Mentor Interview"))
        self.Exit_pushButton.setText(_translate("admin_pref_men_MainWindow", "Exit"))
        self.interviews_pushButton.setText(_translate("admin_pref_men_MainWindow", "Interviews"))
        self.back_menu_pushButton.setText(_translate("admin_pref_men_MainWindow", "Main Menu"))

    def application_page_clicked(self):
        from  applications_page import Ui_applications_page_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_applications_page_MainWindow()
        self.ui.setupUi(self.MainWindow) 
        self.MainWindow.show()

    def mentor_interview_clicked(self):
        from mentor_interview_page import Ui_mentor_interviews_page_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_mentor_interviews_page_MainWindow()
        self.ui.setupUi(self.MainWindow) 
        self.MainWindow.show()


    def interviews_clicked(self):
        from interviews_page import Ui_interviews_page_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_interviews_page_MainWindow()
        self.ui.setupUi(self.MainWindow) 
        self.MainWindow.show() 

    def back_menu_clicked(self):
        from login_window import Ui_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow) 
        self.MainWindow.show()
        

    def Exit_clicked(self):
        from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
        QApplication.instance().quit()                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_pref_men_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_admin_pref_men_MainWindow()
    ui.setupUi(admin_pref_men_MainWindow)
    admin_pref_men_MainWindow.show()
    sys.exit(app.exec())
