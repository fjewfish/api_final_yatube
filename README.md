# Проект «API для Yatube» 
#### API и документация для приложения Yatube.
___
## Стек технологий:
- Python,
- Djando, 
- DRF
- JWT
___
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/fjewfish/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
```

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

***
#### Полная redoc документация доступна по url: (после запуска сервера):
http://localhost:8000/redoc/
***
