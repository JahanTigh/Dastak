from PyQt5 import QtCore, QtGui, QtWidgets
import os
import random
import datetime
import string
import webbrowser
import pylunar
import jdatetime
import speech_recognition as sr 



class Ui_MainWindow(object):
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
        self.textBrowser.setText('سلام \n چی کار می تونم برات انجام بدم؟')


    def get_audio(self):
        self.lineEdit.setText('')
        app.processEvents()
        r = sr.Recognizer()
        app.processEvents()
        with sr.Microphone() as source:
            app.processEvents()
            r.adjust_for_ambient_noise(source)
            app.processEvents()
            self.textBrowser.append('دارم بهت گوش می دم...(لطفا با آرامش صحبت کن تا متوجه بشم)') 
            app.processEvents()
            audio = r.listen(source)
            app.processEvents()
            try:     
                app.processEvents()
                voice_U = (r.recognize_google(audio, language= 'fa-IR'))
                self.lineEdit.setText(voice_U)
                self.textBrowser.setText(voice_U)
                app.processEvents()
                self.get_data()
            except:
                app.processEvents()
                self.textBrowser.append("متوجه نشدم دوباره روی میکروفون ضربه بزن و امتحان کن")
                app.processEvents()
    
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
            char = string.ascii_letters + string.punctuation + string.digits       
            passw = ''.join(random.choice(char) for x in range(16))
            self.textBrowser.append(passw)
        

        # elif 'سنگ' in input_U or 'بازی' in input_U: #TODO اینجا برای ورودی گرفتن از کاربر مشکل دارم ممنون می شم کمک کنید
        #     self.textBrowser.setText('سنگ...')
        #     self.textBrowser.setText('کاغذ...')
        #     self.textBrowser.setText('قیچی...')
        #     self.textBrowser.setText('--------------------------')

        #     randomNumber = random.randint(0, 2)

        #     if randomNumber == 0:
        #         computerMove = 'سنگ' #rock
        #     elif randomNumber == 1:
        #         computerMove = 'کاغذ' #paper
        #     elif randomNumber == 2:
        #         computerMove = 'قیچی'#scissors

        #     player1_wins = 0
        #     player2_wins = 0
        #     self.textBrowser.setText(('چند دست می خوای بازی کنی؟'))
        #     while True:
        #         try:
        #             winning_score = self.lineEdit.text()
        #             winning_score = int(winning_score)
        #         except:
        #             self.textBrowser.setText('b')
        #             break

        #     while player1_wins < winning_score and player2_wins < winning_score:
        #         self.textBrowser.setText(f'شما : {player1_wins} کامپیوتر : {player2_wins}')
        #         self.textBrowser.setText(('حرکت شما'))
        #         Player_1 = input()
        #         self.textBrowser.setText(('حرکت کامپیوتر:'))
        #         self.textBrowser.setText((computerMove))
        #         Player_2 = computerMove

        #         if Player_1 == Player_2:
        #             self.textBrowser.setText(('مساوی...'))
        #         elif Player_1 == 'سنگ':
        #             if Player_2 == 'قیچی':
        #                 self.textBrowser.setText(('تو برنده شدی!...'))
        #                 player1_wins += 1
        #             elif Player_2 == 'کاغذ':
        #                 self.textBrowser.setText(('کامپیوتر برنده شد!...'))
        #                 player2_wins += 1
        #         elif Player_1 == 'کاغذ':
        #             if Player_2 == 'سنگ':
        #                 self.textBrowser.setText(('تو برنده شدی!...'))
        #                 player1_wins += 1
        #             elif Player_2 == 'قیچی':
        #                 self.textBrowser.setText(('کامپیوتر برنده شد!...'))
        #                 player2_wins += 1
        #         elif Player_1 == 'قیچی':
        #             if Player_2 == 'کاغذ':
        #                 self.textBrowser.setText(('تو برنده شدی!...'))
        #                 player1_wins += 1
        #             elif Player_2 == 'سنگ':
        #                 self.textBrowser.setText(('کامپیوتر برنده شد!...'))
        #                 player2_wins += 1
        #         else:
        #             self.textBrowser.setText(('یه چیزی اشتباهه!...'))

        #     self.textBrowser.setText(('بازی تموم شد!...'))

        #     self.textBrowser.setText(f' شما : {player1_wins} | کامپیوتر : {player2_wins}')


        elif 'تاریخ' in input_U or 'زمان' in input_U or 'ساعت' in input_U or 'امروز' in input_U or 'چندم' in input_U or 'jhvdo' in input_U.lower() or 'clhk' in input_U.lower() or 'shuj' in input_U.lower() or 'hlv,c' in input_U.lower() or ']knl' in  input_U.lower():
            moon = pylunar.MoonInfo((35, 42, 55.0728),(51,24,15.6348))
            today = datetime.datetime.now()
            moon.update((today.year, today.month, today.day, today.hour, today.minute, today.second))
            age = (moon.age())
            chandom_ghamari = int(age) + 1

            chandom_shamsi = (jdatetime.date.fromgregorian(day = today.day, month = today.month, year = today.year))
            chandom_shamsi = str(chandom_shamsi)

            chandom_miladi = today.year, today.month, today.day

            self.textBrowser.append(f'الان ساعت :\n{ today.hour} : {today.minute} : {today.second}')
            self.textBrowser.append(f'امروز به تاریخ شمسی : \n{chandom_shamsi}')
            self.textBrowser.append(f'امروز به تاریخ میلادی : \n{chandom_miladi}')
            self.textBrowser.append( f'امروز « {chandom_ghamari} » ماه قمری به افق تهران هست(دقت کن که من هر دفعه نمی رم برات آسمون رو نگاه کنم\U0001F609\U0001F601)')

        elif 'تاس' in input_U or 'jhs' in input_U:
            tass = str(random.randint(1, 6))
            self.textBrowser.append((f'برات تاس انداختم « {tass} » اومد'))



        elif 'جوک' in input_U or '[,;' in input_U.lower():
            try:
                randomjok = random.randint(1, 11)
                if randomjok == 1:
                    compeyoterjok = 'چن وخ پیش به پسر عموم گفتم واسم ایمیل بساز رمزشم واسم بفرست گفت باشه آدرس ایمیلمو فرستاد، گفتم پس رمزش کو؟ گفت واست ایمیل کردم من قضاوت رو به کارشناسا واگذار میکنم '
                
                elif randomjok == 2:
                    compeyoterjok ='تخمه آفتابگردون كيلويی 39 تومن تسبيح دونه‌ای 40 تومن كاپشن پفی 400 تومن شلوار شيش جيب 280 تومن كتونی تايگر فيک 180 تومن! واسه سر كوچه الاف واستادن و تخمه شكستن تو ايران الان حدودا ۱ تومن سرمايه لازمه! '

                elif randomjok == 3:
                    compeyoterjok ='سوالات متداول از مامان: گشنمه….  شام کی حاضر میشه!؟  سردمه!!  پیرهنم کجاست!؟  اون شلوار مشکیمو شستی!؟  نمیتونم پیداش کنم!!  ناهارچی داریم!؟  این چرا اتو نداره!؟  سوالات متداول از بابا: مامان کجاست؟! '

                elif randomjok == 4:
                    compeyoterjok ='یک معمای خیلی جالب: سه تابچه تو خونه بودن اولی عشق نام داشت دومی محبت نام داشت و سومی دوستت دارم بود یک روز پدرشان عشق و محبت رابه بازار برد حالا بگو کی خونه مونده؟؟؟؟ نشنیدم بازم بگو؟ واقعاً؟!!!!! '

                elif randomjok == 5:
                    compeyoterjok ='یارو میره هارد بخره میگه هارد 640 میخوام حیف نون هارد 500 میاره بهش میگه گفتم 640 میگه: ناراحت نباش جا وا می‌کنه…!!! '

                elif randomjok == 7:
                    compeyoterjok ='کبوتر با کبوتر باز باران با ترانه میخورد بر بامش بیش برفش بیشتر آمدی جانم به قربانت ولی حالا چرا عاقل کند کاری که باز آید به کنعان غم مخور خربزه با پوست موزو میندازی زمین هوا میره نمیدونی تا کجا میره!! '

                elif randomjok == 8:
                    compeyoterjok ='ای کسانی که با خیال راحت ماسک فیلتر دار استفاده می‌کنید! بدانید و آگاه باشید که کرونا در ایران مانند شهروندان این کشور به فیلتر شکن مجهز است!!'

                elif randomjok == 9:
                    compeyoterjok ='آب رﯾﺰﺵ ﺑﯿﻨﻰ ﺩﺍﺭﻡ. ﺭﻓﺘﻢ ﺩﺍﺭﻭﺧﻮﻧﻪ ﻗﺮﺹ ﺿﺪﺣﺴﺎﺳﯿﺖ ﺑﮕﯿﺮﻡ. ﺗﻮ ﻋﻮﺍﺭﺽ ﺟﺎﻧﺒﯿﺶ ﻧﻮﺷﺘﻪ ﺳﺮ ﺩﺭﺩ و ﺳﺮ ﮔﯿﺠﻪ ﺣﺎﻟﺖ تهوع ﺍﺧﺘﻼﻝ ﺩﺭ ﺧﻮﺍﺏ ﻧﺎﺭﺳﺎﯾﻰ ﮐﺒﺪ ﺳﮑﺘﻪ ﻗﺒﻠﻰ و ﺳﮑﺘﻪ ﻯ ﻣﻐﺰﻯﻣﺮﮒ ﻧﺎﮔﮭﺎﻧﻰ!… ﮪﯿﭽﻰ ﺩﯾﮕﻪ … ﭘﺸﯿﻤﻮﻥ ﺷﺪﻡ با آستینم پاکش می‌کنم ﺍﻣﻨﯿﺘﺶ ﺑﯿﺸﺘﺮﻩ؟!'

                elif randomjok == 10:
                    compeyoterjok ='ﺍﮔﺮ ﺩﯾﺪﯼ ﺟﻮﺍﻧﯽ ﺑﺮﺩﺭﺧﺘﯽ ﺗﮑﯿﻪ ﮐﺮﺩﻩ ﺳﺮﯾﻊ ﺑﯿﺎﺭﯾﺪﺵ ﮐﻨﺎﺭ ﯾﻬﻮ ﮔﻼﺑﯽ ﭼﯿﺰﯼ می‌خوره ﺗﻮﺳﺮﺵ چهار تا فرمول ﺑﻪ ﻓﯿﺰﯾﮏ ﺍﺿﺎﻓﻪ ﻣﯿﮑﻨﻪ ﺑﺪﺑﺨﺖ می‌شیم'
                
                elif randomjok == 11:
                    compeyoterjok  ='یه عدد بین 10 تا 20 انتخاب کن \n اون عدد رو با 32 جمع کن\nحاصل رو ضرب در 2 کن\n حاصل رو منهای 1 کن\nحالا چشماتو 5 ثانیه ببند \n . \n .\n .همه جا تاریک شد. درسته؟ \n اینو خودم درس کردم\n ما اینیم دیگه!'

                self.textBrowser.append('')
                self.textBrowser.append('-----------------------------------------------------------------------------------------------')
                self.textBrowser.append('')
                self.textBrowser.append((compeyoterjok))
            except:
                self.textBrowser.append('یه مشکلی پیش اومده!!!(شاید جوک هام تموم شده)')


        elif 'خاموش' in input_U or 'شات دان' in input_U or 'شاتدان' in input_U or 'ohl,a' in input_U.lower() or 'ahj nhk' in input_U.lower() or 'ahjnhk' in input_U.lower():
            os.system("shutdown -s -t 11")
            self.textBrowser.append('تا 11 ثانیه دیگه کامپیوتر خاموش میشه !')

        else: 
            self.textBrowser.append(('متوجه نشدم یک بار دیگه دستورت رو بنویس (احتمالا کاری رو که می خوای من بلد نیستم\U0001F614)'))


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


