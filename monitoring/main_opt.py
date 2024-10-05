import matplotlib

matplotlib.use("Qt5Agg")  # Или 'Agg' для работы без GUI
import matplotlib.colors
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
from gpiozero import DigitalInputDevice
import board
import time
from adafruit_bme280 import basic as adafruit_bme280

import datetime
import RPi.GPIO as GPIO
import pandas as pd
import os
import threading
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import shutil  # Для копирования файла
import mimetypes

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QWidget,
    QMainWindow,
    QFileDialog,
    QVBoxLayout,
)
import sys
from Main_menu import Ui_MainWindow
from Dialog import Ui_Dialog
from Monitor_observation import Ui_Form_1
from reply_universal import Reply
from graphic import SensorGraph, BuildGraph
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import threading
import pandas as pd
from scipy.interpolate import UnivariateSpline

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

counts = deque()

# Конфигурация GPIO
MQ135_PIN = 18  # GPIO пин, к которому подключен цифровой выход датчика MQ-135

# переменная для подсчета и перевод
counts = deque()
usvh_ratio = 0.00812037037037  # Перевод едениц для счетчика гейгера
geigerChannel = 4  # пин для гейгера


# устанвока пина
GPIO.setmode(GPIO.BCM)  # установка пина по его названию
GPIO.setwarnings(True)


# функция подсчета импульсов
def countme(channel):
    global counts
    timestamp = datetime.datetime.now()
    counts.append(timestamp)


# Set the input with falling edge detection for geiger counter pulses
GPIO.setup(geigerChannel, GPIO.IN)
GPIO.add_event_detect(geigerChannel, GPIO.FALLING, callback=countme)

# Настройка пина для чтения данных
mq135 = DigitalInputDevice(MQ135_PIN)

# Настройки для отправки почты
SMTP_SERVER = "smtp.mail.ru"  # SMTP-сервер (например, для Gmail)
SMTP_PORT = 587  # Порт
EMAIL_USER = "...."  # Ваш email
EMAIL_PASSWORD = "...."  # Ваш пароль от email

TO_EMAIL = "...."  # Email получателя по умолчанию (если не указать в меню)


