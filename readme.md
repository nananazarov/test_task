# Тестовое задание

## Настройка окружения

1. Создание виртуального окружения:

```bash
python -m venv venv
```

2. Активация виртуального окружения:

   - В Windows:

   ```bash
   venv\Scripts\activate
   ```

   - В macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

3. Установка зависимостей:

```bash
pip install -r requirements.txt
```

4. Запуск генератора тестовых данных:

```bash
python -m helpers.dummy_data_generator
```

## Задачи

1. **Добавление поля номера телефона**

   - Добавить переменную с номером телефона в класс SQLIntegrationReader

2. **Создание пилотной стратегии**

   - Для репитных клиентов, чей номер телефона оканчивается цифрой 2 или 4 применить стратегию RepeatClientPilotStrategy

3. **Тестирование**
   - Сгенерировать тестовые данные с помощью helpers.dummy_data_generator
   - Запустить расчет с помощью runner.py
   - Убедиться, что стратегия работает, можно использовать helpers.test_result_look_up
