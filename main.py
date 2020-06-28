import sys, os
import frame
from PyQt5 import QtCore, QtGui, QtWidgets
import PyWinMouse as mouse
from system_hotkey import SystemHotkey

cap_size = 64
cap_zoom = 4

def cap_screen():
    pos = ui.mouse.get_mouse_pos()
    if ui.cur_pos != pos:
        #print(pos)
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

def cap_color():
    #print(ui.xcolor.text())

    ui.color_list.insertRow(0)
    send.run(ui.xcolor.text())

    #ui.color_list.setItem(0, 1, QtWidgets.QTableWidgetItem())
    #ui.color_list.setItem(0, 0, QtWidgets.QTableWidgetItem())
    
    # ui.color_list.item(0,1).setText(ui.xcolor.text())
    # back_color = QtGui.QColor()
    # back_color.setNamedColor(ui.xcolor.text())
    # brush = QtGui.QBrush(back_color)
    # brush.setStyle(QtCore.Qt.SolidPattern)
    # ui.color_list.item(0,0).setBackground(brush)
    # ui.color_list.item(0,0).setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

#https://github.com/timeyyy/system_hotkey
#sig_hotkey = QtCore.pyqtSignal(str)
#sig_hotkey.connect(cap_Color)
sig_cap_color = SystemHotkey()
sig_cap_color.register(("alt","s"), callback=lambda x: cap_color())

#class receive send signal
class x_signal(QtCore.QObject):
    send_sig = QtCore.pyqtSignal(object)
    def run(self,value):
        self.send_sig.emit(value)

#class response to signal
class x_Ui_Dialog(frame.Ui_Dialog):
    def x_setitem(self,value):
        self.color_list.setItem(0,0,QtWidgets.QTableWidgetItem())
        self.color_list.setItem(0,1,QtWidgets.QTableWidgetItem(value))
        back_color = QtGui.QColor()
        back_color.setNamedColor(value)
        brush = QtGui.QBrush(back_color)
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.color_list.item(0,0).setBackground(brush)
        self.color_list.item(0,0).setFlags(QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.color_list.setFocus()
        self.color_list.setCurrentCell(0,1)
    def clear_list(self):
        self.color_list.clear()
        self.color_list.setRowCount(0)
    def copy_list(self):
        clipboard = QtGui.QGuiApplication.clipboard()
        if(self.color_list.rowCount() == 0):
            cap_color()
        list_text = ""
        for item in self.color_list.selectedItems():
            list_text = list_text + item.text() + "\n"
        if(len(list_text) < 9):
            clipboard.setText(list_text[:-1])
        else:
            clipboard.setText(list_text)
        self.color_list.setFocus()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    #ui = frame.Ui_Dialog()
    ui=x_Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #send_sig and slot
    send = x_signal()
    send.send_sig.connect(ui.x_setitem)

    ui.btn_clear.clicked.connect(ui.clear_list)
    ui.btn_copy.clicked.connect(ui.copy_list)

    screen = QtWidgets.QApplication.primaryScreen()
    #window, something error now
    #hwnd = win32gui.FindWindow(None,"Zotero")
    #img = screen.grabWindow(hwnd).toImage()
    ui.img_preview.setGeometry(QtCore.QRect(10, 10, 256, 256))
    ui.xcolor.setGeometry(QtCore.QRect(10, 276, 90, 30))
    ui.btn_clear.setGeometry(QtCore.QRect(274, 276, 90, 30))
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