class DialogBase(QDialog):
    def __init__(
        self, parent=None, label_text_from="Период с", label_text_to="По", path=None
    ):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self, label_text_from, label_text_to)
        self.label_text_from = label_text_from
        self.path = path
        self.checkboxes = {
            "Температура": self.ui.checkBox_6,
            "Давление": self.ui.checkBox_7,
            "Влажность": self.ui.checkBox_8,
            "Наличие газа": self.ui.checkBox_9,
            "Уровень радиации": self.ui.checkBox_10,
        }

        self.lineedits = {"beg": "", "end": ""}
        if label_text_from == "Период с" and label_text_to == "По":
            self.ui.lineEdit_3.textChanged.connect(self.format_time_lineedit)
            self.ui.lineEdit_4.textChanged.connect(self.format_time_lineedit)

        self.ui.buttonBox.accepted.connect(self.handle_ok)
        self.ui.buttonBox.rejected.connect(self.handle_cancel)

    def format_time_lineedit(self):
        sender = self.sender()
        text = sender.text()
        formatted_text = self.format_time(text)
        sender.blockSignals(True)
        sender.setText(formatted_text)
        sender.setCursorPosition(len(formatted_text))
        sender.blockSignals(False)

    @staticmethod
    def format_time(text):
        digits = "".join(filter(str.isdigit, text))
        if len(digits) <= 2:
            return digits
        elif len(digits) <= 4:
            return f"{digits[:2]}:{digits[2:]}"
        elif len(digits) <= 6:
            return f"{digits[:2]}:{digits[2:4]}:{digits[4:]}"
        else:
            return f"{digits[:2]}:{digits[2:4]}:{digits[4:6]}"

    def check_lineedits(self):
        self.lineedits["beg"] = self.ui.lineEdit_3.text()
        self.lineedits["end"] = self.ui.lineEdit_4.text()

    def check_checkboxes(self):
        self.selected_options = [
            label for label, checkbox in self.checkboxes.items() if checkbox.isChecked()
        ]

    # Функция для сглаживания с помощью скользящего среднего
    def smooth_column(self, data, window_size=5):
        """
        Сглаживание данных с помощью скользящего среднего.

        :param data: входные данные для сглаживания
        :param window_size: размер окна для скользящего среднего
        :return: сглаженные данные
        """
        return data.rolling(window=window_size, min_periods=1).mean()

    def read_copy_file(self):
        filepath = self.path + ".csv"
        temp_filepath = filepath + ".temp"  # расширение для создания копии
        try:
            shutil.copy(filepath, temp_filepath)  # Копируем файл
            df_c = pd.read_csv(temp_filepath)  # Читаем данные с копии файла в DataFrame
            df = df_c.iloc[:, :-2].apply(
                lambda col: self.smooth_column(col, window_size=5)
            )
            df[df_c.columns[-2]] = df_c[df_c.columns[-2]]
            df[df_c.columns[-1]] = df_c[df_c.columns[-1]]
            df = df.round(2)
        finally:
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)  # Удаляем временный копируемый файл
        return df

    def formation_array_period(self):
        df = self.read_copy_file()
        # Преобразование столбца 6 (индекс 5) в тип datetime.time
        df[5] = pd.to_datetime(df.iloc[:, 5], format="%H:%M:%S").dt.time
        # определение границ по времени
        start_time = pd.to_datetime(self.lineedits["beg"], format="%H:%M:%S").time()
        end_time = pd.to_datetime(self.lineedits["end"], format="%H:%M:%S").time()
        # Фильтруем по времени
        filtered_df = df[(df[5] >= start_time) & (df[5] <= end_time)]
        return [filtered_df.iloc[:, i].tolist() for i in range(6)]

    def formation_array_max(self, right=5, left=5):
        df = self.read_copy_file()
        results = []
        # Проходим по каждому столбцу, кроме последнего (с индексом 5)
        for col in df.columns[:-1]:
            max_index = df[
                col
            ].idxmax()  # индекс максимального значения в текущем столбце
            # Срезаем данные: 5 значений до максимума, само максимальное и 10 после
            start_index = max(0, max_index - left)
            end_index = min(len(df), max_index + right + 1)
            # Формируем список значений и соответствующих им времён из столбца с индексом 5
            values_and_times = [
                (int(df[col][i]), df.iloc[i, 5]) for i in range(start_index, end_index)
            ]
            results.append(
                values_and_times
            )  # список списков, где в каждом списке количество кортежей = right+left+1
            print(results)
        return results

    def handle_ok(self):
        self.check_checkboxes()
        self.check_lineedits()
        reply = Reply()
        if not self.selected_options:
            reply.setText("Не отмечен ни один из параметров")
            reply.exec()
        elif not self.lineedits["beg"] and not self.lineedits["end"]:
            reply.setText("Не корректно указан промежуток времени")
            reply.exec()
        else:
            self.accept()
            print(f"Следующие чекбоксы выбраны: {self.selected_options}")
            print(
                f'Следующие значения с lineedits: Слева: {self.lineedits["beg"]}, Справа: {self.lineedits["end"]}'
            )
            try:
                self.lineedits["beg"] = int(self.lineedits["beg"])
                self.lineedits["end"] = int(self.lineedits["end"])
            except:
                print("В диапазон данных вы ввели не числа, попробуйте ещё раз")

            if self.label_text_from == "Период с":
                (
                    self.y_array_temp,
                    self.y_array_pres,
                    self.y_array_hum,
                    self.y_array_rad,
                    self.y_array_gas,
                    self.x_array,
                ) = self.formation_array_period()
                selected_graphs = {
                    "Температура": (self.y_array_temp, "T(°C)"),
                    "Давление": (self.y_array_pres, "P, мм.рт.ст."),
                    "Влажность": (self.y_array_hum, "φ, %"),
                    "Наличие газа": (self.y_array_gas, "True/False"),
                    "Уровень радиации": (self.y_array_rad, "Рад, мкзв/час"),
                }
            else:
                (
                    self.array_temp,
                    self.array_pres,
                    self.array_hum,
                    self.array_rad,
                    self.array_gas,
                ) = self.formation_array_max(
                    right=self.lineedits["end"], left=self.lineedits["beg"]
                )

                selected_graphs = {
                    "Температура": (self.array_temp, "T(°C)"),
                    "Давление": (self.array_pres, "P, мм.рт.ст."),
                    "Влажность": (self.array_hum, "φ, %"),
                    "Наличие газа": (self.array_gas, "True/False"),
                    "Уровень радиации": (self.array_rad, "Рад, мкзв/час"),
                }

            # Оставляем только выбранные графики
            selected_graphs = {
                label: selected_graphs[label]
                for label in self.selected_options
                if label in selected_graphs
            }
            num_graphs = len(selected_graphs)  # количество выбранных графиков

            if num_graphs == 0:
                print("Не выбрано ни одного графика")
                return
            elif num_graphs == 1:
                fig, ax = plt.subplots(figsize=(8, 6))
                if self.label_text_from == "Период с":
                    for label, y_array in selected_graphs.items():
                        graph = BuildGraph(
                            ax,
                            label,
                            ylabel=y_array[1],
                            xlabel="t, c",
                            x_array=self.x_array,
                            y_array=y_array[0],
                            avg_value_bit=np.mean(y_array[0]),
                            max_value_bit=np.max(y_array[0]),
                        )
                        graph.draw_graph()
                else:
                    for label, array in selected_graphs.items():
                        y, x = zip(*array[0])
                        y, x = list(y), list(x)
                        graph = BuildGraph(
                            ax,
                            label,
                            ylabel=array[1],
                            xlabel="t, c",
                            x_array=x,
                            y_array=y,
                            avg_value_bit=np.mean(y),
                            max_value_bit=np.max(y),
                        )
                        graph.draw_graph()
            else:
                # Если графиков больше одного, используем сетку
                ncols = 2
                nrows = (
                    num_graphs + 1
                ) // ncols  # Рассчитываем строки с учётом остатка
                fig = plt.figure(figsize=(8, 3 * nrows))  # Общий размер фигуры
                gs = fig.add_gridspec(nrows, ncols)
                axs = []  # Список для хранения осей
                # Создаем оси для каждого графика с учетом комбинации ячеек для нечетных случаев
                for i in range(num_graphs):
                    row = i // ncols
                    col = i % ncols
                    if (
                        num_graphs == 3 and i == 2
                    ):  # Объединяем столбцы для 3-го графика
                        ax = fig.add_subplot(gs[1, :])
                    elif (
                        num_graphs == 5 and i == 4
                    ):  # Объединяем столбцы для 5-го графика
                        ax = fig.add_subplot(gs[2, :])
                    else:
                        ax = fig.add_subplot(gs[row, col])
                    axs.append(ax)

                # Перебираем выбранные графики и строим их на соответствующих осях
                if self.label_text_from == "Период с":
                    for ax, (label, y_array) in zip(axs, selected_graphs.items()):
                        print(self.x_array, y_array[0])
                        print(type(self.x_array), type(y_array[0]))

                        graph = BuildGraph(
                            ax,
                            label,
                            ylabel=y_array[1],
                            xlabel="t, c",
                            x_array=self.x_array,
                            y_array=y_array[0],
                            avg_value_bit=np.mean(y_array[0]),
                            max_value_bit=np.max(y_array[0]),
                        )

                        graph.draw_graph()
                else:
                    for ax, (label, array) in zip(axs, selected_graphs.items()):
                        y, x = zip(*array[0])
                        y, x = list(y), list(x)
                        graph = BuildGraph(
                            ax,
                            label,
                            ylabel=array[1],
                            xlabel="t, c",
                            x_array=x,
                            y_array=y,
                            avg_value_bit=np.mean(y),
                            max_value_bit=np.max(y),
                        )

                        graph.draw_graph()

            plt.tight_layout()
            plt.show()
            # print(f"y_array[1]{y_array[1]}")

    def handle_cancel(self):
        self.reject()


