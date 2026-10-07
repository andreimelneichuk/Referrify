# Referrify

Черновик REST API для реферальной системы на FastAPI: регистрация пользователя, получение JWT и создание реферального кода.

**Статус: не завершён.** Реализованы не все задуманные функции, см. раздел «Состояние».

## Стек

- FastAPI
- SQLAlchemy 2 (async), по умолчанию SQLite через `aiosqlite`; другая БД задаётся через `DATABASE_URL`
- JWT (`python-jose`), хэширование паролей (`passlib`)
- `python-dotenv` для чтения `.env`

## Эндпоинты

- `POST /register/` — регистрация по email и паролю;
- `POST /token/` — получение access-токена по email и паролю;
- `POST /referral/` — создание реферального кода с датой истечения для текущего пользователя.

## Состояние

- Удаление кода и регистрация по реферальному коду не реализованы.
- В `crud.py` нет функции `get_referral_code`, которую вызывает `POST /referral/`.
- Таблицы БД автоматически не создаются.
- Тестов нет, `app/cache.py` пустой.

## Запуск

```bash
git clone https://github.com/andreimelneichuk/Referrify.git
cd Referrify
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs
