from time import sleep, time
from PyQt5 import QtCore, QtGui, QtWidgets
from shahr import *
from translate import Translator
import os
import requests 
import random
import datetime
import string
import webbrowser
import pylunar
import jdatetime
import speech_recognition as sr
import pygame


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
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(10, 460, 111, 91))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.run.setFont(font)
        self.run.setObjectName("run")
        self.komack = QtWidgets.QPushButton(self.centralwidget)
        self.komack.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.komack.setFont(font)
        self.komack.setObjectName("komack")
        self.github = QtWidgets.QPushButton(self.centralwidget)
        self.github.setGeometry(QtCore.QRect(210, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.github.setFont(font)
        self.github.setObjectName("github")
        self.site = QtWidgets.QPushButton(self.centralwidget)
        self.site.setGeometry(QtCore.QRect(410, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.site.setFont(font)
        self.site.setObjectName("site")
        self.donit = QtWidgets.QPushButton(self.centralwidget)
        self.donit.setGeometry(QtCore.QRect(610, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.donit.setFont(font)
        self.donit.setObjectName("donit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 460, 541, 91))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.mic = QtWidgets.QPushButton(self.centralwidget)
        self.mic.setGeometry(QtCore.QRect(680, 460, 111, 91))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
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
        f = open('shahr.txt','a+' , encoding="utf8")
        shahr = f.readlines()
        if os.lstat("shahr.txt")[6] == 0 :
            self.show_new_window_for_ab_o_hava()
            red_text = "الان یه پنجره باز شده که ازت شهر رو می پرسه لطفا بازش کن"
            self.textBrowser.setHtml(f"<p6 style=\"color:#ff0000;\" > {red_text} </p6>")
        else:
            self.textBrowser.append('سلام\n چی کار می تونم برات انجام بدم؟\n')
            
    def get_audio(self):
        app.processEvents()
        self.lineEdit.setText('')
        app.processEvents()
        r = sr.Recognizer()
        app.processEvents()
        with sr.Microphone() as source:
            app.processEvents()
            r.adjust_for_ambient_noise(source)
            app.processEvents()
            self.textBrowser.append('')
            app.processEvents()
            self.textBrowser.append('دارم بهت گوش می دم...(لطفا با آرامش صحبت کن تا متوجه بشم)') 
            app.processEvents()
            audio = r.listen(source)
            app.processEvents()
            try:     
                app.processEvents()
                voice_U = (r.recognize_google(audio, language= 'fa-IR'))
                app.processEvents()
                self.lineEdit.setText(voice_U)
                app.processEvents()
                self.textBrowser.append('')
                app.processEvents()
                self.textBrowser.append(voice_U)
                app.processEvents()
                self.get_data()
                app.processEvents()
            except:
                app.processEvents()
                self.textBrowser.append('')
                app.processEvents()
                self.textBrowser.append("متوجه نشدم دوباره روی میکروفون ضربه بزن و امتحان کن")
                app.processEvents()
    def passw(self):
        char = string.ascii_letters + string.punctuation + string.digits       
        passw = ''.join(random.choice(char) for x in range(16))
        self.textBrowser.append('')
        self.textBrowser.append(passw)    

    def time(self):
        moon = pylunar.MoonInfo((35, 42, 55.0728),(51,24,15.6348))
        today = datetime.datetime.now()
        moon.update((today.year, today.month, today.day, today.hour, today.minute, today.second))
        age = (moon.age())
        chandom_ghamari = int(age) + 1

        chandom_shamsi = (jdatetime.date.fromgregorian(day = today.day, month = today.month, year = today.year))
        chandom_shamsi = str(chandom_shamsi)

        chandom_miladi = today.year, today.month, today.day
        self.textBrowser.append('')
        self.textBrowser.append(f'الان ساعت :\n{ today.hour} : {today.minute} : {today.second}')
        self.textBrowser.append(f'امروز به تاریخ شمسی : \n{chandom_shamsi}')
        self.textBrowser.append(f'امروز به تاریخ میلادی : \n{chandom_miladi}')
        self.textBrowser.append( f'امروز « {chandom_ghamari} » ماه قمری به افق تهران هست(دقت کن که من هر دفعه نمی رم برات آسمون رو نگاه کنم\U0001F609\U0001F601)')

    def tass(self):
        tass = str(random.randint(1, 6))
        self.textBrowser.append('')
        self.textBrowser.append((f'برات تاس انداختم « {tass} » اومد'))
        self.show_new_window()

    def jok(self):
        try:
            f = open('jok.txt', encoding="utf8")
            joks = f.readlines()
            rand = random.randint(0, len(joks))
            print (joks[rand])
            self.textBrowser.append('')
            self.textBrowser.append(joks[rand])
        except:
            self.jok()
    
    def khamoosh(self):
        self.textBrowser.append('')
        self.textBrowser.append('تا ۱۱ ثانیه دیگه کامپیوتر خاموش می شه\nمسی تونی سریع من رو ببندی تا خاموش نشه')
        sleep(11)
        os.system('shutdown -s -t 00')
    
    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]

    
    def ab_o_hava(self):
        f = open('shahr.txt','r' , encoding="utf8")
        shahr = f.read()
        try:
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + shahr 
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]

                current_temperature = y["temp"]
                z = x["weather"]
                current_temperature = float(current_temperature) -273.15
                weather_description = z[0]["description"]
                translator= Translator(to_lang="fa")
                weather_description_t = translator.translate(weather_description)
                hava = (f'الان هوا تو {shahr} {str(current_temperature.__round__(2))} درجه سانتی‌گراده و وضعیت هوا: {str(weather_description_t)}')#" Temperature  = " + str(current_temperature) + "\n description = " + str(weather_description))
                self.textBrowser.append(hava)
            else:
                self.textBrowser.append("شهر شما پیدا نشد")
        except:
            self.textBrowser.append('اینترنتت رو دوباره چک کن')

    def ping_pong_game(self):
        self.textBrowser.append('بفرما پینگ پونگ بازی کن')
        pygame.init()

        screen=pygame.display.set_mode((640,480),0,32)
        pygame.display.set_caption("Pong Pong!")

        #Creating 2 bars, a ball and background.
        back = pygame.Surface((640,480))
        background = back.convert()
        background.fill((0,0,0))
        bar = pygame.Surface((10,50))
        bar1 = bar.convert()
        bar1.fill((0,0,255))
        bar2 = bar.convert()
        bar2.fill((255,0,0))
        circ_sur = pygame.Surface((15,15))
        circ = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
        circle = circ_sur.convert()
        circle.set_colorkey((0,0,0))

        # some definitions
        bar1_x, bar2_x = 10. , 620.
        bar1_y, bar2_y = 215. , 215.
        circle_x, circle_y = 307.5, 232.5
        bar1_move, bar2_move = 0. , 0.
        speed_x, speed_y, speed_circ = 250., 250., 250.
        bar1_score, bar2_score = 0,0
        #clock and font objects
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("calibri",40)

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        bar1_move = -ai_speed
                    elif event.key == pygame.K_DOWN:
                        bar1_move = ai_speed
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        bar1_move = 0.
                    elif event.key == pygame.K_DOWN:
                        bar1_move = 0.
            
            score1 = font.render(str(bar1_score), True,(255,255,255))
            score2 = font.render(str(bar2_score), True,(255,255,255))

            screen.blit(background,(0,0))
            frame = pygame.draw.rect(screen,(255,255,255),pygame.Rect((5,5),(630,470)),2)
            middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
            screen.blit(bar1,(bar1_x,bar1_y))
            screen.blit(bar2,(bar2_x,bar2_y))
            screen.blit(circle,(circle_x,circle_y))
            screen.blit(score1,(250.,210.))
            screen.blit(score2,(380.,210.))

            bar1_y += bar1_move
            
        # movement of circle
            time_passed = clock.tick(30)
            time_sec = time_passed / 1000.0
            
            circle_x += speed_x * time_sec
            circle_y += speed_y * time_sec
            ai_speed = speed_circ * time_sec
        #AI of the computer.
            if circle_x >= 305.:
                if not bar2_y == circle_y + 7.5:
                    if bar2_y < circle_y + 7.5:
                        bar2_y += ai_speed
                    if  bar2_y > circle_y - 42.5:
                        bar2_y -= ai_speed
                else:
                    bar2_y == circle_y + 7.5
            
            if bar1_y >= 420.: bar1_y = 420.
            elif bar1_y <= 10. : bar1_y = 10.
            if bar2_y >= 420.: bar2_y = 420.
            elif bar2_y <= 10.: bar2_y = 10.
        #since i don't know anything about collision, ball hitting bars goes like this.
            if circle_x <= bar1_x + 10.:
                if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
                    circle_x = 20.
                    speed_x = -speed_x
            if circle_x >= bar2_x - 15.:
                if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
                    circle_x = 605.
                    speed_x = -speed_x
            if circle_x < 5.:
                bar2_score += 1
                circle_x, circle_y = 320., 232.5
                bar1_y,bar_2_y = 215., 215.
            elif circle_x > 620.:
                bar1_score += 1
                circle_x, circle_y = 307.5, 232.5
                bar1_y, bar2_y = 215., 215.
            if circle_y <= 10.:
                speed_y = -speed_y
                circle_y = 10.
            elif circle_y >= 457.5:
                speed_y = -speed_y
                circle_y = 457.5

            pygame.display.update()


    def site_open(self):
        webbrowser.open_new('http://jahantigh.gigfa.com/')
    def github_open(self):
        webbrowser.open_new('https://github.com/yasinprogrammer')
    def donit_open(self):
        webbrowser.open_new('https://idpay.ir/yasinjahantigh')
    def help(self):
        self.textBrowser.setText(' کار هایی که فعلا بلدم ایناس: \nتاس بندازم \nرمز عبور قوی بسازم \nساعت رو بهت بگم \nتاریخ رو به میلادی بگم \nتاریخ رو به شمسی بگم \nبگم امروز چندم ماهه قمریه  \n برات جوک بگم \n کامپیوتر رو خاموش کنم  \n')

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
            self.textBrowser.append('')
            self.textBrowser.append('الان بهت می گم...')
            self.textBrowser.append('')
            self.textBrowser.append(f'\nآی پی تو الان «{self.get_ip()}» هست')

        elif 'هوا' in input_U or 'درجه' in input_U or 'i,h' in input_U.lower() or 'nv[i' in input_U.lower():
            self.textBrowser.append('')
            self.textBrowser.append('وایسا برم آسمون رو نگاه کنم\U0001F601')
            self.ab_o_hava()
        
        elif 'بازی' in input_U or 'گیم' in input_U or 'fhcd' in input_U.lower() or "'dl" in input_U.lower() or 'game' in input_U.lower():
            self.ping_pong_game()

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
