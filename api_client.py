# apli_client.py
# Usage from command line:
# curl http://127.0.0.1:5000 -X POST -H "Content-Type: application/json" -d '{"bathrooms": "2", "bedrooms": "3", "sqft_living": "1800", "sqft_lot": "2200", "floors": "1", "waterfront": "1", "condition": "3"}'
#
import requests


def make_request():
    """Make a request to the API server"""

    url = "http://127.0.0.1:5000"

    data = {
        "bathrooms": "2",
        "bedrooms": "3",
        "sqft_living": "1800",
        "sqft_lot": "2200",
        "floors": "1",
        "waterfront": "1",
        "condition": "3",
    }

    response = requests.post(url, json=data, timeout=5)

    print(response.text)


if __name__ == "__main__":
    make_request()

    
    
    
 
















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    """Build, deploy and access a model using scikit-learn"""

import pickle

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house_data.csv", sep=",")

features = df[
    [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "waterfront",
        "condition",
    ]
]

target = df[["price"]]

estimator = LinearRegression()
estimator.fit(features, target)

print(estimator.coef_)
print(estimator.intercept_)

with open("house_predictor.pickle", "wb") as file:
    pickle.dump(estimator, file)
    
    
    
    
    
    
    
