# Автоматизированные тесты для [Яндекс Самокат - учебный тренажер](https://qa-scooter.praktikum-services.ru/)

Яндекс Самокат - это тестовая онлайн-платформа для заказа самокатов и получения информации о них.

## Обзор

Этот репозиторий содержит автоматизированные тесты для учебного веб-приложения Яндекс Самокат, реализованные с использованием Selenium WebDriver и Python.

## Используемые технологии

- Python 3.11.9
- Selenium WebDriver 4.21.0
- Pytest
- Allure (для генерации отчетов)
- Faker (для генерации случайных тестовых данных)

## Описания тестов

### tests_header.py

- **test_click_on_scooter_logo_and_redirect_to_main_page**: Проверяет открытие главной страницы по клику на логотип "Самокат".
- **test_click_on_yandex_logo_and_redirect_to_dzen**: Проверяет открытие главной страницы "Дзен" по клику на логотип "Яндекс".

### tests_order_scooter.py

- **test_order_scooter**: Проверяет оформление заказа самоката с различными наборами данных.

### tests_main_page.py

- **test_click_on_question_get_answer**: Проверяет соответствие ответов на вопросы в блоке "Вопросы о важном".
