from pydantic import BaseModel , Field, field_validator
from typing import Literal

class UserInput(BaseModel):
    total_orders:int = Field(...,gt=0,description="Total number of orders placed by the user")
    total_returns:int = Field(...,ge=0,description="Total number of returned ")
    order_value:float = Field(...,gt=0,description="Value of the current order")
    acc_age_days:int=Field(...,ge=0, description="Age of the user account in days")
    days_since_last_return:int =Field(...,ge=0, description="Days since last return")
    return_last_7_days:int =Field(...,ge=0,description="Number of returns in last 7 days")
    product_category:Literal[
        "electronics",
        "fashion",
        "home",
        "beauty_&_self_care",
        "fitness_&_sports",
        "toys_&_kids"
    ]
    return_reason:Literal[
        "damaged",
        "not_needed",
        "wrong_item",
        "size_issue"
    ]





    @field_validator("product_category", "return_reason", mode="before")
    def clean_input(cls,value):
        return value.strip().lower()




