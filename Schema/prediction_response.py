from pydantic import BaseModel,Field

class PredictionResponse(BaseModel):
    predicted_category:str=Field(...,
        description="The predicted category",
        example="Low"
    )
    confidence: float=Field(...,
        description="The confidence of the prediction",
        example=0.5
    )

