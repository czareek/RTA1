from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/api/v1.0/predict")
def predict(x1: float = Query(0), x2: float = Query(0)):
    total = x1 + x2
    prediction = 1 if total > 5.8 else 0
    return {
        "prediction": prediction,
        "features": {"x1": x1, "x2": x2, "sum": total}
    }