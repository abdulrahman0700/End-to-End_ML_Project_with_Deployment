# ⚽ Score Rate Prediction Web App

An end-to-end machine learning web application that predicts a football player's **season rating** based on historical performance statistics. Built with a `RandomForestRegressor` model and served through a Flask API, the app is designed to help coaches, analysts, and sports enthusiasts evaluate player performance across seasons.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED.svg)](https://www.docker.com/)

---

## 📖 Overview

This project implements a complete machine learning pipeline — from data collection and feature engineering to model training, evaluation, and deployment.

The model is trained on historical player statistics (goals, assists, playing time, and more) across multiple seasons and predicts a player's season rating. It is deployed as a lightweight Flask web service, hosted on **Hugging Face**, making it easy to integrate into other applications via a simple API call.

---

## 🏗️ Architecture & Pipeline

### 1. Data Collection & Preprocessing
- Historical player statistics were collected, including goals, assists, playing time, and other season-level metrics.
- Missing values were handled using **median imputation**.
- Categorical variables were transformed using **one-hot encoding**.
- Numerical features were scaled to ensure uniform contribution to the model.

### 2. Feature Engineering
- Engineered features such as average performance over past seasons and injury history to improve prediction accuracy.
- Applied correlation analysis to select the most impactful features.

### 3. Modeling
- Trained a **RandomForestRegressor** for its robustness on complex, tabular datasets with minimal tuning.
- **Key hyperparameters:**
  - `n_estimators`: 100
  - `max_depth`: 10
- Data split: 80% training / 20% testing.

### 4. Model Evaluation

| Metric | Score |
|---|---|
| RMSE (Root Mean Square Error) | 0.85 |
| R² (R-squared) | 0.92 |
| MAE (Mean Absolute Error) | 0.65 |

Cross-validation was used to confirm the model generalizes well and avoids overfitting.

### 5. Deployment
- The trained model is served through a **Flask** REST API.
- The app is containerized with **Docker** and hosted on **Hugging Face Spaces**.
- Clients send player statistics to the API and receive real-time predicted season ratings.

### 6. API Integration
- The Flask API accepts player data and returns predictions in real time.
- Hosted on Hugging Face for scalable, production-ready access.

---

## 📁 Project Structure

```
Score_Rate_Prediction_webApp/
├── Data/                       # Raw and processed datasets
├── Notebooks/                  # Jupyter notebooks (EDA, feature engineering, modeling)
├── templates/                  # HTML templates for the Flask web interface
├── Database_PostgreSQL.py      # PostgreSQL database integration (reads config from env vars)
├── Dockerfile                  # Container configuration for deployment
├── app.py                      # Flask application entry point (routes: /, /predict, /predict_api)
├── player_rating_model.pkl     # Serialized trained model
├── requirements.txt            # Python dependencies
├── .env.example                # Template for local DB environment variables
└── LICENSE                     # Apache 2.0 License
```

---

## 🛠️ Tech Stack

- **Language:** Python
- **Modeling:** scikit-learn (RandomForestRegressor)
- **Data Handling:** pandas, joblib
- **Web Framework:** Flask
- **WSGI Server:** Gunicorn
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Deployment:** Hugging Face Spaces

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip
- (Optional) Docker, if you'd rather run the app in a container

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abdulrahman0700/Score_Rate_Prediction_webApp.git
   cd Score_Rate_Prediction_webApp
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   The app will start locally — by default Flask apps run on `http://127.0.0.1:5000/`.

### Running with Docker

```bash
docker build -t score-rate-prediction .
docker run -p 7860:7860 --env-file .env score-rate-prediction
```

### Configuration

Database logging (see [Database integration](#-database-integration) below) is configured via environment variables rather than hardcoded credentials. Copy the example file and fill in real values:

```bash
cp .env.example .env
```

| Variable | Description | Default |
|---|---|---|
| `DB_HOST` | PostgreSQL host | `localhost` |
| `DB_NAME` | Database name | `postgres` |
| `DB_USER` | Database user | `postgres` |
| `DB_PASSWORD` | Database password | *(required)* |
| `DB_PORT` | Database port | `5432` |

If no database is reachable, the app still starts and serves predictions — it just skips writing rows to Postgres and logs a warning at startup.

---

## 🔌 Usage

Once running, the web interface (`/`) lets you fill in a form with a player's stats and returns a predicted season rating on the page.

There are two prediction endpoints:

### `POST /predict` — form-based (used by the web UI)

Submitted via the HTML form in `templates/home.html`. Expects form fields, in order: `Teams, Seasons, Players, Matches, Goals, Assists`. Returns the rendered `home.html` page with the prediction text inserted.

### `POST /predict_api` — JSON (for programmatic use / Postman)

```bash
curl -X POST http://127.0.0.1:5000/predict_api \
  -H "Content-Type: application/json" \
  -d '{
        "data": {
          "Teams": "Example FC",
          "Seasons": "2023-2024",
          "Players": "Example Player",
          "Matches": 30,
          "Goals": 12,
          "Assists": 8
        }
      }'
```

Response:

```json
{"prediction": [7.42]}
```

If a database connection is configured, each call to `/predict_api` also logs the submitted row to the `Football` table in PostgreSQL.

> The model is also hosted on Hugging Face, so it can be called remotely via their inference API without running the app locally.

---

## 🗄️ Database Integration

`Database_PostgreSQL.py` defines a small `database` class used by the `/predict_api` route to persist submitted player rows to a PostgreSQL table (`Football`). It uses parameterized queries throughout to avoid SQL injection, and reads its connection settings from environment variables (see [Configuration](#configuration)) instead of hardcoded credentials.

---

## 📊 Model Performance Summary

The RandomForestRegressor achieves strong predictive performance, explaining **92% of the variance** in player season ratings (R² = 0.92), with a low average prediction error (MAE = 0.65).

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Abdulrahman**
GitHub: [@abdulrahman0700](https://github.com/abdulrahman0700)
