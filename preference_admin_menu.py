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
        admin_pref_men_MainWindow.resize(800, 600)
        admin_pref_men_MainWindow.setAcceptDrops(False)
        admin_pref_men_MainWindow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        admin_pref_men_MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(parent=admin_pref_men_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.admin_preference_menu_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.admin_preference_menu_frame.setGeometry(QtCore.QRect(-140, -100, 721, 661))
        self.admin_preference_menu_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.admin_preference_menu_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.admin_preference_menu_frame.setObjectName("admin_preference_menu_frame")
        self.werhere_image_label = QtWidgets.QLabel(parent=self.admin_preference_menu_frame)
        self.werhere_image_label.setGeometry(QtCore.QRect(210, 110, 481, 101))
        self.werhere_image_label.setText("")
        self.werhere_image_label.setPixmap(QtGui.QPixmap("werhere_image.png"))
        self.werhere_image_label.setObjectName("werhere_image_label")
        self.application_page_pushButton = QtWidgets.QPushButton(parent=self.admin_preference_menu_frame)
        self.application_page_pushButton.setGeometry(QtCore.QRect(220, 240, 75, 24))
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
        self.mentor_interview_pushButton.setGeometry(QtCore.QRect(460, 240, 101, 31))
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
        self.Exit_pushButton.setGeometry(QtCore.QRect(460, 370, 101, 31))
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
        self.interviews_pushButton.setGeometry(QtCore.QRect(220, 360, 81, 31))
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
        self.back_menu_pushButton.setGeometry(QtCore.QRect(230, 470, 75, 24))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        admin_pref_men_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=admin_pref_men_MainWindow)
        self.statusbar.setObjectName("statusbar")
        admin_pref_men_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(admin_pref_men_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(admin_pref_men_MainWindow)

    def retranslateUi(self, admin_pref_men_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        admin_pref_men_MainWindow.setWindowTitle(_translate("admin_pref_men_MainWindow", "                                                          Admin Preference Menu "))
        self.application_page_pushButton.setText(_translate("admin_pref_men_MainWindow", "Applications"))
        self.mentor_interview_pushButton.setText(_translate("admin_pref_men_MainWindow", "Mentor Interview"))
        self.Exit_pushButton.setText(_translate("admin_pref_men_MainWindow", "Exit"))
        self.interviews_pushButton.setText(_translate("admin_pref_men_MainWindow", "Interviews"))
        self.back_menu_pushButton.setText(_translate("admin_pref_men_MainWindow", "Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_pref_men_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_admin_pref_men_MainWindow()
    ui.setupUi(admin_pref_men_MainWindow)
    admin_pref_men_MainWindow.show()
    sys.exit(app.exec())