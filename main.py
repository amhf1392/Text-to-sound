import sys
import pyttsx3
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # تنظیمات پنجره اصلی
        self.setObjectName("MainWindow")
        self.resize(727, 518)

        # تغییر عنوان پنجره
        self.setWindowTitle("Text To Sound")  # این خط رو اضافه کردیم

        # ایجاد ویجت مرکزی
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        # ایجاد و تنظیم QLabel (برای عنوان)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 101))
        self.label.setAcceptDrops(False)
        self.label.setStyleSheet("font: 26pt \"MS Shell Dlg 2\";\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(0, 0, 255);")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        
        # ایجاد و تنظیم دکمه Start
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(250, 300, 231, 51))
        self.start_btn.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
                                     "border: 3px solid blue;\n"
                                     "border-radius: 5px;\n"
                                     "selection-color: rgb(255, 255, 255);\n"
                                     "selection-background-color: rgb(0, 0, 255);")
        self.start_btn.setObjectName("start_btn")
        
        # ایجاد و تنظیم QLabel (برای راهنمایی متن)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 210, 131, 31))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        
        # ایجاد و تنظیم QLineEdit (برای وارد کردن متن)
        self.text_line = QtWidgets.QLineEdit(self.centralwidget)
        self.text_line.setGeometry(QtCore.QRect(210, 210, 401, 41))
        self.text_line.setStyleSheet("border: 3px solid blue;\n"
                                     "border-radius: 5px;")
        self.text_line.setText("")
        self.text_line.setObjectName("text_line")
        
        # تنظیم ویجت مرکزی
        self.setCentralWidget(self.centralwidget)
        
        # تنظیم نوار منو
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        
        # تنظیم نوار وضعیت
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        # ترجمه متن‌های UI
        self.retranslateUi()

        # اتصال دکمه Start به تابع تبدیل متن به صدا
        self.start_btn.clicked.connect(self.text_to_sound)

        # مقداردهی اولیه موتور pyttsx3
        self.engine = pyttsx3.init()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        #self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                  Text To Sound"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "Enter Text:"))

    def text_to_sound(self):
        text = self.text_line.text()  # دریافت متن از text_line
        self.engine.say(text)         # تبدیل متن به صدا
        self.engine.runAndWait()      # اجرای موتور تبدیل صدا


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
