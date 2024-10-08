 ![rasberry pi5](https://www.raspberrypi.com/app/uploads/2023/10/RPi-5-Featured-Product-copy-1024x649.jpg) 
# 📡 Подключение трёх датчиков к Raspberry Pi 5

## 📋 Описание проекта

Данный проект демонстрирует подключение и использование **трёх различных датчиков** на платформе **Raspberry Pi 5**. Каждый из датчиков обеспечивает сбор и обработку данных об окружающей среде, что делает проект полезным для мониторинга параметров воздуха, окружающей среды и радиационного фона. Проект включает в себя установку необходимых библиотек, настройку и соединение датчиков, пример подключения датчиков к соответствующим пинам на Raspberry Pi 5 и готовое desktop приложение по сбору данных с этих устройств и вывод информации в режиме реального времени на экран в виде анимированных графиков, представляющих зависимость параметра в единицу времени. 

### 🛠️ Подключаемые датчики:

1. **BME-280** — датчик температуры, давления и влажности.
2. **MQ-135** — газовый датчик для обнаружения различных газов (включая CO₂, аммиак и другие вредные вещества).
3. **RadiationD-1.1v (Cajoe)** — датчик радиации для измерения уровня гамма-излучения.

## ⚙️ Установка и настройка

Перед началом работы с проектом необходимо выполнить следующие шаги:

1. **Клонировать репозиторий:**
   ```bash
   git clone <URL вашего репозитория>
   cd <название папки проекта>
   ```
2. **Установить все необходимые зависимости из `requirements.txt`:**
   ```bash
   pip3 install -r requirements.txt
   ```


3. **Подключить датчики к Raspberry Pi:**
   - Для **BME-280** используйте шину I2C.
   - Для **MQ-135** подключите аналоговый выход к аналогово-цифровому преобразователю (например, ADS1115).
   - Для **RadiationD-1.1v** используйте GPIO пины для подключения.
4. **Установка библиотек**
   Все библиотеки можно установить, следуя пункту 2, но при использовании именно **Raspberry Pi 5**, и использовани библиотеки RPi.GPIO, следует использовать следующую команду:
   ```
   - sudo apt remove python3-rpi.gpio
   - python3 -m pip install rpi-lgpio
   ```
   Для коректной работы данного модуля для считывания данных с счетчика гейгера и газового датчика.
   
   Далее будет представлена схематическая схема подключения датчиков к **Raspberry Pi 5** (На схеме изображена 4 версия малины, но так как пины подключения у них одинаковы, это не играет принципиальную роль)
![Подключение](https://github.com/user-attachments/assets/b7aefda0-4d60-436e-9b08-5b5a257e4c33)
## Приложение для отображения и отправки данных с датчиков

На изображении представлено первоначальное окно программы для мониторинга обстановки. Интерфейс выполнен в светло-зелёных тонах и состоит из нескольких блоков с возможностью ввода и настройки параметров. Вот описание ключевых элементов интерфейса:

1. **Заголовок**:
   В верхней части окна указан заголовок — "Главное меню программы".

2. **Название приложения**:
   В центральной части окна отображается название: **"Мониторинг обстановки"**. Оно выделено крупным шрифтом и обрамлено рамкой, что указывает на основную цель приложения.

3. **Поля для настройки параметров**:
   - **Периодичность сбора данных (СЕКУНДЫ)**: 
     Справа находится поле ввода, где пользователь может задать интервал в секундах, через который программа будет собирать данные с подключённых датчиков. В примере указано значение **"2"**, то есть сбор данных с датчиков осуществляется каждые 2 секунды.
   
   - **Периодичность отправки данных (ЧАСЫ:МИНУТЫ:СЕКУНДЫ)**:
     В следующем блоке можно задать периодичность отправки данных. Формат ввода времени — ЧАСЫ:МИНУТЫ:СЕКУНДЫ. В примере указано **"02:00:00"**, что означает отправку данных каждые 2 часа.

   - **Почтовый ящик получателя**:
     Поле для указания e-mail адреса, на который будут отправляться данные. В примере введён адрес **"abcd@mail.ru"**.

4. **Кнопки управления**:
   - **"Указать путь сохранения"**: 
     Кнопка для выбора директории, куда будут сохраняться файлы с данными мониторинга.
   
   - **"Запустить Мониторинг"**:
     Главная кнопка для старта процесса мониторинга с заданными параметрами. После нажатия программа начнёт собирать и обрабатывать данные в реальном времени, которые уже в следующем экране будут отбражены на анимированных графиках.

 
![Screenshot from 2024-09-28 11-12-17](https://github.com/user-attachments/assets/a5599bbb-fba0-45c0-99cd-79906e880ef3)

###  📊 Окно мониторинга в реальном времени  

После нажатия кнопки **"Запустить Мониторинг"**, происходит открытие следующего окна **"Мониторинг в реальном времени"**.

 На котором отображены анимированные графики всех измеряемых параметров. Значения на изображении обнавляются через заданное ранее время (в секундах), указанное в предыдущем окне. Таким образом, оператор может получать как визуальное представление о ситуации по измеряемым парметрам, так и в виде обновляемого и отправляемого по почте файла. Так измеряемыми парметрами стали:
 ![Screenshot from 2024-09-28 11-15-50](https://github.com/user-attachments/assets/811c63fb-c28e-428e-bf14-458b6efacf0d)

- *Температура (°C)*;
- *Давление (мм.рт.ст.)*;
- *Наличие газа (True/False)*;
- *Влажность (%)*;
- *Уровень радиации (мкЗв/ч)*.

А также среднее значение, максимальное значение, текущее значение всех парметров, которые снесены в отдельные текстовые боксы в верхнем углу графиков.

### ⌨ Дополнительные Функции приложения:

Графическое представление данных в реальном времени.

Кнопки для фильтрации данных:

1. В указанном диапазоне — позволяет выбрать и отобразить данные за конкретный период.

2. Вокруг максимального значения — выделение и анализ данных вокруг пиковых значений.

Эта страница дает пользователям возможность наблюдать за состоянием окружающей среды, а также оперативно реагировать на любые изменения параметров, таких как резкое увеличение концентрации газа или уровня радиации.

#### 👉 👈В указанном диапазоне

Данное окно открывается при нажатии **"В указанном диапазоне"**.

![Screenshot from 2024-09-28 12-13-03](https://github.com/user-attachments/assets/b204436c-6d36-41bb-9c5e-b19073706696)

И выводит график выбранных парметров в указанном временном интервале.

![Screenshot from 2024-09-28 12-40-17](https://github.com/user-attachments/assets/85dac0ea-b90f-423e-abc1-db122a77a458)

#### 📈 Вокруг максимального значения

Также есть возможность просмотра максимального значения по выбранным парметрам по данным, собранным после запуска программы (файл создается каждые сутки новый), с указанием количества значений вокруг этой максимальной точки для оценки самого максимума.

![Screenshot from 2024-09-28 12-46-43](https://github.com/user-attachments/assets/80947476-f9ab-48a8-a380-d32379700042)

![Screenshot from 2024-09-28 12-47-24](https://github.com/user-attachments/assets/e5a81b4a-6032-43d8-836f-ec700442e9f6)


