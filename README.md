# Credits

This project is based on the work from [AchilleasKn/flask_api_python](https://github.com/AchilleasKn/flask_api_python).

# Iris Classifier Web Application

This project is a full-stack web application for classifying Iris flower species using a machine learning model. It consists of a Python Flask API backend and a Streamlit frontend, both containerized with Docker for easy deployment.

## Features

- **Machine Learning Model:**  
  Trained on the classic Iris dataset using the K-Nearest Neighbors (KNN) algorithm (`n_neighbors=1`) for perfect accuracy on the training data.
- **REST API:**  
  A Flask-based API that serves predictions from the trained model.
- **Interactive Frontend:**  
  A Streamlit web app for users to input flower features and receive instant predictions.
- **Dockerized:**  
  Both backend and frontend run in isolated containers, orchestrated with Docker Compose.

---

## Project Structure

```
flask_api_python/
│
├── api/                  # Backend Flask API
│   ├── api.py            # Main API application
│   ├── iris_model.pkl    # Serialized ML model
│   ├── requirements.txt  # Python dependencies for backend
│   ├── Dockerfile        # Dockerfile for backend
│
├── frontend/             # Streamlit frontend
│   ├── app.py            # Main Streamlit app
│   ├── requirements.txt  # Python dependencies for frontend
│   ├── Dockerfile        # Dockerfile for frontend
│
├── model/                # Model training notebook
│   └── Iris_model.ipynb  # Jupyter notebook for training and exporting the model
│
├── docker-compose.yml    # Orchestration for backend and frontend
└── README.md             # Project documentation
```

---

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/) installed on your system.

### Build and Run

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Build and start the application:**

   ```sh
   docker compose up --build
   ```

3. **Access the frontend:**

   - Open your browser and go to [http://localhost:8501](http://localhost:8501)

4. **API endpoint (optional):**
   - The backend API is available at [http://localhost:5000](http://localhost:5000)

---

## How It Works

- The **backend** (`api/`) loads a pre-trained KNN model (`iris_model.pkl`) and exposes a `/predict` endpoint for predictions.
- The **frontend** (`frontend/`) provides a user-friendly interface to input flower measurements and displays the predicted Iris species.
- Both services are defined in `docker-compose.yml` and communicate over a Docker network using service names.

---

## Model Training

- The model is trained in the `model/Iris_model.ipynb` notebook using the K-Nearest Neighbors algorithm with `n_neighbors=1`.
- The trained model is saved as `api/iris_model.pkl` and used by the Flask API for inference.

---

## Customization

- To retrain or update the model, modify and run the Jupyter notebook in `model/`, then replace the `iris_model.pkl` file in `api/`.
- To change the frontend or backend logic, edit the respective files in `frontend/` or `api/` and rebuild the containers.

---

## License

[MIT License](LICENSE)  
Feel free to use, modify, and distribute this project.

---

## Acknowledgements

- [Scikit-learn](https://scikit-learn.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Streamlit](https://streamlit.io/)
- [Docker](https://www.docker.com/)

---

**Enjoy classifying Iris flowers!**
