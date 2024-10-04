# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
)


class Ui_Form_1(object):
    def setupUi(self, Form_1):
        if not Form_1.objectName():
            Form_1.setObjectName("Form_1")
        Form_1.resize(1204, 799)
        # Фиксируем размер окна, чтобы оно не могло изменяться
        Form_1.setFixedSize(1204, 799)

        # Отключаем кнопку развертывания (оставляем только сворачивание и закрытие)
        Form_1.setWindowFlags(Form_1.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        Form_1.setStyleSheet(
            """
        QWidget {
            background-color: #99FFCC;
            font-family: 'Roboto', sans-serif;
        }
        QLabel {
            background-color: #f0f4f8;     /* Светло-серый фон для современного стиля */
            color: #333333;                /* Тёмно-серый цвет текста */
            border: 1px solid #cfd8dc;     /* Тонкая светлая граница */
            border-radius: 8px;            /* Скругленные углы */
            padding: 0.5px 1px;             /* Внутренние отступы для аккуратности */
            font-size: 18px;               /* Удобный размер шрифта */
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
            border: 1px solid #1976d2;     /* Синяя граница при фокусировке (если используется) */
            background-color: #ffffff;     /* Белый фон при фокусировке */
        }
        QPushButton {
            background-color: #5bc0de;  /* Яркий голубой */
            color: #ffffff;  /* Белый текст */
            border: none;
            border-radius: 10px;
            padding: 10px 15px;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  /* Легкая тень */
            transition: background-color 0.3s ease, box-shadow 0.3s ease;  /* Плавные переходы */
        }

        QPushButton:hover {
            background-color: #31b0d5;  /* Темнее при наведении */
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);  /* Глубже тень */
        }

        QPushButton:pressed {
            background-color: #1b97b2;  /* Еще темнее при нажатии */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);  /* Меньшая тень при нажатии */
        }

        QPushButton:disabled {
            background-color: #b0bec5;  /* Светло-серый для выключенных кнопок */
            color: #ffffff;
            box-shadow: none;  /* Без тени */
        }

        QPushButton:focus {
            outline: none;  /* Убираем стандартную границу фокуса */
            border: 2px solid #0077b6;  /* Ярко-синий обвод для фокуса */
            background-color: #48cae4;  /* Светлый фон при фокусе */
        }

        """
        )
        # Основная горизонтальная компоновка
        self.horizontalLayoutWidget = QWidget(Form_1)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 1181, 781))
        self.horizontalLayout_general = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_general.setContentsMargins(0, 0, 0, 0)

        # Левая вертикальная компоновка
        self.verticalLayout_left = QVBoxLayout()
        self.label_1 = QLabel(self.horizontalLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_left.addWidget(self.label_1)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_left.addWidget(self.label_2)
        self.horizontalLayout_general.addLayout(self.verticalLayout_left)

        # Центральная вертикальная компоновка
        self.verticalLayout_center = QVBoxLayout()
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_center.addWidget(self.label_3)
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_center.addWidget(self.label_4)
        self.horizontalLayout_general.addLayout(self.verticalLayout_center)

        # Правая вертикальная компоновка
        self.verticalLayout_left_2 = QVBoxLayout()
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_left_2.addWidget(self.label_5)

        # Нижняя часть правой вертикальной компоновки
        self.verticalLayout_right_down = QVBoxLayout()

        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setStyleSheet(
            """
        QLabel {
            background-color: #f0f4f8;     /* Светло-серый фон для современного стиля */
            color: #333333;                /* Тёмно-серый цвет текста */
            border: 1px solid #cfd8dc;     /* Тонкая светлая граница */
            border-radius: 8px;            /* Скругленные углы */
            padding: 8px 12px;             /* Внутренние отступы для аккуратности */
            font-size: 18px;               /* Удобный размер шрифта */
            font-weight: bold;             /* Жирный текст для акцента */
            text-align: center;            /* Центрирование текста */
            font-family: 'Roboto', sans-serif; 
        }

        """
        )
        self.verticalLayout_right_down.addWidget(self.label_6)

        # Кнопка pushButton_1
        self.pushButton_1 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_1.setObjectName("pushButton_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.verticalLayout_right_down.addWidget(self.pushButton_1)

        # Кнопка pushButton_2
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.verticalLayout_right_down.addWidget(self.pushButton_2)
        self.verticalLayout_left_2.addLayout(self.verticalLayout_right_down)
        self.horizontalLayout_general.addLayout(self.verticalLayout_left_2)
        self.retranslateUi(Form_1)
        QMetaObject.connectSlotsByName(Form_1)

    def retranslateUi(self, Form_1):
        Form_1.setWindowTitle(
            QCoreApplication.translate(
                "Form_1", "Мониторинг в режиме реального времени", None
            )
        )
        self.label_1.setText(QCoreApplication.translate("Form_1", "", None))
        self.label_2.setText(QCoreApplication.translate("Form_1", "", None))
        self.label_3.setText(QCoreApplication.translate("Form_1", "", None))
        self.label_4.setText(QCoreApplication.translate("Form_1", "", None))
        self.label_5.setText(QCoreApplication.translate("Form_1", "", None))
        self.label_6.setText(
            QCoreApplication.translate("Form_1", "Посмотреть изменение данных", None)
        )
        self.pushButton_1.setText(
            QCoreApplication.translate("Form_1", "В указанном диапазоне", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("Form_1", "Вокруг максимального значения", None)
        )
