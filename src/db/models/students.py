from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func

from db.base import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    grade = Column(String)
    pgroup = Column(String)
    group = Column(String)
    subject = Column(String, nullable=True)
    total_students = Column(Integer, nullable=True)
    buffer_size = Column(Integer)
    is_physical = Column(String)
    student = Column(String)
    marks = Column(Integer)
    location = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)