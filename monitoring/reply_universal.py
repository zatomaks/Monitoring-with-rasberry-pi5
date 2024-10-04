# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtWidgets import QMessageBox


class Reply(QMessageBox):
	def __init__(self):
		super().__init__()
		self.setupUi()

	def setupUi(self):
		self.setWindowTitle("Подтверждение")
		self.setIcon(QMessageBox.Warning)
		# Кастомизация стиля диалогового окна
		self.setStyleSheet("""
			QMessageBox {
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
			
			QPushButton {
				background-color: #1976d2;     /* Синий цвет кнопки */
				color: white;                  /* Белый текст */
				border-radius: 5px;            /* Скругленные углы */
				padding: 5px 10px;             /* Отступы */
			}
			
			QPushButton:hover {
				background-color: #1565c0;     /* Темнее при наведении */
			}

			QPushButton:pressed {
				background-color: #0d47a1;     /* Ещё темнее при нажатии */
			}
		""")
		self.addButton(QMessageBox.Ok)

	
