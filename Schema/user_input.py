from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities,tier_2_cities 

# pydantic model for validate incoming data
class UserInput(BaseModel):
    age: Annotated[
        int,
        Field(..., gt=0, lt=120, description='Age of the User')
    ]

    weight: Annotated[
        float,
        Field(..., gt=0, description='Weight of the User')
    ]

    height: Annotated[
        float,
        Field(..., gt=0, description='Height of the User')
    ]

    income_lpa: Annotated[
        float,
        Field(..., description='Income of the User')
    ]

    smoker: Annotated[
        bool,
        Field(..., description='Smoker status of the User')
    ]

    city: Annotated[
        str,
        Field(..., description='City of the User')
    ]

    occupation: Annotated[
        Literal[
            'retired',
            'student',
            'freelancer',
            'government_job',
            'private_job',
            'business_owner',
            'unemployed',
        ],
        Field(..., description='Occupation of the User')
    ]

    @field_validator('city')
    @classmethod
    def nomlaize_city(cls, v: str) -> str:
        return v.strip().title()

    @computed_field
    @property
    def bmi(self) -> float:
        return round(
            self.weight / ((self.height / 100) ** 2),
            2
        )

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return "senior"

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3