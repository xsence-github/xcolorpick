import sys, os
import frame
from PyQt5 import QtCore, QtGui, QtWidgets
import PyWinMouse as mouse

cap_size = 64
cap_zoom = 4


def cap_screen():
    pos = ui.mouse.get_mouse_pos()
    if ui.cur_pos != pos:
        print(pos)
        if (pos[0] + 1) < cap_size/2:
            grab_x = 0
            pixel_x = pos[0]
        elif (pos[0] + cap_size/2 + 1) > screen.size().width():
            grab_x = screen.size().width() - cap_size - 1
            pixel_x = cap_size - (screen.size().width() - pos[0])
        else:
            grab_x = pos[0] + 1 - cap_size/2
            pixel_x = cap_size/2 - 1
        
        if (pos[1] + 1) < cap_size/2:
            grab_y = 0
            pixel_y = pos[1]
        elif (pos[1] + cap_size/2 + 1) > screen.size().height():
            grab_y = screen.size().height() - cap_size - 1
            pixel_y = cap_size - (screen.size().height() - pos[1])
        else:
            grab_y = pos[1] + 1 - cap_size/2
            pixel_y = cap_size/2 - 1
        img = screen.grabWindow(QtWidgets.QApplication.desktop().winId(),grab_x,grab_y,cap_size,cap_size)
        r = QtGui.qRed(img.toImage().pixel(pixel_x,pixel_y))
        g = QtGui.qGreen(img.toImage().pixel(pixel_x,pixel_y))
        b = QtGui.qBlue(img.toImage().pixel(pixel_x,pixel_y))
        ui.img_preview.setPixmap(img.scaled(cap_zoom*img.width(),cap_zoom*img.height()))
        ui.xcolor.setText(QtGui.QColor(r, g, b).name())
        ui.cur_pos = pos
        ui.line_h.move(11,11 + cap_zoom*pixel_y)
        ui.line_v.move(11 + cap_zoom*pixel_x,11)
        ui.color_preview.move(7 + cap_zoom*pixel_x,7 + cap_zoom*pixel_y)
        ui.line_h.setStyleSheet("color: "+QtGui.QColor(255-r, 255-g, 255-b).name()+";")
        ui.line_v.setStyleSheet("color: "+QtGui.QColor(255-r, 255-g, 255-b).name()+";")

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
    ui.img_preview.setGeometry(QtCore.QRect(10, 10, 256, 256))
    ui.xcolor.setGeometry(QtCore.QRect(10, 276, 90, 30))
    ui.pushButton.setGeometry(QtCore.QRect(295, 276, 90, 40))
    ui.line_h.setGeometry(QtCore.QRect(11, 135, 256, 1))
    ui.line_v.setGeometry(QtCore.QRect(135, 11, 1, 256))
    ui.color_preview.setGeometry(QtCore.QRect(131, 131, 9, 9))
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
