# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(990, 778)
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 121, 145, 255), stop:1 rgba(120, 255, 214, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.window_title = QLabel(self.centralwidget)
        self.window_title.setObjectName(u"window_title")
        self.window_title.setMinimumSize(QSize(500, 30))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(18)
        self.window_title.setFont(font1)
        self.window_title.setStyleSheet(u"background: none;")
        self.window_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.window_title)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.method_title = QLabel(self.centralwidget)
        self.method_title.setObjectName(u"method_title")
        self.method_title.setMinimumSize(QSize(180, 80))
        self.method_title.setMaximumSize(QSize(180, 80))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(16)
        self.method_title.setFont(font2)
        self.method_title.setStyleSheet(u"background: none;")
        self.method_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.method_title)

        self.radio_euler = QRadioButton(self.centralwidget)
        self.radio_euler.setObjectName(u"radio_euler")
        self.radio_euler.setMinimumSize(QSize(200, 30))
        self.radio_euler.setMaximumSize(QSize(200, 30))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans SC"])
        font3.setPointSize(14)
        self.radio_euler.setFont(font3)
        self.radio_euler.setStyleSheet(u"background: none;")
        self.radio_euler.setChecked(True)

        self.verticalLayout_2.addWidget(self.radio_euler)

        self.radio_runge_kutta = QRadioButton(self.centralwidget)
        self.radio_runge_kutta.setObjectName(u"radio_runge_kutta")
        self.radio_runge_kutta.setMinimumSize(QSize(200, 30))
        self.radio_runge_kutta.setMaximumSize(QSize(200, 30))
        self.radio_runge_kutta.setFont(font3)
        self.radio_runge_kutta.setStyleSheet(u"background: none;")

        self.verticalLayout_2.addWidget(self.radio_runge_kutta)

        self.radio_together = QRadioButton(self.centralwidget)
        self.radio_together.setObjectName(u"radio_together")
        self.radio_together.setFont(font3)
        self.radio_together.setStyleSheet(u"background: none;")

        self.verticalLayout_2.addWidget(self.radio_together)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.limits_title = QLabel(self.centralwidget)
        self.limits_title.setObjectName(u"limits_title")
        self.limits_title.setMinimumSize(QSize(240, 80))
        self.limits_title.setMaximumSize(QSize(240, 80))
        self.limits_title.setFont(font2)
        self.limits_title.setStyleSheet(u"background: none;")
        self.limits_title.setScaledContents(False)
        self.limits_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.limits_title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.limit_x1 = QLabel(self.centralwidget)
        self.limit_x1.setObjectName(u"limit_x1")
        self.limit_x1.setMinimumSize(QSize(30, 20))
        self.limit_x1.setMaximumSize(QSize(30, 20))
        self.limit_x1.setFont(font3)
        self.limit_x1.setStyleSheet(u"background: none;")
        self.limit_x1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.limit_x1)

        self.X0SpinBox = QDoubleSpinBox(self.centralwidget)
        self.X0SpinBox.setObjectName(u"X0SpinBox")
        self.X0SpinBox.setMinimumSize(QSize(60, 0))
        self.X0SpinBox.setMaximumSize(QSize(60, 16777215))
        self.X0SpinBox.setStyleSheet(u"background: #F9F9F9;")
        self.X0SpinBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.X0SpinBox.setDecimals(1)
        self.X0SpinBox.setMinimum(-100.000000000000000)
        self.X0SpinBox.setSingleStep(0.100000000000000)
        self.X0SpinBox.setValue(1.000000000000000)

        self.horizontalLayout.addWidget(self.X0SpinBox)

        self.horizontalSpacer_7 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.limit_x2 = QLabel(self.centralwidget)
        self.limit_x2.setObjectName(u"limit_x2")
        self.limit_x2.setMinimumSize(QSize(30, 20))
        self.limit_x2.setMaximumSize(QSize(30, 20))
        self.limit_x2.setFont(font3)
        self.limit_x2.setStyleSheet(u"background: none;\n"
"margin: 0px;")
        self.limit_x2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.limit_x2)

        self.Y0SpinBox = QDoubleSpinBox(self.centralwidget)
        self.Y0SpinBox.setObjectName(u"Y0SpinBox")
        self.Y0SpinBox.setMinimumSize(QSize(60, 0))
        self.Y0SpinBox.setMaximumSize(QSize(60, 16777215))
        self.Y0SpinBox.setStyleSheet(u"background: #F9F9F9;\n"
"margin: 0px;")
        self.Y0SpinBox.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.Y0SpinBox.setDecimals(1)
        self.Y0SpinBox.setMinimum(-100.000000000000000)
        self.Y0SpinBox.setSingleStep(0.100000000000000)
        self.Y0SpinBox.setValue(1.000000000000000)

        self.horizontalLayout_2.addWidget(self.Y0SpinBox)

        self.horizontalSpacer_6 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 20))
        self.label.setMaximumSize(QSize(30, 20))
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background: none;\n"
"margin: 0px;")

        self.horizontalLayout_7.addWidget(self.label)

        self.XnspinBox = QSpinBox(self.centralwidget)
        self.XnspinBox.setObjectName(u"XnspinBox")
        self.XnspinBox.setMinimumSize(QSize(60, 0))
        self.XnspinBox.setMaximumSize(QSize(60, 16777215))
        self.XnspinBox.setStyleSheet(u"background: #F9F9F9;\n"
"margin: 0px;")
        self.XnspinBox.setValue(5)

        self.horizontalLayout_7.addWidget(self.XnspinBox)

        self.horizontalSpacer_8 = QSpacerItem(110, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.accuracy_label = QLabel(self.centralwidget)
        self.accuracy_label.setObjectName(u"accuracy_label")
        self.accuracy_label.setMinimumSize(QSize(90, 20))
        self.accuracy_label.setMaximumSize(QSize(90, 20))
        self.accuracy_label.setFont(font2)
        self.accuracy_label.setStyleSheet(u"background: none;\n"
"margin: 0px;")

        self.horizontalLayout_6.addWidget(self.accuracy_label)

        self.AccuracySpinBox = QDoubleSpinBox(self.centralwidget)
        self.AccuracySpinBox.setObjectName(u"AccuracySpinBox")
        self.AccuracySpinBox.setMinimumSize(QSize(60, 0))
        self.AccuracySpinBox.setMaximumSize(QSize(60, 16777215))
        self.AccuracySpinBox.setStyleSheet(u"background: #F9F9F9;\n"
"margin: 0px;")
        self.AccuracySpinBox.setMaximum(1.000000000000000)
        self.AccuracySpinBox.setSingleStep(0.010000000000000)
        self.AccuracySpinBox.setValue(0.100000000000000)

        self.horizontalLayout_6.addWidget(self.AccuracySpinBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.function_label = QLabel(self.centralwidget)
        self.function_label.setObjectName(u"function_label")
        self.function_label.setMinimumSize(QSize(200, 50))
        self.function_label.setMaximumSize(QSize(200, 50))
        self.function_label.setFont(font2)
        self.function_label.setStyleSheet(u"background: none;")
        self.function_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.function_label)

        self.function_input = QLineEdit(self.centralwidget)
        self.function_input.setObjectName(u"function_input")
        self.function_input.setMinimumSize(QSize(500, 30))
        self.function_input.setMaximumSize(QSize(500, 30))
        self.function_input.setFont(font3)
        self.function_input.setStyleSheet(u"background: #F9F9F9;")
        self.function_input.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.function_input)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.img_place = QLabel(self.centralwidget)
        self.img_place.setObjectName(u"img_place")
        self.img_place.setMinimumSize(QSize(600, 450))
        self.img_place.setMaximumSize(QSize(600, 450))
        self.img_place.setStyleSheet(u"background: #F9F9F9;")
        self.img_place.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.img_place)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, -1)
        self.calc_btn = QPushButton(self.centralwidget)
        self.calc_btn.setObjectName(u"calc_btn")
        self.calc_btn.setMinimumSize(QSize(250, 50))
        self.calc_btn.setMaximumSize(QSize(250, 50))
        self.calc_btn.setStyleSheet(u"QPushButton{\n"
"background: #F9F9F9;\n"
"border-radius: 20px;\n"
"\n"
"font-family: 'Noto Sans SC';\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #95BFFF;     \n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: #DFECFF;\n"
"}")

        self.horizontalLayout_5.addWidget(self.calc_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_title.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0438\u0441\u0435\u043b\u044c\u043d\u0435 \u0440\u043e\u0437\u0432'\u044f\u0437\u0443\u0432\u0430\u043d\u043d\u044f \u0437\u0432\u0438\u0447\u0430\u0439\u043d\u0438\u0445 \u0434\u0438\u0444\u0435\u0440\u0435\u043d\u0446\u0456\u0430\u043b\u044c\u043d\u0438\u0445 \u0440\u0456\u0432\u043d\u044f\u043d\u044c", None))
        self.method_title.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u043f\u043e\u0448\u0443\u043a\u0443\n"
"\u043a\u043e\u0440\u0435\u043d\u044f", None))
        self.radio_euler.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0415\u0439\u043b\u0435\u0440\u0430", None))
        self.radio_runge_kutta.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0442\u043e\u0434 \u0420\u0443\u043d\u0433\u0435-\u041a\u0443\u0442\u0442\u0430", None))
        self.radio_together.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431'\u0454\u0434\u043d\u0430\u043d\u043d\u044f \u043c\u0435\u0442\u043e\u0434\u0456\u0432", None))
        self.limits_title.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u043d\u044f\n"
"\u043f\u043e\u0447\u0430\u0442\u043a\u043e\u0432\u0438\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u044c", None))
        self.limit_x1.setText(QCoreApplication.translate("MainWindow", u"\u04250:", None))
        self.limit_x2.setText(QCoreApplication.translate("MainWindow", u"Y0:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Xn:", None))
        self.accuracy_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u0456\u0441\u0442\u044c:", None))
        self.function_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0435\u043d\u043d\u044f \u0444\u0443\u043d\u043a\u0446\u0456\u0457", None))
        self.function_input.setText(QCoreApplication.translate("MainWindow", u"(y**2-y)/x", None))
        self.img_place.setText("")
        self.calc_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0437\u0440\u0430\u0445\u0443\u0432\u0430\u0442\u0438", None))
    # retranslateUi

