# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QRect,
    Qt,
)
from PySide6.QtWidgets import (
    QCheckBox,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog, label_text_from="Период с", label_text_to="По"):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(367, 382)
        Dialog.setFixedSize(367, 382)
        Dialog.setWindowFlags(Dialog.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        Dialog.setStyleSheet(
            """
        QDialog{
                background-color: #99FFCC;
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
        QCheckBox {
                background-color: #f0f4f8; /* Светло-серый фон */
                color: #333333;            /* Тёмно-серый цвет текста */
                border: 1px solid #cfd8dc;     /* Тонкая светлая граница */
                border-radius: 8px;            /* Скругленные углы */
                padding: 8px 12px;             /* Внутренние отступы для аккуратности */
                font-size: 14px;               /* Удобный размер шрифта */
                font-weight: bold;             /* Жирный текст для акцента */
                text-align: center;            /* Центрирование текста */
                font-family: 'Roboto', sans-serif; 
                }
        QCheckBox::indicator {
                width: 18px;               /* Размер чекбокса */
                height: 18px;
                border: 1px solid #cfd8dc; /* Тонкая граница чекбокса */
                border-radius: 4px;        /* Скруглённые углы чекбокса */
                background-color: #ffffff; /* Белый фон чекбокса */
                }
        QCheckBox::indicator:checked {
                background-color: #00BCD4; /* Яркий бирюзовый цвет при отмеченном состоянии */
                border: 1px solid #00BCD4; /* Цвет границы при отмеченном состоянии */
                }
        QCheckBox::indicator:hover {
                background-color: #e0f7fa; /* Светлее фон при наведении */
                }
        QCheckBox::indicator:pressed {
                background-color: #00ACC1; /* Темнее фон при нажатии */
                }
        QCheckBox::indicator:disabled {
                background-color: #e0e0e0; /* Светло-серый фон при отключенном состоянии */
                border: 1px solid #bdbdbd; /* Светло-серая граница при отключенном состоянии */
                }
        """
        )
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 341, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3.setWordWrap(True)
        self.label_3.setFixedWidth(90)
        self.label_3.setAlignment(Qt.AlignCenter)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.label_4.setWordWrap(True)
        self.label_4.setFixedWidth(90)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 110, 241, 261))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_7 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_2.addWidget(self.checkBox_7)
        self.checkBox_8 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_2.addWidget(self.checkBox_8)
        self.checkBox_9 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_2.addWidget(self.checkBox_9)
        self.checkBox_10 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout_2.addWidget(self.checkBox_10)
        self.buttonBox = QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setStyleSheet("")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.retranslateUi(Dialog, label_text_from, label_text_to)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)

    # setupUi
    def retranslateUi(self, Dialog, label_text_from, label_text_to):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Диалоговое окно"))
        self.label_3.setText(QCoreApplication.translate("Dialog", label_text_from))
        self.label_4.setText(QCoreApplication.translate("Dialog", label_text_to))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", "Температура"))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", "Давление"))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", "Влажность"))
        self.checkBox_9.setText(QCoreApplication.translate("Dialog", "Наличие газа"))
        self.checkBox_10.setText(
            QCoreApplication.translate("Dialog", "Уровень радиации")
        )
