pyuic6 -x login_window.ui -o login_window.py
***********************************************************************************************
tabwidget- iç içe pencere oluşturma
***********************************************************************************************************
Resim için --->boş label koy---> Qlabel menü---> pixmap(search yaparakta bulabilirsin)---> dosya seç

***********************************************************************************************************
Size sabitleme----> MainWindow size sabit olmalı bunun için max ve min değerleri aynı olacak
                    Frame size sabit olmalı  bunun için max ve min değerleri aynı olacak
***************************************************************************************************
nesnenin üzerine sağ tuş tıkla---> changeStylesheet----->color


*******************BUTON TANIMLAMA FONKSİYONLARI *******************

self.admin_login_pushButton.clicked.connect(self.admin_login_clicked)

def admin_login_clicked(self):
        print("Admin Login düğmesine tıklandı!")

   
********************************button Hover Rengi Değiştirme ****************************************************************************************

QPushButton:hover {

                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));
                  color: rgb(255, 255, 255);
                  }

QPushButton:pressed {
                    background-color: rgb(255, 255, 255);
                    color: rgb(0, 0, 255);
                    }
*************************************************Text Edit Hover Rengi değitirme*************************************************************************************************************
QTextEdit:hover {

                  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0,157, 255, 255), stop:1 rgba(30, 206, 255, 255));
                  color: rgb(255, 255, 255);
                  }

QTextEdit:pressed {
                    background-color: rgb(255, 255, 255);
                    color: rgb(0, 0, 255);
                    }
**********************************************************************************************************************************************************

******************************PushButton SAYFA ATLATMA FONSİYONU*******************************
def admin_login_clicked(self):
        from admin_menu import Ui_Admin_menu_MainWindow
        self.MainWindow= QtWidgets.QMainWindow()
        self.ui =Ui_Admin_menu_MainWindow()
        self.ui.setupUi(MainWindow)   

************************************************************************************************ 




