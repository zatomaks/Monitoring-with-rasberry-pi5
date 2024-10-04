# -*- coding: utf-8 -*-
###############################################################################
# Form generated from reading UI file 'Main_menu.ui'
#
# Created by: Qt User Interface Compiler version 6.7.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QCursor, QFont
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 420)
        MainWindow.setFixedSize(476, 420)
        # Отключаем кнопку развертывания, оставляя возможность закрытия и сворачивания
        MainWindow.setWindowFlags(
            MainWindow.windowFlags() & ~Qt.WindowMaximizeButtonHint
        )

        MainWindow.setStyleSheet("")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            """
        QWidget{
                background-color: #99FFCC;
                }
        QLineEdit {
        background-color: #f0f4f8;     /* Светло-серый фон для минималистичного стиля */
        color: #333333;                /* Тёмно-серый текст для контраста */
        border: 1px solid #cfd8dc;     /* Тонкая светлая граница */
        border-radius: 8px;            /* Скругленные углы для мягкости */
        padding: 8px 12px;             /* Внутренние отступы для большего пространства */
        font-size: 14px;               /* Удобный для чтения размер шрифта */
        outline: none;                 /* Убираем стандартный фокус-эффект */
        }
        QLineEdit:hover {
        background-color: #e0e7ee;     /* Легкое изменение цвета фона при наведении */
        }
        QLineEdit:focus {
        background-color: #ffffff;     /* Белый фон при фокусировке */
        border: 2px solid #1976d2;     /* Синяя граница при фокусировке */
        }
        QLineEdit::placeholder {
        color: #757575;                /* Серый цвет текста плейсхолдера */
        font-style: italic;            /* Курсив для текста плейсхолдера */
        }
        QLineEdit:disabled {
        background-color: #e0e0e0;     /* Светло-серый фон для неактивного состояния */
        color: #9e9e9e;                /* Бледный текст для отключенного состояния */
        border: 1px solid #bdbdbd;     /* Бледная граница для неактивного состояния */
        }
        QPushButton{
        background-color: #f0f4f8;     /* Светло-серый фон для современного стиля */
        color: #333333;                /* Тёмно-серый цвет текста */
        border: 1px solid #cfd8dc;     /* Тонкая светлая граница */
        border-radius: 8px;            /* Скругленные углы */
        padding: 8px 12px;             /* Внутренние отступы для аккуратности */
        font-size: 14px;               /* Удобный размер шрифта */
        font-weight: bold;             /* Жирный текст для акцента */
        text-align: center;            /* Центрирование текста */
        font-family: 'Roboto', sans-serif; 
        }
        QPushButton:hover {
        background-color: #e0e7ee;     /* Легкое изменение цвета фона при наведении */
        color: #1976d2;                /* Изменение цвета текста при наведении */
        }
        QPushButton:disabled {
        background-color: #e0e0e0;     /* Серый фон для отключенного состояния */
        color: #9e9e9e;                /* Бледный текст для неактивного состояния */
        border: 1px solid #bdbdbd;     /* Бледная граница для отключенного состояния */
        }
        QPushButton:focus {
        border: 2px solid #ffffff;     /* Синяя граница при фокусировке (если используется) */
        background-color: #81C784;     /* Белый фон при фокусировке #ffffff  */
        }
        QLabel {
        background-color: #f0f4f8;     /* Светло-серый фон для современного стиля */
        color: #333333;                /* Тёмно-серый цвет текста */
        border: 1px solid #cfd8dc;     /* Тонкая светлая граница */
        border-radius: 8px;            /* Скругленные углы */
        padding: 8px 12px;             /* Внутренние отступы для аккуратности */
        font-size: 14px;               /* Удобный размер шрифта */
        font-weight: bold;             /* Жирный текст для акцента */
        text-align: center;            /* Центрирование текста */
        font-family: 'Roboto', sans-serif; 
        }
        QLabel:hover {
        background-color: #e0e7ee;     /* Легкое изменение цвета фона при наведении */
        color: #1976d2;                /* Изменение цвета текста при наведении */
        }
        QLabel:disabled {
        background-color: #e0e0e0;     /* Серый фон для отключенного состояния */
        color: #9e9e9e;                /* Бледный текст для неактивного состояния */
        border: 1px solid #bdbdbd;     /* Бледная граница для отключенного состояния */
        }
        QLabel:focus {
        border: 2px solid #1976d2;     /* Синяя граница при фокусировке (если используется) */
        background-color: #ffffff;     /* Белый фон при фокусировке */
        }
        QSpinBox {
        background-color: #f0f4f8;     /* Светло-серый фон для современного минимализма */
        color: #333333;                /* Тёмно-серый цвет текста для хорошего контраста */
        border: 1px solid #cfd8dc;     /* Тонкая светло-серая граница */
        border-radius: 8px;            /* Скруглённые углы */
        padding: 5px 10px;             /* Увеличенные внутренние отступы */
        font-size: 14px;               /* Чёткий размер шрифта */
        }
        QSpinBox::up-button, QSpinBox::down-button {
        background-color: #e0e0e0;     /* Светло-серый фон для кнопок */
        border: none;                  /* Убираем стандартную границу */
        width: 16px;                   /* Фиксированная ширина кнопок */
        margin: 1px;                   /* Минимальный отступ между кнопками и полем */
        }
        QSpinBox::up-button {
        border-top-right-radius: 8px;  /* Скругление для верхней кнопки */
        }
        QSpinBox::down-button {
        border-bottom-right-radius: 8px; /* Скругление для нижней кнопки */
        }
        QSpinBox::up-button:hover, QSpinBox::down-button:hover {
        background-color: #b0bec5;      /* Темнее на кнопках при наведении */
        }
        QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {
        background-color: #90a4ae;      /* Цвет при нажатии */
        }
        QSpinBox::up-arrow, QSpinBox::down-arrow {
        width: 10px;                    /* Размер стрелок */
        height: 10px;
        color: #607d8b;                 /* Тёмно-серый цвет стрелок */
        }
        QSpinBox:focus {
        border: 2px solid #1976d2;      /* Синяя граница при фокусе */
        background-color: #ffffff;      /* Белый фон при фокусировке */
        }
        QSpinBox::up-arrow, QSpinBox::down-arrow {
        image: none;                    /* Убираем стандартные изображения стрелок */
        }
        QSpinBox::up-arrow {
        border-image: url(up-arrow.svg); /* Путь к SVG изображению стрелки вверх */
        }
        QSpinBox::down-arrow {
        border-image: url(down-arrow.svg); /* Путь к SVG изображению стрелки вниз */
        }
        """
        )
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(10, 20, 451, 121))
        font = QFont()
        font.setFamilies(["Roboto"])
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label.setStyleSheet(
            """
        QLabel{
        font-size: 22px; /* Размер шрифта */
        font-weight: bold; /* Жирный шрифт */
        color: #333; /* Цвет текста */
        text-align: center; /* Выравнивание по центру */
        margin-bottom: 15px; /* Отступ снизу */
        padding: 10px; /* Внутренние отступы */
        border-bottom: 4px solid #ccc; /* Нижняя граница */
        background-color: #f9f9f9; /* Цвет фона */
                font-family: 'Roboto', sans-serif; 
                border-radius: 8px;
        }
        """
        )
        self.label.setTextFormat(Qt.TextFormat.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 150, 451, 241))
        self.verticalLayout_general = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_general.setObjectName("verticalLayout_general")
        self.verticalLayout_general.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_1 = QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.TextFormat.PlainText)
        self.label_2.setWordWrap(True)
        self.verticalLayout_1.addWidget(self.label_2)
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(Qt.TextFormat.PlainText)
        self.label_3.setWordWrap(True)
        self.verticalLayout_1.addWidget(self.label_3)
        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(Qt.TextFormat.PlainText)
        self.label_6.setWordWrap(True)
        self.verticalLayout_1.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_1)
        self.verticalLayout_input = QVBoxLayout()
        self.verticalLayout_input.setObjectName("verticalLayout_input")
        self.spinBox_1 = QSpinBox(self.verticalLayoutWidget_3)
        self.spinBox_1.setObjectName("spinBox_1")
        sizePolicy.setHeightForWidth(self.spinBox_1.sizePolicy().hasHeightForWidth())
        self.spinBox_1.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies(["URW Bookman [UKWN]"])
        font1.setBold(True)
        font1.setItalic(True)
        self.spinBox_1.setFont(font1)
        self.verticalLayout_input.addWidget(self.spinBox_1)
        self.lineEdit_1 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_1.setObjectName("lineEdit_1")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_1.setSizePolicy(sizePolicy2)
        self.lineEdit_1.setFont(font1)
        self.verticalLayout_input.addWidget(self.lineEdit_1)
        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setFont(font1)
        self.verticalLayout_input.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_input)
        self.verticalLayout_general.addLayout(self.horizontalLayout)
        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")
        self.pushButton_1 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_1.setObjectName("pushButton_1")
        sizePolicy1.setHeightForWidth(
            self.pushButton_1.sizePolicy().hasHeightForWidth()
        )
        self.pushButton_1.setSizePolicy(sizePolicy1)
        self.horizontalLayout_buttons.addWidget(self.pushButton_1)
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_buttons.addWidget(self.pushButton_2)
        self.verticalLayout_general.addLayout(self.horizontalLayout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Главное меню", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "Мониторинг обстановки", None)
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "MainWindow", "Укажите периодичность сбора данных (СЕКУНДЫ)", None
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Укажите периодичность отправки данных (Часы:Минуты:СЕКУНДЫ)",
                None,
            )
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "MainWindow", "Указать почтовый ящик получателя", None
            )
        )
        self.pushButton_1.setText(
            QCoreApplication.translate("MainWindow", "Указать путь сохранения", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "Запустить Мониторинг", None)
        )
