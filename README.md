# Holiday Tour

A small Django-based holiday tour website project. This repository contains a simple tour booking site built with Django, using SQLite for local development.

## Features

- Basic tour listing pages
- Booking forms and admin management
- Static files and templates included

## Prerequisites

- Python 3.8+ installed
- `pip` available

## Setup (Windows / PowerShell)

1. Create and activate a virtual environment:

```
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```
py -m pip install -r requirements.txt
```

3. Apply migrations and create a superuser (if needed):

```
py manage.py migrate
py manage.py createsuperuser
```

4. Run the development server:

```
py manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Project Structure (important files)

- `manage.py` — Django management script
- `db.sqlite3` — local SQLite database (development)
- `templates/` — HTML templates (includes `index.html`)
- `static/` — CSS, images
- `toursite/` — Django app and settings

## Notes

- This project is configured for local development. For production, configure a production-ready database, static files hosting, and secure settings.

## License

Include your preferred license here.

---
If you'd like the README expanded (badges, CI, contribution guide), tell me what to include.
#
