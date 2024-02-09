#!/usr/bin/python3
"""class Review from BaseModels"""
from models.base_models import BaseModels


class Review(BaseModel):
    """Review"""
    place_id = ""
    user_id = ""
    text = ""