class DialogPeriod(DialogBase):
    def __init__(self, parent=None, path=None):
        super().__init__(parent)
        self.path = path
        self.ui.buttonBox.accepted.connect(self.handle_ok)
        self.ui.buttonBox.rejected.connect(self.handle_cancel)


class Monitor(QWidget):
    def __init__(
        self, parent=None, path=None, period=None, dispatch_period=None, mail=None
    ):
        super().__init__(parent)
        self.ui = Ui_Form_1()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.monitor_period)
        self.ui.pushButton_1.setCheckable(True)
        self.ui.pushButton_2.clicked.connect(self.max_value)
        self.ui.pushButton_2.setCheckable(True)

        self.temp = self.rad = self.pres = self.water = self.mq_bool = 0
        self.path = path
        self.timer_graf = period
        self.time_obj = datetime.datetime.strptime(dispatch_period, "%H:%M:%S")
        self.total_seconds = (
            self.time_obj.hour * 3600 + self.time_obj.minute * 60 + self.time_obj.second
        )
        self.diff = datetime.timedelta(seconds=self.total_seconds)
        self.mail = mail
        self.loop_count = 0
        # Создание Figure и FigureCanvas для графиков
        self.fig_temp = Figure()
        self.ax_temp = self.fig_temp.add_subplot(111)
        self.canvas_temp = FigureCanvas(self.fig_temp)

        self.fig_hum = Figure()
        self.ax_hum = self.fig_hum.add_subplot(111)
        self.canvas_hum = FigureCanvas(self.fig_hum)

        self.fig_pres = Figure()
        self.ax_pres = self.fig_pres.add_subplot(111)
        self.canvas_pres = FigureCanvas(self.fig_pres)

        self.fig_rad = Figure()
        self.ax_rad = self.fig_rad.add_subplot(111)
        self.canvas_rad = FigureCanvas(self.fig_rad)

        self.fig_gas = Figure()
        self.ax_gas = self.fig_gas.add_subplot(111)
        self.canvas_gas = FigureCanvas(self.fig_gas)

        self.temperature_graph = SensorGraph(
            self.ax_temp,
            "Температура",
            "T,\n(°C)",
            (0, 40),
            range(0, 45, 5),
            self.get_temperature,
            (0.03, 0.93, 0.03, 0.83, 0.03, 0.73),
            1,
            "o",
            (0.2, 0.81, 0.75),
            (1, 0.57, 0.25),
            1,
            (0.77, 0.98, 0.36),
        )
        self.humidity_graph = SensorGraph(
            self.ax_hum,
            "Влажность",
            "φ,\n(%)",
            (0, 100),
            range(0, 110, 10),
            self.get_humidity,
            (0.03, 0.93, 0.03, 0.83, 0.03, 0.73),
            1,
            "o",
            (0.43, 0.28, 0.84),
            (1, 0.88, 0.25),
            5,
            (0.42, 0.6, 0.07),
        )
        self.pressure_graph = SensorGraph(
            self.ax_pres,
            "Давление",
            "p,\n(мм.рт.ст.)",
            (720, 780),
            range(720, 785, 20),
            self.get_pressure,
            (0.03, 0.93, 0.03, 0.83, 0.03, 0.73),
            1,
            "o",
            (0.24, 0.63, 0.82),
            (1, 0.54, 0),
            10,
            (0.25, 0.09, 0.55),
        )
        self.radiation_graph = SensorGraph(
            self.ax_rad,
            "Радиация",
            "P,\n(мкЗв/ч)",
            (0, 1),
            np.arange(0, 1, 0.1),
            self.get_radiation,
            (0.03, 0.93, 0.03, 0.83, 0.03, 0.73),
            1,
            "o",
            (0.72, 0, 0.58),
            (0.74, 0.96, 0),
            0.05,
            (0, 0.71, 0.47),
        )
        self.gas_graph = SensorGraph(
            self.ax_gas,
            "Наличие газа",
            "True/\nFalse",
            (0, 2),
            range(0, 2, 1),
            self.get_gas,
            (0.03, 0.93, 0.03, 0.83, 0.03, 0.73),
            1,
            "o",
            (0.27, 0.17, 0.02),
            (0.06, 0.13, 0.28),
            1,
            (0.45, 0.25, 0.64),
        )

        self.ani_temp = animation.FuncAnimation(
            self.fig_temp,
            self.temperature_graph.update_graph,
            interval=self.timer_graf * 1000,
            blit=False,
            cache_frame_data=False,
        )
        self.ani_hum = animation.FuncAnimation(
            self.fig_hum,
            self.humidity_graph.update_graph,
            interval=self.timer_graf * 1000,
            blit=False,
            cache_frame_data=False,
        )
        self.ani_pres = animation.FuncAnimation(
            self.fig_pres,
            self.pressure_graph.update_graph,
            interval=self.timer_graf * 1000,
            blit=False,
            cache_frame_data=False,
        )
        self.ani_rad = animation.FuncAnimation(
            self.fig_rad,
            self.radiation_graph.update_graph,
            interval=self.timer_graf * 1000,
            blit=False,
            cache_frame_data=False,
        )
        self.ani_gas = animation.FuncAnimation(
            self.fig_gas,
            self.gas_graph.update_graph,
            interval=self.timer_graf * 1000,
            blit=False,
            cache_frame_data=False,
        )

        # Обновление canvas
        self.canvas_temp.draw()
        self.canvas_hum.draw()
        self.canvas_pres.draw()
        self.canvas_rad.draw()
        self.canvas_gas.draw()

        # Вставка графика температуры в label_1
        self.insert_canvas_into_label(self.canvas_temp, self.ui.label_1)
        self.insert_canvas_into_label(self.canvas_hum, self.ui.label_2)
        self.insert_canvas_into_label(self.canvas_pres, self.ui.label_3)
        self.insert_canvas_into_label(self.canvas_rad, self.ui.label_4)
        self.insert_canvas_into_label(self.canvas_gas, self.ui.label_5)

        self.thread = threading.Thread(target=self.main_loop, daemon=True)
        self.thread.start()

    def send_email_with_attachment(self):
        time_for_email = time.localtime()
        time_form = time.strftime("%d-%m-%Y", time_for_email)
        # Создаем копию CSV файла с расширением .txt
        txt_file = f"{self.path}.csv".replace(
            ".csv", ".txt"
        )  # Заменяем расширение на .txt
        shutil.copyfile(f"{self.path}.csv", txt_file)  # Копируем содержимое в .txt
        # Создаем объект сообщения
        msg = MIMEMultipart()
        msg["From"] = EMAIL_USER
        msg["To"] = self.mail
        msg["Subject"] = f"Мониторинг данных в .txt на {time_form}"
        body = "Во вложении находится .txt-файл с данными."
        msg.attach(MIMEText(body, "plain"))
        filename = os.path.basename(txt_file)
        ctype, encoding = mimetypes.guess_type(txt_file)
        maintype, subtype = ctype.split("/", 1)
        if maintype == "text":
            with open(txt_file) as fp:
                file = MIMEText(fp.read(), _subtype=subtype)
                fp.close()

        file.add_header(
            "Content-Disposition", "attachment", filename=filename
        )  # Добавляем заголовки
        msg.attach(file)  # Присоединяем файл к сообщению

        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.set_debuglevel(True)
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
            # server.sendmail(EMAIL_USER, TO_EMAIL, msg.as_string())
            print("Письмо с вложением успешно отправлено!")
            server.quit()
        except Exception as e:
            print(f"Не удалось отправить email: {e}")
        finally:
            # Удаление временной копии файла
            os.remove(txt_file)

    def periodic_email(self):
        # Функция для отправки email с файлом через заданный интервал
        self.send_email_with_attachment()  # Отправляем email

    def main_loop(self):
        # Функция для сбора данных с датчиков
        self.start_time = time.strftime("%H:%M:%S")
        self.start_time_obj = datetime.datetime.strptime(self.start_time, "%H:%M:%S")
        csv_file = f"{self.path}.csv"
        print(csv_file)
        try:
            while True:
                now_time = datetime.datetime.strptime(
                    time.strftime("%H:%M:%S"), "%H:%M:%S"
                )
                if (now_time - self.start_time_obj) >= self.diff:
                    self.periodic_email()
                    self.start_time_obj = datetime.datetime.strptime(
                        time.strftime("%H:%M:%S"), "%H:%M:%S"
                    )

                # проверка на наличие файла по мониторингу за определенный день
                if not os.path.isfile(csv_file):
                    self.write_data()
                # mq135
                self.mq_bool = 0
                if mq135.is_active:
                    print("Газ не обнаружен")
                else:
                    print("ГАЗЫ!")
                    self.mq_bool = 1

                self.temp = round(bme280.temperature, 2)
                self.water = round(bme280.humidity, 2)
                self.pres = round(bme280.pressure * 0.7506, 2)

                self.loop_count += 1

                try:
                    while counts[0] < datetime.datetime.now() - datetime.timedelta(
                        seconds=60
                    ):
                        counts.popleft()
                except IndexError:
                    pass  # Если в очереди нет записей.

                if self.loop_count == 1:
                    # Каждую self.loop_count итерацию сохраняем данные
                    imp = len(counts)
                    self.rad = round(len(counts) * usvh_ratio, 2)
                    self.loop_count = 0

                # Запись данных в файл
                new_data = pd.DataFrame(
                    {
                        "Температура, С": [self.temp],
                        "Давление, мм.рт.ст.": [self.pres],
                        "Влажность %": [self.water],
                        "Уровень рад., мкЗв/час": [self.rad],
                        "Уровень газа": [self.mq_bool],
                        "Время, ч.м.с.": [time.strftime("%H:%M:%S")],
                    }
                )
                print(new_data)
                new_data.to_csv(csv_file, mode="a", header=False, index=False)
                # Задержка перед следующим циклом
                time.sleep(self.timer_graf)

        except KeyboardInterrupt:
            print("Программа остановлена")

    def write_data(self):
        # Здесь можно создать новый CSV файл с заголовками
        headers = [
            "Температура, С",
            "Давление, мм.рт.ст.",
            "Влажность %",
            "Уровень рад., мкЗв/час",
            "Уровень газа",
            "Время, ч.м.с.",
        ]
        df = pd.DataFrame(columns=headers)
        df.to_csv(f"{self.path}.csv", index=False)

    def insert_canvas_into_label(self, canvas, label):
        # Убедитесь, что у label есть layout, если нет - создайте его
        if label.layout() is None:
            layout = QVBoxLayout()
            label.setLayout(layout)
        else:
            layout = label.layout()

        # Удалите все виджеты из QLabel (если есть)
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Добавьте canvas в layout
        layout.addWidget(canvas)

    def get_temperature(self):
        # Возвращаем последнее измеренное значение температуры
        return self.temp

    def get_humidity(self):
        # Возвращаем последнее измеренное значение влажности
        return self.water

    def get_pressure(self):
        # Возвращаем последнее измеренное значение давления
        return self.pres

    def get_radiation(self):
        # Возвращаем последнее измеренное значение радиации
        return self.rad

    def get_gas(self):
        # Возвращаем последнее измеренное значение газа
        return self.mq_bool

    def monitor_period(self):
        self.dialog_period = DialogPeriod(path=self.path)
        self.dialog_period.show()

    def max_value(self):
        self.dialog_max = DialogBase(
            label_text_from="Кол-во точек слева",
            label_text_to="Кол-во точек справа",
            path=self.path,
        )
        self.dialog_max.show()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.path = ""
        self.ui.pushButton_1.clicked.connect(self.save_file_dialog)
        self.ui.pushButton_2.clicked.connect(self.start_monitoring)
        self.ui.lineEdit_1.textChanged.connect(self.format_time_lineedit)
        self.ui.lineEdit_2.setText(TO_EMAIL)

    def format_time_lineedit(self):
        sender = self.sender()
        text = sender.text()
        formatted_text = self.format_time(text)
        sender.blockSignals(True)
        sender.setText(formatted_text)
        sender.setCursorPosition(len(formatted_text))
        sender.blockSignals(False)

    @staticmethod
    def format_time(text):
        digits = "".join(filter(str.isdigit, text))
        if len(digits) <= 2:
            return digits
        elif len(digits) <= 4:
            return f"{digits[:2]}:{digits[2:]}"
        elif len(digits) <= 6:
            return f"{digits[:2]}:{digits[2:4]}:{digits[4:]}"
        else:
            return f"{digits[:2]}:{digits[2:4]}:{digits[4:6]}"

    def save_file_dialog(self):
        current_date = time.strftime("%d.%m.%Y")
        print(current_date)
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить файл", current_date, "CSV.Files (*.csv)"
        )
        if file_path:
            self.path = file_path

    def start_monitoring(self):
        self.recording_period = int(self.ui.spinBox_1.value())
        self.dispatch_period = self.ui.lineEdit_1.text()
        self.mail = self.ui.lineEdit_2.text()
        reply = Reply()
        if self.recording_period == "0":
            reply.setText("Не указана периодичность сбора данных")
            reply.exec()
        elif not self.dispatch_period:
            reply.setText("Не указана периодичность отправки данных")
            reply.exec()
        elif not self.mail:
            reply.setText("Не указан почтовый ящик получателя")
            reply.exec()
        elif not self.path:
            reply.setText("Не указан путь сохранения файла")
            reply.exec()
        else:
            print(
                f"Периодичность сбора: {self.recording_period}, Периодичность отправки: {self.dispatch_period}, Почтовый ящик: {self.mail}"
            )
            self.monitor = Monitor(
                path=self.path,
                period=self.recording_period,
                dispatch_period=self.dispatch_period,
                mail=self.mail,
            )
            self.monitor.show()


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.setWindowTitle("Главное меню программы")
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error occurred: {e}")
