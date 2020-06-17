import sys, os
import frame
from PyQt5 import QtCore, QtGui, QtWidgets
import PyWinMouse as mouse

import win32gui

hwnd_title = dict()
def get_all_hwnd(hwnd,mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})

win32gui.EnumWindows(get_all_hwnd, 0)

for h,t in hwnd_title.items():
    if t is not "":
        print(h,t)

def test():
    m = mouse.Mouse()
    pos = m.get_mouse_pos()
    print(pos)
    img = screen.grabWindow(QtWidgets.QApplication.desktop().winId(),pos[0],pos[1],32,32)
    img.save(os.path.abspath(os.path.dirname(__file__)) + "\shot.jpg")
    ui.label_2.setPixmap(QtGui.QPixmap(os.path.abspath(os.path.dirname(__file__)) + "\shot.jpg"))

def cap_screen():
    pos = ui.mouse.get_mouse_pos()
    if ui.cur_pos != pos:
        print(pos)
        img = screen.grabWindow(QtWidgets.QApplication.desktop().winId(),pos[0],pos[1],128,128)
        r = QtGui.qRed(img.toImage().pixel(0,0))
        g = QtGui.qGreen(img.toImage().pixel(0,0))
        b = QtGui.qBlue(img.toImage().pixel(0,0))
        ui.img_preview.setPixmap(img.scaled(2*img.width(),2*img.height()))
        ui.xcolor.setText(QtGui.QColor(r, g, b).name())
        ui.cur_pos = pos

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = frame.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()

    screen = QtWidgets.QApplication.primaryScreen()
    #window, something error now
    #hwnd = win32gui.FindWindow(None,"Zotero")
    #img = screen.grabWindow(hwnd).toImage()

    #fullscreen
    #img = screen.grabWindow(QtWidgets.QApplication.desktop().winId())
    #img.save(os.path.abspath(os.path.dirname(__file__)) + "\shot.jpg")
    #QScreen.grabWindow(app.primaryScreen(), QApplication.desktop().winId()).save(filename, 'png')

    ui.mouse = mouse.Mouse()
    ui.cur_pos = ui.mouse.get_mouse_pos()
    ui.mouse_listen_timer = QtCore.QTimer(app)
    ui.mouse_listen_timer.timeout.connect(cap_screen)
    ui.mouse_listen_timer.start(100)

    sys.exit(app.exec_())
