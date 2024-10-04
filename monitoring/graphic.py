import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import matplotlib.ticker as ticker
import numpy as np


class SensorGraph:
    def __init__(
        self,
        ax,
        title,
        ylabel,
        ylim,
        yticks,
        data_func,
        kordinat_lable,
        line_widh,
        mar_ker,
        rgb_fill_color_f,
        rgb_fill_color_l,
        step_line,
        marker_facecolor,
    ):
        self.ax = ax
        self.title = title
        self.ylabel = ylabel
        self.ylim = ylim
        self.yticks = yticks
        self.data_func = data_func
        self.x_data = []
        self.y_data = []
        self.total = 0
        self.count = 0
        self.max_value = float("-inf")
        self.kordinat_lable = kordinat_lable
        x1, y1 = self.kordinat_lable[:2]
        x2, y2 = self.kordinat_lable[2:4]
        x3, y3 = self.kordinat_lable[4:]
        self.line_widh = line_widh
        self.mar_ker = mar_ker
        self.rgb_fill_color_f = rgb_fill_color_f
        self.rgb_fill_color_l = rgb_fill_color_l
        self.step_line = step_line
        self.marker_facecolor = marker_facecolor
        self.fill = None

        # Настройка линии и текстов
        (self.line,) = self.ax.plot(
            [],
            [],
            marker=self.mar_ker,
            linewidth=self.line_widh,
            color=self.rgb_fill_color_l,
            markerfacecolor=self.marker_facecolor,
        )
        self.avg_text = self.ax.text(
            x1,
            y1,
            "",
            transform=self.ax.transAxes,
            fontsize=7,
            verticalalignment="bottom",
            bbox=dict(facecolor="skyblue", alpha=0.5),
        )
        self.max_text = self.ax.text(
            x2,
            y2,
            "",
            transform=self.ax.transAxes,
            fontsize=7,
            verticalalignment="bottom",
            bbox=dict(facecolor="red", alpha=0.5),
        )
        self.now_text = self.ax.text(
            x3,
            y3,
            "",
            transform=self.ax.transAxes,
            fontsize=7,
            verticalalignment="bottom",
            bbox=dict(facecolor="green", alpha=0.5),
        )

        # Настройки осей
        self.ax.set_title(self.title)
        self.ax.set_xlabel("Время: час.мин.сек.")

        # Убираем стандартную подпись оси Y
        self.ax.set_ylabel("")

        # Устанавливаем метку оси Y вручную сверху оси
        self.ax.text(
            x=-0.05,
            y=1.03,
            s=self.ylabel,
            transform=self.ax.transAxes,
            fontsize=8,
            ha="center",
            va="bottom",
            rotation=0,
        )

        self.ax.set_ylim(self.ylim)
        self.ax.set_yticks(self.yticks)
        self.ax.grid(True, which="major", linestyle="-", linewidth=0.1, color="black")
        self.ax.grid(True, which="minor", linestyle=":", linewidth=0.5)
        self.ax.yaxis.set_minor_locator(plt.MultipleLocator(self.step_line))
        self.ax.yaxis.set_minor_formatter(plt.NullFormatter())

    def update_graph(self, frame):
        # Обновляем данные
        current_time_str = time.strftime("%H:%M:%S")
        value = round(self.data_func(), 2)

        self.total += value
        self.count += 1
        avg_value = round(self.total / self.count, 2)
        self.max_value = max(self.max_value, value)

        self.x_data.append(current_time_str)
        self.y_data.append(value)

        if len(self.x_data) > 20:
            self.x_data.pop(0)
            self.y_data.pop(0)

        # Обновляем линию
        self.line.set_data(range(len(self.x_data)), self.y_data)
        self.ax.set_xlim(0, 20)
        self.ax.set_xticks(range(len(self.x_data)))
        self.ax.set_xticklabels(self.x_data, rotation=45, ha="right", fontsize=5)

        # Обновляем текст
        self.avg_text.set_text(f"Среднее значение: {avg_value:.2f}")
        self.max_text.set_text(f"Максимальное значение: {self.max_value:.2f}")
        self.now_text.set_text(f"Текущее значение: {value:.2f}")

        # Удаляем старую заливку, если она существует
        if self.fill is not None:
            self.fill.remove()

        # Закрашиваем под графиком
        self.fill = self.ax.fill_between(
            range(len(self.x_data)), self.y_data, alpha=0.5, color=self.rgb_fill_color_f
        )

        return self.line, self.avg_text, self.max_text, self.now_text


class BuildGraph:
    def __init__(
        self, ax, title, ylabel, xlabel, x_array, y_array, avg_value_bit, max_value_bit
    ):
        self.ax = ax

        self.x_array = x_array
        self.y_array = y_array
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        self.avg_value_bit = avg_value_bit
        self.max_value_bit = max_value_bit

        self.avg_text_bit = self.ax.text(
            0.03,
            0.93,
            "",
            transform=self.ax.transAxes,
            fontsize=5,
            verticalalignment="bottom",
            bbox=dict(facecolor="skyblue", alpha=0.5),
        )
        self.max_text_bit = self.ax.text(
            0.03,
            0.83,
            "",
            transform=self.ax.transAxes,
            fontsize=5,
            verticalalignment="bottom",
            bbox=dict(facecolor="red", alpha=0.5),
        )

        # Инициализация графика с тонкими линиями и маленькими точками
        (self.line,) = self.ax.plot([], [], marker="o", linewidth=1, markersize=3)

    def draw_graph(self):

        # Установка заголовков и меток
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)

        # Построение графика с очень тонкой линией и маленькими точками
        (self.line,) = self.ax.plot(
            self.x_array, self.y_array, marker="o", linewidth=1, markersize=3
        )
        # Форматирование оси Y
        self.ax.yaxis.set_major_formatter(
            ticker.StrMethodFormatter("{x:.1f}")
        )  # Форматирование

        # Настройка сетки
        self.ax.grid(
            True, which="major", linestyle="-", linewidth=0.2, color="black"
        )  # Очень тонкие линии сетки
        # self.ax.grid(True, which='minor', linestyle=':', linewidth=0.2)

        self.ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
        self.ax.yaxis.set_minor_formatter(plt.NullFormatter())

        # Установка подписей только для первой и последней точки
        first_label = self.x_array[0]
        last_label = self.x_array[-1]
        self.ax.set_xticks(
            [0, len(self.x_array) - 1]
        )  # Индексы для первой и последней точки
        self.ax.set_xticklabels(
            [first_label, last_label]
        )  # Подписи только для этих точек
        self.avg_text_bit.set_text(f"Среднее значение: {self.avg_value_bit:.2f}")
        self.max_text_bit.set_text(f"Максимальное значение: {self.max_value_bit:.2f}")
        # Заполнение области под графиком
        self.ax.fill_between(
            self.x_array, self.y_array, color="skyblue", alpha=0.5, hatch="x"
        )

        # Перерисовка
        self.ax.relim()  # Обновление пределов
        self.ax.autoscale_view()  # Автоматическая подстройка осей

        return self.line
