from pydantic import BaseModel
from typing import Literal, Union
from datetime import date



class ExperimentDTO(BaseModel):
    test_type: Literal['Two-Sided-Test', 'One-Sided-Test']
    start_date: date
    customer_type: Literal['b2b', 'b2c', 'b2c and b2b']
    device_type: Literal[
        'mobile', 
        'consumer app', 
        'desktop', 
        'desktop and consumer app', 
        'desktop and mobile', 
        'mobile and consumer app', 
        'all three'
    ]
    browser_type: Literal[
        'apple', 
        'google', 
        'microsoft', 
        'apple and google', 
        'apple and microsoft', 
        'google and microsoft', 
        'all three'
    ]