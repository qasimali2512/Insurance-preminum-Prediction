from fastapi import FastAPI
from Schema.user_input import UserInput
from model.predict import predict_output
from fastapi.responses import JSONResponse
from Schema.prediction_response import PredictionResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get('/')
# def home():
#     return {
#         'message': 'Welcome to Insurance Premium Prediction API'
#     }


@app.get('/health')
def health_check():
    return {
        'status': 'ok'
    }


@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'lifestyle_risk': data.lifestyle_risk,
        'age_group': data.age_group,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction, confidence = predict_output(user_input)

        return PredictionResponse(
            predicted_category=prediction,
            confidence=confidence
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                'error': str(e)
            }
        )
        
    #React Frontend
        
frontend_dist = "insurance-frontend/dist"

if os.path.exists(frontend_dist):

    app.mount(
        "/assets",
        StaticFiles(directory=f"{frontend_dist}/assets"),
        name="assets"
    )

    @app.get("/{full_path:path}")
    async def serve_react(full_path: str):
        index_path = os.path.join(frontend_dist, "index.html")

        if os.path.exists(index_path):
            return FileResponse(index_path)

        return {
            "error": "Frontend build not found"
        }