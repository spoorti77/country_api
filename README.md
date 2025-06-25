# 🌍 Country-State-City API

A free and open-source API built with Django & Django REST Framework that provides Countries, States, and Cities data — structured, searchable, and ready to consume.

---

## 📌 Features

- ✅ List of all countries with ISO2/ISO3 codes
- ✅ Get all states for a given country
- ✅ Get all cities for a given state
- ✅ Search cities by name
- ✅ Swagger & Redoc documentation
- ✅ RESTful API with Django ORM

---


## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/spoorti77/country_api.git
cd country_api
````

### 2. Set up Virtual Environment

```bash
python -m venv env
env\Scripts\activate   # On Windows
# source env/bin/activate  # On Linux/macOS
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install django djangorestframework drf-yasg
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Import Country, State, and City Data

```bash
python manage.py import_locations
```

Ensure your JSON files are placed in `locations/data/` folder:

* `countries.json`
* `states.json`
* `cities.json`

### 6. Start the Server

```bash
python manage.py runserver
```

---

## 📘 API Documentation

Swagger UI:
👉 `http://127.0.0.1:8000/swagger/`

Redoc:
👉 `http://127.0.0.1:8000/redoc/`

---

## 📬 API Endpoints

| Method | Endpoint                          | Description                     |
| ------ | --------------------------------- | ------------------------------- |
| GET    | `/api/countries/`                 | List all countries              |
| GET    | `/api/countries/<iso2>/states/`   | List states for a given country |
| GET    | `/api/states/<state_id>/cities/`  | List cities for a given state   |
| GET    | `/api/cities/?search=<city_name>` | Search for cities               |

---

## 📦 Project Structure

```
country_api/
├── locations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── data/
│       ├── countries.json
│       ├── states.json
│       └── cities.json
├── manage.py
└── country_api/
    └── settings.py
```

---

## 🛡 License

This project is licensed under the MIT License.

---

## 🙋‍♀️ Maintainer

**Spoorti Jadhav**
Python Django Developer
[GitHub Profile](https://github.com/spoorti77)

---

```


