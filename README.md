# RetailPulse

RetailPulse is a retail analytics and demand forecasting application built using Python and Streamlit.

## Features

- Sales Analysis
- Demand Forecasting
- Customer Segmentation
- Interactive Dashboard
- Data Visualization

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- Docker
- Kubernetes

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd RetailPulse
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run main.py
```

## Docker

Build image:

```bash
docker build -t retailpulse .
```

Run container:

```bash
docker run -p 8501:8501 retailpulse
```

## Kubernetes

Deploy application:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## Project Structure

```text
RetailPulse/
├── main.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
└── README.md
```

## Author

Aryan Yadav