"""
    This Model Contains the Hospital Model Initialization

    Attributes:


"""
from models.base_model import Base, BaseModel


class Hospital(Base, basemodel):
    """Representation of hospitals"""
    __tablename__ = "hospitals"
    name = 