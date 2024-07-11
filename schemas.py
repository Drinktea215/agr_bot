from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class SalarySchemas(BaseModel):
    dt_from: datetime = Field(default=None, json_schema_extra={
        "format": "date-time",
        "example": "2023-04-05T12:34:56"
    })
    dt_upto: datetime = Field(default=None, json_schema_extra={
        "format": "date-time",
        "example": "2023-04-05T12:34:56"
    })
    group_type: str

    @field_validator("dt_from", "dt_upto")
    def parse_date(cls, v):
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        return v
