# KeyboardQuestion backend
Backend part of system for keyboard layout analysis. Made on Django REST Framework. Collects info about keyboard layouts and it's metrics. Uses PostgreSQL as backend database, creates Swagger and Redoc API documentation.

> [!NOTE]  
> Frontend is located in [separate repository](https://github.com/Catalyst-42/keyboard-question-frontend)

> [!NOTE]  
> Analyzer is located in [separate repository](https://github.com/Catalyst-42/keyboard-question-analyzer)

## Images
| ![Admin panel](<img/KeyboardQuestion - Admin panel.png>) | ![Backend api](<img/KeyboardQuestion - Backend api.png>) |
|-|-|

## Setup
To use system you need to create PostgreSQL database:

```sql
-- Database
CREATE DATABASE keyboard_db;

-- Create user for production
CREATE USER keyboard_db_control_user WITH PASSWORD '******';
GRANT ALL PRIVILEGES ON DATABASE keyboard_db TO keyboard_db_control_user;
GRANT ALL ON SCHEMA public TO keyboard_db_user;
GRANT CREATE ON SCHEMA public TO keyboard_db_user;
```

To run app you need to create `.env` file with app configuration. Example shown below:

```ini
# Django
DJANGO_SECRET_KEY=ilovecurrant

# Database
DB_NAME=keyboard_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

Also install all dependencies and appy common Django migrations.

```sh
# Install requirements
python3 -m venv venv
source venv/bin/activate

pip3 install --upgrade pip
pip3 install -r requirements.txt

# Apply migrations
cd keyboard_question
python3 manage.py makemigrations
python3 manage.py migrate
```

Also you may need to create admin account via `manage.py`:

```sh
python3 manage.py createsuperuser
```

Now you should be ready to go.

## Launch
To run app use common Django command:

```sh
python3 manage.py runserver
```

Now you can find app on `localhost:8000`. Watch full list of urls on `http://localhost:8000/redoc/` or `http://localhost:8000/swagger/`

<!-- 
TODO:

- [x] Normal readme
- [x] API keys in separate .env
- [x] Quety to get minand max values of metrics
- [x] Make private POST queries
-->
