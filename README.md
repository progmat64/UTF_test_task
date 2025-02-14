# UTF_test_task

## Установка и запуск

### Клонирование репозитория
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### Создание виртуального окружения и установка зависимостей
```bash
python -m venv venv
source venv/bin/activate
venv\Scripts\activate

pip install -r requirements.txt
```

### Применение миграций и создание суперпользователя
```bash
python manage.py migrate
python manage.py createsuperuser
```

### Запуск сервера
```bash
python manage.py runserver
```
API будет доступно по адресу:
```
http://127.0.0.1:8000/api/v1/foods/
```
