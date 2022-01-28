from PyQt5 import QtCore, QtGui, QtWidgets,QtMultimedia
import ntpath
import YTSongDownload
from DownloadUI import Ui_Dialog
import os
import sqlite3
from mutagen.id3 import ID3
from PIL import  Image,ImageDraw
import numpy as np

class Ui_MainWindow(object):
    playing = False
    paused = False
    stopped = False

    guestLogin = False
    userid = "Guest"

    def check(self):
        if(self.guestLogin==True):
            self.addToFavoritesButton.setDisabled(True)
            self.downloadSongsMenu.setDisabled(True)
            self.sortSongsMenu.setDisabled(True)
            self.createPlaylistMenu.setDisabled(True)
            self.importPlaylist.setDisabled(True)
            self.loadFav.setDisabled(True)
            self.profile.setDisabled(True)
            self.profilePicLabel.setPixmap(QtGui.QPixmap("images/default profile.png"))

        else:
                if(os.path.exists("Users/"+self.userid+"/ProfilePic.png")):
                    self.profilePicLabel.setPixmap(QtGui.QPixmap("Users/"+self.userid+"/ProfilePic.png"))

                else:
                    self.profilePicLabel.setPixmap(QtGui.QPixmap("images/default profile.png"))
                
    def initial(self):
        songs = os.listdir("Songs/")
        self.songsList.addItems(songs)

        for i in songs:
            self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile("Songs/"+i)))

    def setupUi(self, MainWindow):
        self.Window=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 991)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n""")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setWindowIcon(QtGui.QIcon("images/icon.ico"))
        MainWindow.setFixedSize(1122,991)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.songImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.songImageLabel.setGeometry(QtCore.QRect(130, 250, 350, 350))
        self.songImageLabel.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.songImageLabel.setText("")
        self.songImageLabel.setObjectName("songImageLabel")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setEnabled(True)
        self.playButton.setGeometry(QtCore.QRect(140, 780, 101, 40))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(12)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.playButton.setAutoDefault(False)
        self.playButton.setDefault(False)
        self.playButton.setFlat(False)
        self.playButton.setObjectName("playButton")

        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(340, 780, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(12)
        self.pauseButton.setFont(font)
        self.pauseButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pauseButton.setObjectName("pauseButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(540, 780, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(12)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.nextButton.setObjectName("nextButton")
        self.previousButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(740, 780, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(12)
        self.previousButton.setFont(font)
        self.previousButton.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.previousButton.setObjectName("previousButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(940, 780, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(12)
        self.stopButton.setFont(font)
        self.stopButton.setStyleSheet("background-color: rgb(255, 51, 24);")
        self.stopButton.setObjectName("stopButton")
        self.songProgressBar = QtWidgets.QSlider(self.centralwidget)
        self.songProgressBar.setGeometry(QtCore.QRect(190, 700, 700, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songProgressBar.sizePolicy().hasHeightForWidth())
        self.songProgressBar.setSizePolicy(sizePolicy)
        self.songProgressBar.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.songProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.songProgressBar.setObjectName("songProgressBar")
        self.volumeDial = QtWidgets.QDial(self.centralwidget)
        self.volumeDial.setGeometry(QtCore.QRect(980, 660, 81, 81))
        self.volumeDial.setObjectName("volumeDial")
        self.addToFavoritesButton = QtWidgets.QPushButton(self.centralwidget)
        self.addToFavoritesButton.setGeometry(QtCore.QRect(480, 870, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(12)
        self.addToFavoritesButton.setFont(font)
        self.addToFavoritesButton.setStyleSheet("background-color: rgb(234, 255, 0);\n"
"background-color: rgb(85, 170, 255);")
        self.addToFavoritesButton.setObjectName("addToFavoritesButton")
        self.songsList = QtWidgets.QListWidget(self.centralwidget)
        self.songsList.setGeometry(QtCore.QRect(580, 230, 490, 400))
        self.songsList.setStyleSheet("background-color: rgb(118, 118, 118);\n"
"font: 14pt \"NSimSun\";\n"
"background-color: rgb(153, 153, 153);")
        self.songsList.setObjectName("songsList")
        self.addedLabel = QtWidgets.QLabel(self.centralwidget)
        self.addedLabel.setGeometry(QtCore.QRect(730, 870, 141, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        self.addedLabel.setFont(font)
        self.addedLabel.setStyleSheet("color: rgb(255, 255, 0);")
        self.addedLabel.setText("ADDED !!")
        self.addedLabel.setObjectName("addedLabel")
        self.addedLabel.setHidden(True)
        self.playlistLabel = QtWidgets.QLabel(self.centralwidget)
        self.playlistLabel.setGeometry(QtCore.QRect(760, 185, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(35)
        self.playlistLabel.setFont(font)
        self.playlistLabel.setStyleSheet("color:rgb(151, 6, 255);")
        self.playlistLabel.setText("PLAYLIST")
        self.playlistLabel.setObjectName("plalistLabel")
        self.iconLabel = QtWidgets.QLabel(self.centralwidget)
        self.iconLabel.setGeometry(QtCore.QRect(190, 10, 240, 220))
        self.iconLabel.setText("")
        self.iconLabel.setPixmap(QtGui.QPixmap("images/logo3.jpeg"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setObjectName("iconLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1122, 21))
        self.menuBar.setStyleSheet("background-color: rgb(231, 231, 231);")
        self.menuBar.setObjectName("menuBar")
        self.songsMenu = QtWidgets.QMenu(self.menuBar)
        self.songsMenu.setObjectName("songsMenu")
        self.createPlaylistMenu = QtWidgets.QMenu(self.songsMenu)
        self.createPlaylistMenu.setObjectName("createPlaylistMenu")
        self.removeSong = QtWidgets.QAction(MainWindow)
        self.removeSong.setObjectName("removeSong")
        self.removeSong.setText("Remove Song")
        self.profile = QtWidgets.QMenu(self.menuBar)
        self.profile.setObjectName("profile")
        self.downloadSongsMenu = QtWidgets.QMenu(self.menuBar)
        self.downloadSongsMenu.setObjectName("downloadSongsMenu")
        self.sortSongsMenu = QtWidgets.QMenu(self.menuBar)
        self.sortSongsMenu.setObjectName("sortSongsMenu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.statusBar.setFont(font)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.statusBar.setObjectName("statusBar")
       # self.statusBar.showMessage("Welcome "+self.userid+" !!")
        MainWindow.setStatusBar(self.statusBar)
        self.profilePic = QtWidgets.QAction(MainWindow)
        self.profilePic.setObjectName("profilePic")
        self.youtubeDownload = QtWidgets.QAction(MainWindow)
        self.youtubeDownload.setObjectName("youtubeDownload")
        self.sortActors = QtWidgets.QAction(MainWindow)
        self.sortActors.setObjectName("sortActors")
        self.loadFav = QtWidgets.QAction(MainWindow)
        self.loadFav.setObjectName("loadFavorites")
        self.sortMood = QtWidgets.QAction(MainWindow)
        self.sortMood.setObjectName("sortMood")
        self.addSongs = QtWidgets.QAction(MainWindow)
        self.addSongs.setObjectName("addSongs")
        self.currentSongsSelect = QtWidgets.QAction(MainWindow)
        self.currentSongsSelect.setObjectName("currentSongsSelect")
        self.newSongsSelect = QtWidgets.QAction(MainWindow)
        self.newSongsSelect.setObjectName("newSongsSelect")
        self.importPlaylist = QtWidgets.QAction(MainWindow)
        self.importPlaylist.setObjectName("importPlaylist")
        self.clearPlaylist = QtWidgets.QAction(MainWindow)
        self.clearPlaylist.setObjectName("clearPlaylist")
        self.createPlaylistMenu.addAction(self.currentSongsSelect)
        self.createPlaylistMenu.addAction(self.newSongsSelect)
        self.songsMenu.addAction(self.addSongs)
        self.songsMenu.addAction(self.createPlaylistMenu.menuAction())
        self.songsMenu.addAction(self.importPlaylist)
        self.songsMenu.addAction(self.loadFav)
        self.songsMenu.addAction(self.clearPlaylist)
        self.downloadSongsMenu.addAction(self.youtubeDownload)
        self.sortSongsMenu.addAction(self.sortActors)
        self.sortSongsMenu.addAction(self.sortMood)
        self.profile.addAction(self.profilePic)
        self.menuBar.addAction(self.songsMenu.menuAction())
        self.menuBar.addAction(self.removeSong)
        self.menuBar.addAction(self.downloadSongsMenu.menuAction())
        self.menuBar.addAction(self.sortSongsMenu.menuAction())
        self.menuBar.addAction(self.profile.menuAction())

        self.playTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.playTimeLabel.setGeometry(QtCore.QRect(120, 700, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.playTimeLabel.setFont(font)
        self.playTimeLabel.setStyleSheet("color: rgb(255, 222, 57);")
        self.playTimeLabel.setText("0:00")
        self.playTimeLabel.setObjectName("playTimeLabel")

        self.songDurationLabel = QtWidgets.QLabel(self.centralwidget)
        self.songDurationLabel.setGeometry(QtCore.QRect(910, 700, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.songDurationLabel.setFont(font)
        self.songDurationLabel.setStyleSheet("color: rgb(255, 222, 57);")
        self.songDurationLabel.setText("0:00")
        self.songDurationLabel.setObjectName("songDurationLabel")

        self.player = QtMultimedia.QMediaPlayer()
        self.playlist = QtMultimedia.QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        self.profilePicLabel= QtWidgets.QLabel(self.centralwidget)
        self.profilePicLabel.setGeometry(QtCore.QRect(620,20,145,145))
        self.profilePicLabel.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:70px;")
        self.profilePicLabel.setObjectName("profilePicLabel")

        self.greetingLabel = QtWidgets.QLabel(self.centralwidget)
        self.greetingLabel.setGeometry(QtCore.QRect(800,60,261,50))
        self.greetingLabel.setStyleSheet("color:rgb(2, 222, 255);font: 18pt 'Eras Demi ITC';")
        self.greetingLabel.setObjectName("greetingLabel")
        self.greetingLabel.setText("Welcome Back "+self.userid+" !!")

        self.check()
        self.initial()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PYMusic"))

        self.playButton.setText(_translate("MainWindow", "PLAY"))
        self.pauseButton.setText(_translate("MainWindow", "PAUSE"))
        self.nextButton.setText(_translate("MainWindow", "NEXT"))
        self.previousButton.setText(_translate("MainWindow", "PREVIOUS"))
        self.stopButton.setText(_translate("MainWindow", "STOP"))
        self.addToFavoritesButton.setText(_translate("MainWindow", "ADD TO FAVORITES"))
        self.songsMenu.setTitle(_translate("MainWindow", "Songs"))
        self.createPlaylistMenu.setTitle(_translate("MainWindow", "Create PlayList"))
        self.downloadSongsMenu.setTitle(_translate("MainWindow", "Download Songs"))
        self.profile.setTitle(_translate("MainWindow","Profile"))
        self.profilePic.setText(_translate("MainWindow", "Change Profile Picture"))
        self.sortSongsMenu.setTitle(_translate("MainWindow", "Sort Songs"))
        self.youtubeDownload.setText(_translate("MainWindow", "Youtube"))
        self.sortActors.setText(_translate("MainWindow", "Actors"))
        self.sortMood.setText(_translate("MainWindow", "Mood"))
        self.addSongs.setText(_translate("MainWindow", "Add Songs"))
        self.currentSongsSelect.setText(_translate("MainWindow", "Current Songs"))
        self.newSongsSelect.setText(_translate("MainWindow", "Select Songs"))
        self.importPlaylist.setText(_translate("MainWindow", "Import PlayList"))
        self.clearPlaylist.setText(_translate("MainWindow", "Clear PlayList"))
        self.loadFav.setText(_translate("MainWindow","Load Favorites"))


    def showDetails(self,song):
        with open('images/temp.jpg', 'wb') as img:
            imgPath='images/temp.jpg'
            size=(350,350)
            a = ID3(song)
            img.write(a.getall('APIC')[0].data)
            self.resizeImage(imgPath,size)
            self.songImageLabel.setPixmap(QtGui.QPixmap("temp.jpg"))

    def resizeImage(self,path,size):
        image = Image.open(path)
        image = image.resize(size, Image.ANTIALIAS)
        image.save("temp.jpg")

    def insertSongs(self):
        songsPath = QtWidgets.QFileDialog.getOpenFileNames(QtWidgets.QMainWindow(),"Select Songs","Songs\\","MP3 Files(*mp3)")
        print(songsPath)
        if (songsPath):
            for _ in songsPath[0]:
                self.songsList.addItem(ntpath.basename(_))
                self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(_)))


    def playSong(self):
        if (self.playlist.isEmpty()): pass

        else:
            if(self.songsList.currentRow()==-1): pass

            else:

                try:
                    if(self.paused==False):
                        self.player.setVolume(50)
                        self.volumeDial.setValue(50)

                    self.playlist.setCurrentIndex(self.songsList.currentRow())
                    self.player.play()

                    self.showDetails(self.playlist.currentMedia().canonicalUrl().toLocalFile())

                    print(self.songsList.currentRow(),"  ",self.playlist.currentIndex())
                    self.statusBar.showMessage("Now Playing :  "+str(self.songsList.currentItem().text()))

                except Exception:
                    print("Error")

    def pauseSong(self):
        self.player.pause()
        self.paused=True

        if((self.player.NoMedia) or self.player.PausedState):
            self.statusBar.showMessage("Music Paused")


    def stopSong(self):
        self.songDurationLabel.setText("0:00")
        self.player.stop()
        self.songDurationLabel.setText("0:00")
        self.songsList.clearSelection()
        self.songsList.setCurrentRow(-1)
        self.volumeDial.setValue(0)
        self.paused=False
        self.stopped=True
        self.statusBar.showMessage("Music Stopped")
        self.songImageLabel.clear()


    def nextSong(self):
        currentSong = self.songsList.currentRow()

        if(currentSong==-1): pass

        else:
            nextSong = currentSong +1

            if(nextSong==self.songsList.count()):
                nextSong=0

            self.songsList.clearSelection()
            self.songsList.setCurrentRow(nextSong)
            self.paused=False
            self.playSong()

    def previousSong(self):
        currentSong = self.songsList.currentRow()

        if (currentSong == -1):
            pass

        else:
            previousSong = currentSong - 1

            if (previousSong == -1):
                previousSong = self.songsList.count()-1

            self.songsList.clearSelection()
            self.songsList.setCurrentRow(previousSong)
            self.paused = False
            self.playSong()

    def addFavorite(self):
        if(self.songsList.currentRow()==-1):pass

        else:

            connection = sqlite3.connect("Users/" + self.userid + "/Favorites.sqlite3")

            cur = connection.cursor()

            cur.execute("create table if not exists Favorites (Songs varchar)")

            media = self.playlist.media(self.songsList.currentRow())
            filename = media.canonicalUrl().toLocalFile()

            cur.execute(' INSERT INTO Favorites (Songs) VALUES (?) ',(filename,))

            connection.commit()
            self.statusBar.showMessage("Added  "+self.songsList.currentItem().text()+" to Favorites !")

    def loadFavorites(self):

        connection = sqlite3.connect("Users/" + self.userid + "/Favorites.sqlite3")

        cur = connection.cursor()

        songsPath = cur.execute( """SELECT name FROM sqlite_master WHERE type='table' AND name='Favorites'; """).fetchall()

        if(songsPath==[]):
            self.statusBar.showMessage("No songs in Favorites")
            return

        self.clear()
        songs=[]
        songsPath=cur.execute("SELECT * FROM Favorites").fetchall()
        for i in songsPath:
            songs.append(i[0])

        for _ in songs:
            self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(_)))
            self.songsList.addItem(ntpath.basename(_))

    def setVolume(self):
        self.player.setVolume(self.volumeDial.value())

    def seekSong(self):
        self.songProgressBar.setFocus()
        if self.player.state() == QtMultimedia.QMediaPlayer.PlayingState or self.player.state() == QtMultimedia.QMediaPlayer.PausedState:
            seek = self.songProgressBar.value()
            self.player.setPosition(seek)

    def formatTime(self,dur):
        hour, r = divmod(dur, 3600000)
        minute, r = divmod(r, 60000)
        second, _ = divmod(r, 1000)
        return ("%d:%02d:%02d" % (hour, minute, second)) if hour else ("%d:%02d" % (minute, second))

    def sliderMove(self, position):
        self.songProgressBar.setValue(position)
        self.playTimeLabel.setText(self.formatTime(position))
        self.songDurationLabel.setText(self.formatTime(self.player.duration()))

    def sliderMax(self, duration):
        self.songProgressBar.setRange(0, duration)

    def downloadUI(self):
        self.ui = Ui_Dialog()
        self.dialog=QtWidgets.QDialog()
        self.ui.setupUi(self.dialog)
        self.dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ui.downloadButton.clicked.connect(self.downloadYTSongs)
        self.dialog.show()

    def downloadYTSongs(self):
        url = self.ui.urlTextField.text()
        #https://www.youtube.com/watch?v=BuW1SqwH_g0  10 sec song
        try:
            YTSongDownload.run(url,self.userid)
            self.ui.downloadedIconLabel.setHidden(False)
            self.ui.downloadSuccessLabel.setHidden(False)
            QtCore.QTimer.singleShot(2000, self.dialog.close)

        except Exception:
            error = QtWidgets.QMessageBox()
            error.setIcon(QtWidgets.QMessageBox.Critical)
            error.setText("URL not found !!")
            error.setWindowTitle("ERROR")
            error.show()
            error.exec_()

    def clear(self):
        self.player.stop()
        self.statusBar.showMessage("Playlist Cleared !")
        self.playlist.clear()
        self.songsList.clear()
        self.songImageLabel.clear()

    def remove(self):

        if(self.songsList.currentRow()== -1):pass

        else:
            self.playlist.removeMedia(self.songsList.currentRow())
            x=self.songsList.takeItem(self.songsList.currentRow())
            self.stopSong()
            self.statusBar.showMessage("Removed:  "+x.text())
            self.songDurationLabel.setText("00:00")

    def createPlaylistCurrent(self):
        totalSongs = self.playlist.mediaCount()
        currSongs=[]

        if (len(currSongs) > 0):
            currSongs.clear()

        if(totalSongs==0): pass

        else:

            playListName,status = QtWidgets.QInputDialog.getText(QtWidgets.QMainWindow(),"Playlist Name", "Enter Playlist Name: ")


            if status:
                connection = sqlite3.connect("Users/"+self.userid+"/Playlists/"+playListName+".sqlite3")

                cursor = connection.cursor()

                cursor.executescript("CREATE TABLE "+playListName+" (Songs varchar);")


                for i in range(totalSongs):
                    media = self.playlist.media(i)
                    filename = media.canonicalUrl().toLocalFile()
                    currSongs.append(filename)

                for i in currSongs:
                    cursor.execute(''' INSERT INTO {} (Songs) VALUES (?) '''.format(playListName), (i,))

                connection.commit()
                self.statusBar.showMessage("Playlist '"+playListName+"' created successfully !")

    def importSongs(self):
        songPlaylist = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QMainWindow(),"Select Playlist","Users/"+self.userid+"/Playlists","Database Files(*.sqlite3)")
        print(songPlaylist)
        if(songPlaylist[0] != ""):
            database = songPlaylist[0]

            databaseName = os.path.split(database)[1]

            tableName = os.path.splitext(databaseName)[0]

            songs=[]
            if (len(songs)>0):
                songs.clear()

            connection = sqlite3.connect(database)
            cursor = connection.cursor()
            cursor.execute(''' SELECT * FROM {} '''.format(tableName))

            playlist = cursor.fetchall()

            for i in playlist:
                songs.append(i[0])

            for _ in songs:
                self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(_)))
                self.songsList.addItem(ntpath.basename(_))

            self.statusBar.showMessage("Playlist Imported !")

    def selectSongs(self):
        currSongs = []

        if (len(currSongs) > 0):
            currSongs.clear()

        songsPath = QtWidgets.QFileDialog.getOpenFileNames(QtWidgets.QMainWindow(), "Select Songs",
                                                       "Songs/",
                                                       "MP3 Files(*mp3)")
        print(songsPath)
        if(songsPath[1] != ""):
            playListName, status = QtWidgets.QInputDialog.getText(QtWidgets.QMainWindow(), "Playlist Name",
                                                              "Enter Playlist Name: ")

            if(status):
                connection = sqlite3.connect("Users/" + self.userid+ "/Playlists/" + playListName + ".sqlite3")

                cursor = connection.cursor()

                cursor.executescript("CREATE TABLE " + playListName + " (Songs varchar);")

                for i in songsPath[0]:
                    cursor.execute(''' INSERT INTO {} (Songs) VALUES (?) '''.format(playListName), (i,))

                connection.commit()
                self.statusBar.showMessage("Playlist '" + playListName + "' created successfully !")

    def actorSongs(self):

        def selected(self):
            self.stopSong()
            self.clear()
            self.Actors.close()
            op = self.actorUi.actorsList.currentIndex()
            path="Actor songs/"

            if(op==0):
                path+="MB/"

            elif(op==1):
                path+="VD/"

            elif(op==2):
                path+="PK/"

            elif(op==3):
                path+="AA/"

            elif(op==4):
                path+="Prabhas/"

            file = os.listdir(path)

            self.songsList.addItems(file)
            for i in file:
                self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(os.path.join(path)+i)))

        from ActorSortUI import Ui_Actors
        self.actorUi = Ui_Actors()
        self.Actors = QtWidgets.QDialog()
        self.actorUi.setupUi(self.Actors)
        self.Actors.setWindowModality(QtCore.Qt.ApplicationModal)
        self.actorUi.submitButton.clicked.connect(lambda  : selected(self))
        self.Actors.show()

    def moodSongs(self):

        def selected(self):
            self.stopSong()
            self.clear()
            self.Moods.close()
            op = self.moodUi.moodBox.currentIndex()
            path="Mood songs/"

            if(op==0):
                path+="Happy/"

            elif(op==1):
                path+="Sorrow/"

            elif(op==2):
                path+="Energetic/"

            elif(op==3):
                path+="Calm/"

            elif(op==4):
                path+="Romantic/"

            file = os.listdir(path)

            self.songsList.addItems(file)
            for i in file:
                self.playlist.addMedia(QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(os.path.join(path)+i)))

        from MoodSortUI import Ui_MoodUI
        self.moodUi = Ui_MoodUI()
        self.Moods = QtWidgets.QDialog()
        self.moodUi.setupUi(self.Moods)
        self.Moods.setWindowModality(QtCore.Qt.ApplicationModal)
        self.moodUi.pushButton.clicked.connect(lambda  : selected(self))
        self.Moods.show()

    def changeProfilePic(self):
        imgPath = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QMainWindow(),"Select Image","","Image Files (*.jpeg) (*.jpg) (*.png)")

        if(imgPath[0]!=("")):

            img = Image.open(imgPath[0]).convert("RGB")
            npImage = np.array(img)
            h, w = img.size

            alpha = Image.new('L', img.size, 0)
            draw = ImageDraw.Draw(alpha)
            draw.pieslice([0, 0, h, w], 0, 360, fill=255)

            npAlpha = np.array(alpha)

            npImage = np.dstack((npImage, npAlpha))

            Image.fromarray(npImage).resize((145, 145), Image.ANTIALIAS).save("Users/"+self.userid+"/ProfilePic.png")

            self.profilePicLabel.setPixmap(QtGui.QPixmap("Users/"+self.userid+"/ProfilePic.png"))

    def events(self):
        self.playButton.clicked.connect(self.playSong)
        self.pauseButton.clicked.connect(self.pauseSong)
        self.stopButton.clicked.connect(self.stopSong)
        self.nextButton.clicked.connect(self.nextSong)
        self.previousButton.clicked.connect(self.previousSong)

        self.addSongs.triggered.connect(self.insertSongs)

        self.songProgressBar.sliderReleased.connect(self.seekSong)
        self.volumeDial.valueChanged.connect(self.setVolume)

        self.youtubeDownload.triggered.connect(self.downloadUI)

        self.clearPlaylist.triggered.connect(self.clear)

        self.removeSong.triggered.connect(self.remove)

        self.player.positionChanged.connect(self.sliderMove)
        self.player.durationChanged.connect(self.sliderMax)

        self.addToFavoritesButton.clicked.connect(self.addFavorite)

        self.currentSongsSelect.triggered.connect(self.createPlaylistCurrent)

        self.importPlaylist.triggered.connect(self.importSongs)

        self.loadFav.triggered.connect(self.loadFavorites)

        self.newSongsSelect.triggered.connect(self.selectSongs)

        self.sortActors.triggered.connect(self.actorSongs)

        self.sortMood.triggered.connect(self.moodSongs)

        self.profilePic.triggered.connect(self.changeProfilePic)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)

    ui.events()

    sys.exit(app.exec_())


