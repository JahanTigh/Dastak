from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from shahr import *
from ping_pong_game import *
import os
import requests 
import random
import datetime
import string
import webbrowser
import jdatetime
import speech_recognition as sr



class Ui_MainWindow(object):
    def show_new_window_for_ab_o_hava(self):
        self.w = QtWidgets.QMainWindow()
        self.ui = Ui_city()
        self.ui.setupUi(self.w)
        self.w.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Persian assistant")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 781, 391))
        self.textBrowser.setStyleSheet("border-radius : 22px;")
        font = QtGui.QFont()
        font.setFamily("Digi Hekayat Bold")
        font.setPointSize(22)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(10, 458, 111, 91))
        self.run.setStyleSheet("border : 1px solid black; border-radius : 20px;")
        font = QtGui.QFont()
        font.setFamily("Digi Hekayat Bold")
        font.setPointSize(22)
        self.run.setFont(font)
        self.run.setObjectName("run")
        self.komack = QtWidgets.QPushButton(self.centralwidget)
        self.komack.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.komack.setStyleSheet("border : 1px solid black; border-radius : 10px;")
        font = QtGui.QFont()
        font.setFamily("Digi Hekayat Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.komack.setFont(font)
        self.komack.setObjectName("komack")
        self.github = QtWidgets.QPushButton(self.centralwidget)
        self.github.setGeometry(QtCore.QRect(210, 10, 181, 31))
        self.github.setStyleSheet("border : 1px solid black; border-radius : 10px;")
        font = QtGui.QFont()
        font.setFamily("Digi Hekayat Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.github.setFont(font)
        self.github.setObjectName("github")
        self.site = QtWidgets.QPushButton(self.centralwidget)
        self.site.setGeometry(QtCore.QRect(410, 10, 181, 31))
        self.site.setStyleSheet("border : 1px solid black; border-radius : 10px;")
        font = QtGui.QFont()
        font.setFamily("Digi Hekayat Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.site.setFont(font)
        self.site.setObjectName("site")
        self.donit = QtWidgets.QPushButton(self.centralwidget)
        self.donit.setGeometry(QtCore.QRect(610, 10, 181, 31))
        self.donit.setStyleSheet("border : 1px solid black; border-radius : 10px;")
        font = QtGui.QFont()
        font.setFamily("Digi Hekayat Bold")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.donit.setFont(font)
        self.donit.setObjectName("donit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 458, 541, 91))
        self.lineEdit.setStyleSheet("border : 1px solid black; border-radius : 20px;")
        font = QtGui.QFont()
        font.setFamily("Digi Hekayat Bold")
        font.setPointSize(22)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.mic = QtWidgets.QPushButton(self.centralwidget)
        self.mic.setGeometry(QtCore.QRect(680, 458, 111, 91))
        self.mic.setStyleSheet("border : 1px solid black; border-radius : 20px;")
        font = QtGui.QFont()
        font.setFamily("Digi Hekayat Bold")
        font.setPointSize(21)
        self.mic.setFont(font)
        self.mic.setObjectName("mic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuPersian_assistant = QtWidgets.QMenu(self.menubar)
        self.menuPersian_assistant.setObjectName("menuPersian_assistant")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuPersian_assistant.menuAction())
        self.retranslateUi(MainWindow)
        self.run.clicked.connect(self.get_data)
        self.mic.clicked.connect(self.get_audio)
        self.komack.clicked.connect(self.help)
        self.github.clicked.connect(self.github_open)
        self.site.clicked.connect(self.site_open)
        self.donit.clicked.connect(self.donit_open)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.run, self.textBrowser)
        MainWindow.setTabOrder(self.textBrowser, self.komack)
        self.textBrowser.setText('')
        open(f"C:\\Users\\{os.getlogin()}\\Documents\\shahr.txt",'a+' , encoding="utf8")
        if os.lstat(f"C:\\Users\\{os.getlogin()}\\Documents\\shahr.txt")[6] == 0 :
            self.show_new_window_for_ab_o_hava()
            red_text = "الان یه پنجره باز شده که ازت شهر رو می پرسه لطفا بازش کن"
            self.textBrowser.setHtml(f"<p6 style=\"color:#ff0000;\" > {red_text} </p6>")
        else:
            self.textBrowser.append('سلام\n چی کار می تونم برات انجام بدم؟\n')
        global joks
        f = open('jok.txt', encoding="utf8")
        joks = f.readlines()

    def trans(self, to_lang, text):
        translator= translator(to_lang=to_lang)
        return translator.translate(text)

          
    def get_audio(self):
        self.lineEdit.setText('')
        r = sr.Recognizer()
        app.processEvents()
        with sr.Microphone() as source:
            app.processEvents()
            r.adjust_for_ambient_noise(source)
            app.processEvents()
            self.textBrowser.append('\nدارم بهت گوش می دم...(لطفا با آرامش صحبت کن تا متوجه بشم)') 
            app.processEvents()
            audio = r.listen(source)
            app.processEvents()
            try:
                app.processEvents()     
                voice_U = (r.recognize_google(audio, language= 'fa-IR'))
                app.processEvents()
                self.lineEdit.setText(voice_U)
                app.processEvents()
                self.textBrowser.append('\n'+voice_U)
                app.processEvents()
                self.get_data()
            except:
                self.textBrowser.append("\nمتوجه نشدم دوباره روی میکروفون ضربه بزن و امتحان کن")
    def passw(self):
        char = string.ascii_letters + string.punctuation + string.digits       
        passw = ''.join(random.choice(char) for x in range(16))
        self.textBrowser.append('\n'+passw)    

    def time(self):
        today = datetime.datetime.now()
        r = requests.get('https://www.time.ir/')
        soup = BeautifulSoup(r.text, 'html.parser')
        chandom_ghamari = soup.find('span', attrs={'id':"ctl00_cphTop_Sampa_Web_View_TimeUI_ShowDate00cphTop_3734_lblHijri"}).text
        chandom_shamsi = (jdatetime.date.fromgregorian(day = today.day, month = today.month, year = today.year))
        chandom_shamsi = str(chandom_shamsi)
        chandom_miladi = today.year, today.month, today.day
        self.textBrowser.append(f'\nالان ساعت :\n{ today.hour} : {today.minute} : {today.second}')
        self.textBrowser.append(f'امروز به تاریخ شمسی : \n{chandom_shamsi}')
        self.textBrowser.append(f'امروز به تاریخ میلادی : \n{chandom_miladi}')
        self.textBrowser.append(f'امروز به تاریخ قمری : \n{chandom_ghamari}')

    def tass(self):
        tass = str(random.randint(1, 6))
        self.textBrowser.append((f'\nبرات تاس انداختم « {tass} » اومد'))

    def jok(self):
        if len(joks) == 0:
            self.textBrowser.append('\nجوک هام تموم شد!!!')
        else:
            randomjok = random.choice(joks)
            joks.remove(randomjok)
            self.textBrowser.append('\n'+randomjok)
    
    def khamoosh(self):
        self.textBrowser.append('تا ۱۱ ثانیه دیگه کامپیوتر خاموش می شه\nمسی تونی سریع من رو ببندی تا خاموش نشه')
        sleep(11)
        os.system('shutdown -s -t 00')
    
    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]

    
    def ab_o_hava(self):
        try:
            self.textBrowser.append('\nوایسا برم آسمون رو نگاه کنم\U0001F601')
            f = open(f"C:\\Users\\{os.getlogin()}\\Documents\\shahr.txt",'r' , encoding="utf-8")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            city = f.read()
            city = city + " weather"
            city = city.replace(" ", "+")
            res = requests.get(
                f'https://www.google.com/search?q={city}&hl=fa&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            location = soup.select('#wob_loc')[0].getText().strip()
            time = soup.select('#wob_dts')[0].getText().strip()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()
            self.textBrowser.append('\n'+location)
            self.textBrowser.append(time)
            self.textBrowser.append(info)
            self.textBrowser.append(weather+"°C")
        except Exception as e:
            error = str(sys.exc_info()[1])[:12]
            if error == 'HTTPSConnect':
                self.textBrowser.append('به اینترنت وصل نیستی!!!')
            else:
                self.textBrowser.append('یه مشکلی هست!!!')
        
    def site_open(self):
        webbrowser.open_new('http://jahantigh.gigfa.com/')
    def github_open(self):
        webbrowser.open_new('https://github.com/yasinprogrammer')
    def donit_open(self):
        webbrowser.open_new('https://idpay.ir/yasinjahantigh')
    def help(self):
        self.textBrowser.setText('برات پسورد بسازم\nساعت رو بگم\nتاریخ رو به شمسی، میلادی و قمری بگم\nبرات تاس بندازم\nبرات جوک بگم\nآی‌پی (IP) دستگاهت رو بگم\nآب‌و‌هوا رو بهت بگم\nباهات پینگ پونگ بازی کنم\nدستگاهت رو خاموش کنم')

    def get_data(self):
        input_U = self.lineEdit.text()
        if 'چه کاری بلدی' in input_U or 'چه کارهایی بلدی' in input_U:
            self.help()
        elif 'پسورد' in input_U or 'رمز' in input_U or 'ms,vn' in input_U.lower() or '\s,vn' in input_U.lower() or '`s,vn`' in input_U.lower() or 'vlc' in input_U.lower():
            self.passw()
    
        elif 'تاریخ' in input_U or 'زمان' in input_U or 'ساعت' in input_U or 'امروز' in input_U or 'چندم' in input_U or 'jhvdo' in input_U.lower() or 'clhk' in input_U.lower() or 'shuj' in input_U.lower() or 'hlv,c' in input_U.lower() or ']knl' in  input_U.lower():
            self.time()

        elif 'تاس' in input_U or 'jhs' in input_U:
            self.tass()

        elif 'جوک' in input_U or '[,;' in input_U.lower():
            self.jok()

        elif 'خاموش' in input_U or 'شات دان' in input_U or 'شاتدان' in input_U or 'ohl,a' in input_U.lower() or 'ahj nhk' in input_U.lower() or 'ahjnhk' in input_U.lower():
            self.khamoosh()

        elif 'ip' in  input_U.lower() or 'آی پی' in input_U or 'آیپی' in input_U or 'hdmd' in input_U.lower() or 'hd md' in input_U.lower() or 'ای پی' in input_U or 'ایپی' in input_U:
            self.textBrowser.append('\nالان بهت می گم...\n')
            self.textBrowser.append(f'\nآی پی تو الان «{self.get_ip()}» هست')

        elif 'هوا' in input_U or 'درجه' in input_U or 'i,h' in input_U.lower() or 'nv[i' in input_U.lower():
            self.ab_o_hava()
        
        elif 'بازی' in input_U or 'گیم' in input_U or 'fhcd' in input_U.lower() or "'dl" in input_U.lower() or 'game' in input_U.lower():
            self.textBrowser.append('بفرما پینگ پونگ بازی کن')
            ping_pong_game()

        else:
            self.textBrowser.append(('\nمتوجه نشدم یک بار دیگه دستورت رو بنویس (احتمالا کاری رو که می خوای من بلد نیستم\U0001F614)'))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Persian assistant", "Persian assistant"))
        self.textBrowser.setHtml(_translate("Persian assistant", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.run.setText(_translate("Persian assistant", "اجراکن"))
        self.komack.setText(_translate("Persian assistant", "!راهنما"))
        self.github.setText(_translate("Persian assistant", "گیت هابم"))
        self.site.setText(_translate("Persian assistant", "وب سایتم"))
        self.donit.setText(_translate("Persian assistant", "حمایت"))
        self.lineEdit.setPlaceholderText(_translate("Persian assistant", "دستورت رو اینجا تایپ کن"))
        self.mic.setText(_translate("Persian assistant", "میکروفون"))
        self.menuPersian_assistant.setTitle(_translate("Persian assistant", "Persian assistant"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
