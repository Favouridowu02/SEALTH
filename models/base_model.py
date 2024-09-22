#!/usr/bin/python3
"""
    This is Model contains the BaseModel and the Base

    BaseModel: This is the foundation of order classes Models
"""


from datetime import datetime
from dotenv import load_dotenv
import models
from os import getenv
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
load_dotenv()


class BaseModel:
    """
        This is the BaseModel
    """
    if model.storage == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
    def __init__(self, *args, **kwargs):
        """This is the In"""
