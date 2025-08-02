# Electricity Cost Prediction

This project predicts electricity cost using a PyTorch regression model served via a FastAPI API.  
It includes a Streamlit frontend for interactive user input and visualization.

## Features

- **FastAPI backend** for model inference
- **PyTorch regression model**
- **Streamlit frontend** for user-friendly predictions
- Ready for deployment on Render (free cloud hosting)

## Demo Links

- **FastAPI API:** [https://electricity-cost-prediction-luz2.onrender.com/docs](https://electricity-cost-prediction-luz2.onrender.com/docs)
- **Streamlit Frontend:** [https://electricity-cost-prediction-with-fronted.onrender.com/](https://electricity-cost-prediction-with-fronted.onrender.com/)

*(Replace these URLs with your actual Render links after deployment.)*

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/electricity-cost-prediction.git
   cd electricity-cost-prediction
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run FastAPI backend:**
   ```bash
   uvicorn api.main:app --reload
   ```

4. **Run Streamlit frontend:**
   ```bash
   streamlit run src/frontend.py
   ```

## Deployment

- Deploy both FastAPI and Streamlit as separate services on [Render](https://render.com/).
- Update the API URL in `frontend.py` to point to your FastAPI Render URL.

## Environment Variables

For Streamlit on Render, set:
- `API_URL=https://your-fastapi-app.onrender.com`

## Project Structure

```
├── api/
│   └── main.py           # FastAPI backend
├── src/
│   ├── model.py          # PyTorch model definition
│   ├── train.py          # Model training script
│   └── frontend.py       # Streamlit frontend
├── results/
│   └── electricity_cost_regressor.pth  # Trained model
├── requirements.txt
├── README.md
```
