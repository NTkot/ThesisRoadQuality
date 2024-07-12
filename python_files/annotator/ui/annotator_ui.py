# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/annotator_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(936, 1001)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 78, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 65, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 34, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 78, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 65, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 34, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(69, 78, 81))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 65, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(30, 34, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(23, 26, 27))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        main_window.setPalette(palette)
        self.main_widget = QtWidgets.QWidget(main_window)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.annotation_list = QtWidgets.QListWidget(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.annotation_list.sizePolicy().hasHeightForWidth())
        self.annotation_list.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(34, 39, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 39, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.annotation_list.setPalette(palette)
        self.annotation_list.setFrameShape(QtWidgets.QFrame.Box)
        self.annotation_list.setObjectName("annotation_list")
        self.gridLayout.addWidget(self.annotation_list, 1, 3, 6, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.annotation_tab = QtWidgets.QWidget()
        self.annotation_tab.setObjectName("annotation_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.annotation_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.anomaly_dropdown = QtWidgets.QComboBox(self.annotation_tab)
        self.anomaly_dropdown.setObjectName("anomaly_dropdown")
        self.gridLayout_6.addWidget(self.anomaly_dropdown, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.annotation_tab)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)
        self.remove_button = QtWidgets.QPushButton(self.annotation_tab)
        self.remove_button.setObjectName("remove_button")
        self.gridLayout_6.addWidget(self.remove_button, 7, 0, 1, 2)
        self.add_button = QtWidgets.QPushButton(self.annotation_tab)
        self.add_button.setObjectName("add_button")
        self.gridLayout_6.addWidget(self.add_button, 6, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.annotation_tab)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.annotation_tab)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 2, 0, 1, 1)
        self.t_start_box = QtWidgets.QDoubleSpinBox(self.annotation_tab)
        self.t_start_box.setAlignment(QtCore.Qt.AlignCenter)
        self.t_start_box.setDecimals(4)
        self.t_start_box.setObjectName("t_start_box")
        self.gridLayout_6.addWidget(self.t_start_box, 0, 1, 1, 1)
        self.t_end_box = QtWidgets.QDoubleSpinBox(self.annotation_tab)
        self.t_end_box.setAlignment(QtCore.Qt.AlignCenter)
        self.t_end_box.setDecimals(4)
        self.t_end_box.setObjectName("t_end_box")
        self.gridLayout_6.addWidget(self.t_end_box, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.annotation_tab)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.annotation_tab)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 5, 0, 1, 1)
        self.transversity_dropdown = QtWidgets.QComboBox(self.annotation_tab)
        self.transversity_dropdown.setObjectName("transversity_dropdown")
        self.gridLayout_6.addWidget(self.transversity_dropdown, 4, 1, 1, 1)
        self.severity_dropdown = QtWidgets.QComboBox(self.annotation_tab)
        self.severity_dropdown.setObjectName("severity_dropdown")
        self.gridLayout_6.addWidget(self.severity_dropdown, 5, 1, 1, 1)
        self.tabWidget.addTab(self.annotation_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.settings_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.settings_tab)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_11.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_11.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_11.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_11.addWidget(self.label, 1, 0, 1, 1)
        self.imu_topic_dropdown = QtWidgets.QComboBox(self.frame_6)
        self.imu_topic_dropdown.setObjectName("imu_topic_dropdown")
        self.gridLayout_11.addWidget(self.imu_topic_dropdown, 1, 1, 1, 1)
        self.mv_size_box = QtWidgets.QSpinBox(self.frame_6)
        self.mv_size_box.setMinimum(1)
        self.mv_size_box.setMaximum(500)
        self.mv_size_box.setObjectName("mv_size_box")
        self.gridLayout_11.addWidget(self.mv_size_box, 3, 1, 1, 1)
        self.wiener_size_box = QtWidgets.QSpinBox(self.frame_6)
        self.wiener_size_box.setMinimum(1)
        self.wiener_size_box.setMaximum(501)
        self.wiener_size_box.setSingleStep(2)
        self.wiener_size_box.setObjectName("wiener_size_box")
        self.gridLayout_11.addWidget(self.wiener_size_box, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_11.addWidget(self.label_5, 0, 0, 1, 2)
        self.gridLayout_5.addWidget(self.frame_6, 4, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.settings_tab)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_10.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.dump_button = QtWidgets.QPushButton(self.frame_5)
        self.dump_button.setObjectName("dump_button")
        self.gridLayout_10.addWidget(self.dump_button, 1, 0, 1, 1)
        self.load_button = QtWidgets.QPushButton(self.frame_5)
        self.load_button.setObjectName("load_button")
        self.gridLayout_10.addWidget(self.load_button, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 2)
        self.gridLayout_5.addWidget(self.frame_5, 7, 0, 1, 2)
        self.frame_4 = QtWidgets.QFrame(self.settings_tab)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.time_disp_box = QtWidgets.QDoubleSpinBox(self.frame_4)
        self.time_disp_box.setPrefix("")
        self.time_disp_box.setDecimals(1)
        self.time_disp_box.setMinimum(0.1)
        self.time_disp_box.setMaximum(1000.0)
        self.time_disp_box.setProperty("value", 20.0)
        self.time_disp_box.setObjectName("time_disp_box")
        self.gridLayout_7.addWidget(self.time_disp_box, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 2)
        self.gridLayout_5.addWidget(self.frame_4, 5, 0, 1, 2)
        self.frame_9 = QtWidgets.QFrame(self.settings_tab)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_14 = QtWidgets.QLabel(self.frame_9)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_12.addWidget(self.label_14, 1, 0, 1, 1)
        self.prev_t_jump_box = QtWidgets.QDoubleSpinBox(self.frame_9)
        self.prev_t_jump_box.setPrefix("")
        self.prev_t_jump_box.setDecimals(2)
        self.prev_t_jump_box.setMinimum(0.01)
        self.prev_t_jump_box.setMaximum(100.0)
        self.prev_t_jump_box.setSingleStep(0.1)
        self.prev_t_jump_box.setProperty("value", 1.0)
        self.prev_t_jump_box.setObjectName("prev_t_jump_box")
        self.gridLayout_12.addWidget(self.prev_t_jump_box, 1, 1, 1, 1)
        self.next_t_jump_box = QtWidgets.QDoubleSpinBox(self.frame_9)
        self.next_t_jump_box.setPrefix("")
        self.next_t_jump_box.setDecimals(2)
        self.next_t_jump_box.setMinimum(0.01)
        self.next_t_jump_box.setMaximum(100.0)
        self.next_t_jump_box.setSingleStep(0.1)
        self.next_t_jump_box.setProperty("value", 1.0)
        self.next_t_jump_box.setObjectName("next_t_jump_box")
        self.gridLayout_12.addWidget(self.next_t_jump_box, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_9)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_12.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_12.addWidget(self.label_13, 0, 0, 1, 2)
        self.gridLayout_5.addWidget(self.frame_9, 6, 0, 1, 2)
        self.tabWidget.addTab(self.settings_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 2, 1, 2)
        self.frame_7 = QtWidgets.QFrame(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.time_slider = QtWidgets.QSlider(self.frame_7)
        self.time_slider.setOrientation(QtCore.Qt.Horizontal)
        self.time_slider.setInvertedAppearance(False)
        self.time_slider.setObjectName("time_slider")
        self.gridLayout_8.addWidget(self.time_slider, 0, 2, 1, 1)
        self.time_play_button = QtWidgets.QPushButton(self.frame_7)
        self.time_play_button.setText("")
        self.time_play_button.setCheckable(True)
        self.time_play_button.setObjectName("time_play_button")
        self.gridLayout_8.addWidget(self.time_play_button, 0, 0, 1, 1)
        self.time_box = QtWidgets.QDoubleSpinBox(self.frame_7)
        self.time_box.setDecimals(3)
        self.time_box.setObjectName("time_box")
        self.gridLayout_8.addWidget(self.time_box, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.frame_7, 6, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gyr_plot = PlotWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gyr_plot.sizePolicy().hasHeightForWidth())
        self.gyr_plot.setSizePolicy(sizePolicy)
        self.gyr_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.gyr_plot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.gyr_plot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.gyr_plot.setObjectName("gyr_plot")
        self.gridLayout_4.addWidget(self.gyr_plot, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 3, 0, 2, 3)
        self.frame_3 = QtWidgets.QFrame(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.acc_plot = PlotWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acc_plot.sizePolicy().hasHeightForWidth())
        self.acc_plot.setSizePolicy(sizePolicy)
        self.acc_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.acc_plot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.acc_plot.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.acc_plot.setObjectName("acc_plot")
        self.gridLayout_3.addWidget(self.acc_plot, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 2, 3)
        self.frame_8 = QtWidgets.QFrame(self.main_widget)
        self.frame_8.setEnabled(True)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_9.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.ext_button_plot = PlotWidget(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ext_button_plot.sizePolicy().hasHeightForWidth())
        self.ext_button_plot.setSizePolicy(sizePolicy)
        self.ext_button_plot.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ext_button_plot.setObjectName("ext_button_plot")
        self.gridLayout_9.addWidget(self.ext_button_plot, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_8, 5, 0, 1, 3)
        self.camera_view = QtWidgets.QLabel(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_view.sizePolicy().hasHeightForWidth())
        self.camera_view.setSizePolicy(sizePolicy)
        self.camera_view.setFrameShape(QtWidgets.QFrame.Box)
        self.camera_view.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.camera_view.setText("")
        self.camera_view.setAlignment(QtCore.Qt.AlignCenter)
        self.camera_view.setObjectName("camera_view")
        self.gridLayout.addWidget(self.camera_view, 0, 0, 1, 2)
        main_window.setCentralWidget(self.main_widget)
        self.dump_annotations = QtWidgets.QAction(main_window)
        self.dump_annotations.setObjectName("dump_annotations")
        self.load_annotations = QtWidgets.QAction(main_window)
        self.load_annotations.setObjectName("load_annotations")
        self.play_pause = QtWidgets.QAction(main_window)
        self.play_pause.setObjectName("play_pause")
        self.prev_t = QtWidgets.QAction(main_window)
        self.prev_t.setObjectName("prev_t")
        self.next_t = QtWidgets.QAction(main_window)
        self.next_t.setObjectName("next_t")

        self.retranslateUi(main_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Road Quality - Annotator"))
        self.label_7.setText(_translate("main_window", "t_start"))
        self.remove_button.setText(_translate("main_window", "Remove"))
        self.add_button.setText(_translate("main_window", "Add"))
        self.label_8.setText(_translate("main_window", "t_end"))
        self.label_9.setText(_translate("main_window", "Anomaly"))
        self.t_start_box.setSuffix(_translate("main_window", " sec"))
        self.t_end_box.setSuffix(_translate("main_window", " sec"))
        self.label_11.setText(_translate("main_window", "Transversity"))
        self.label_12.setText(_translate("main_window", "Severity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.annotation_tab), _translate("main_window", "Annotation"))
        self.label_3.setText(_translate("main_window", "Moving Average filter size:"))
        self.label_2.setText(_translate("main_window", "Wiener filter size:"))
        self.label.setText(_translate("main_window", "IMU topic used:"))
        self.label_5.setText(_translate("main_window", "Data Settings"))
        self.dump_button.setText(_translate("main_window", "Dump"))
        self.load_button.setText(_translate("main_window", "Load"))
        self.label_10.setText(_translate("main_window", "File settings"))
        self.time_disp_box.setSuffix(_translate("main_window", " sec"))
        self.label_4.setText(_translate("main_window", "Time displayed:"))
        self.label_6.setText(_translate("main_window", "Plot settings"))
        self.label_14.setText(_translate("main_window", "Previous time - Jump interval"))
        self.prev_t_jump_box.setSuffix(_translate("main_window", " sec"))
        self.next_t_jump_box.setSuffix(_translate("main_window", " sec"))
        self.label_15.setText(_translate("main_window", "Next time - Jump interval"))
        self.label_13.setText(_translate("main_window", "Control settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("main_window", "Settings"))
        self.time_box.setSuffix(_translate("main_window", " sec"))
        self.dump_annotations.setText(_translate("main_window", "Dump annotations"))
        self.dump_annotations.setShortcut(_translate("main_window", "Ctrl+S"))
        self.load_annotations.setText(_translate("main_window", "Load Annotations"))
        self.load_annotations.setShortcut(_translate("main_window", "Ctrl+L"))
        self.play_pause.setText(_translate("main_window", "Play/Pause"))
        self.play_pause.setShortcut(_translate("main_window", "Space"))
        self.prev_t.setText(_translate("main_window", "Previous time moment"))
        self.prev_t.setToolTip(_translate("main_window", "Previous time moment"))
        self.prev_t.setShortcut(_translate("main_window", "A"))
        self.next_t.setText(_translate("main_window", "Next time moment"))
        self.next_t.setToolTip(_translate("main_window", "Next time moment"))
        self.next_t.setShortcut(_translate("main_window", "D"))
from pyqtgraph import PlotWidget
