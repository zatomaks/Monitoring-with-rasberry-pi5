 ![rasberry pi5](https://www.raspberrypi.com/app/uploads/2023/10/RPi-5-Featured-Product-copy-1024x649.jpg) 
# 📡 Подключение трёх датчиков к Raspberry Pi 5

## 📋 Описание проекта

Данный проект демонстрирует подключение и использование **трёх различных датчиков** на платформе **Raspberry Pi 5**. Каждый из датчиков обеспечивает сбор и обработку данных об окружающей среде, что делает проект полезным для мониторинга параметров воздуха, окружающей среды и радиационного фона. Проект включает в себя установку необходимых библиотек, настройку соединений, пример подключение всех датчиков к пинам и готовое приложение по сбору данных с этих устройств и вывод информации в реальном времени на экран в виде анимированных графиков. 

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

   Далее будет представлена схематическая схема подключения датчиков к rasberry pi5 (На чертеже изображена 4 версия малины, но так как пины подключения у них одинаковы, это не играет принципиальную роль)
![Uploading Подключение.png…]()

