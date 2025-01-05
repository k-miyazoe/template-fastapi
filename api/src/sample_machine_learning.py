from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

router = APIRouter()

# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "iris_model.pkl")

# Load the model
model = joblib.load("iris_model.pkl")

class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class IrisResponse(BaseModel):
    prediction: str

@router.post("/predict", response_model=IrisResponse)
async def predict_iris(data: IrisRequest):
    try:
        prediction = model.predict([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
        predicted_class = iris.target_names[prediction[0]]
        return IrisResponse(prediction=predicted_class)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))