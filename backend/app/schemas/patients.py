
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class PatientCreate(BaseModel):
    patient_code: str = Field(min_length=2, max_length=50)
    full_name: str = Field(min_length=1, max_length=150)
    age: int = Field(ge=0, le=120)
    sex: str = Field(min_length=1, max_length=30)


class PatientResponse(BaseModel):
    id: int
    patient_code: str
    full_name: str
    age: int
    sex: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)