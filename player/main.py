import sys
import os
import random
import pygame as pg
from PyQt5 import QtWidgets, QtCore
from ui import Ui_MainWindow

class AppBase(QtWidgets.QMainWindow):
    music_pos = 0
    isPaused: bool = False
    isPlaying: bool = False

    def __init__(self):
        super(AppBase, self).__init__()
        pg.init()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.folderBtn.clicked.connect(self.openFolder)
        self.ui.nextBtn.clicked.connect(self.next)
        self.ui.prevBtn.clicked.connect(self.previous)
        self.ui.playBtn.clicked.connect(self.play)
        self.ui.stopBtn.clicked.connect(self.stop)
        self.ui.progressSlider.sliderReleased.connect(self.slider_moved)
        self.ui.shuffleBtn.clicked.connect(self.shuffle)

        self.curr_time = QtCore.QTime(00,00,00)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timer_timeout)

    def openFolder(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory()
        self.track_queue = list()
        files = os.listdir(self.directory)
        if len(files) > 0:
            self.ui.trackList.clear()
            AppBase.isPlaying = True
        else:
            AppBase.isPlaying = False
        for file in files:
            if file.endswith(".mp3"):
                self.ui.trackList.addItem(file)
                self.track_queue.append(file)
        self.ui.trackList.setCurrentItem(self.ui.trackList.item(0))
        self.track_length = round(pg.mixer.Sound(self.directory + '/' + self.ui.trackList.currentItem().text()).get_length())
        self.change_description()

    def play(self):
        #print("PLAY ATTEMPTED\n")
        if AppBase.isPlaying:
            AppBase.music_pos = 0
            #print(self.ui.trackList.currentItem().text())
            self.track_length = round(pg.mixer.Sound(self.directory + '/' + self.ui.trackList.currentItem().text()).get_length())
            pg.mixer_music.load(self.directory + '/' + self.ui.trackList.currentItem().text())
            pg.mixer_music.play()
            self.timer.start(1000)
            self.ui.pauseBtn.setText("Pause")

    def pause(self):
        #print("PAUSE/UNPAUSE ATTEMPTED\n")
        if AppBase.isPlaying:
            if AppBase.isPaused:
                pg.mixer_music.unpause()
                self.ui.pauseBtn.setText("Pause")
            else:
                pg.mixer_music.pause()
                self.ui.pauseBtn.setText("Unpause")

    def stop(self):
        #print("STOP ATTEMPTED\n")
        if AppBase.isPlaying:
            pg.mixer_music.fadeout(500)
            self.timer.stop()
            AppBase.music_pos = 0

    def next(self):
        #print("NEXT ATTEMPTED\n")
        if AppBase.isPlaying:
            if self.ui.trackList.currentRow() == len(self.track_queue) - 1:
                self.ui.trackList.setCurrentRow(0)
            else:
                self.ui.trackList.setCurrentRow(self.ui.trackList.currentRow() + 1)
            self.play()
            AppBase.music_pos = 0

    def previous(self):
        if AppBase.isPlaying:
            if self.ui.trackList.currentRow() == 0:
                self.ui.trackList.setCurrentRow(len(self.track_queue) - 1)
            else:
                self.ui.trackList.setCurrentRow(self.ui.trackList.currentRow() - 1)
            self.play()
            AppBase.music_pos = 0

    def shuffle(self):
        if AppBase.isPlaying:
            random.shuffle(self.track_queue)
            self.stop()
            self.ui.trackList.clear()
            for file in self.track_queue:
                self.ui.trackList.addItem(file)
            self.ui.trackList.setCurrentItem(self.ui.trackList.item(0))
            self.change_description()
            self.play()

    def timer_timeout(self):
        AppBase.music_pos += 1000
        self.change_description()
        self.update_progress()

    def slider_moved(self):
        if AppBase.isPlaying:
            value = self.ui.progressSlider.value() * self.track_length * 10
            AppBase.music_pos = value
            pg.mixer_music.rewind()
            pg.mixer_music.set_pos(value // 1000)

    def change_description(self):
        cur_mins = str(round(AppBase.music_pos / 1000) // 60)
        cur_secs = str(round(AppBase.music_pos / 1000) % 60)
        max_mins = str(self.track_length // 60)
        max_secs = str(self.track_length % 60)
        if len(cur_secs) == 1:
            cur_secs = '0' + cur_secs
        if len(max_secs) == 1:
            max_secs = '0' + max_secs
        self.ui.progressLabel.setText(cur_mins + ':' + cur_secs + '/' + max_mins + ':' + max_secs)

    def update_progress(self):
        #print("progress updated\n")
        if AppBase.music_pos / 1000 > self.track_length:
            self.next()
        percent = int((AppBase.music_pos * 100) / (self.track_length * 1000))
        if not self.ui.progressSlider.isSliderDown():
            self.ui.progressSlider.setValue(percent)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppBase()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()