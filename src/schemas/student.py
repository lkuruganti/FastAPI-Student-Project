from pydantic import BaseModel 
from typing import List, Optional
import datetime


# Base class for Student 
class StudentBase(BaseModel):
    student_name: str 
    student_class: str
    first_year_marks: float  
    second_year_marks: Optional[float] = None
    third_year_marks: Optional[float] = None
    final_year_marks: Optional[float] = None
    created_at: datetime.datetime
    
    
# List all Students  
class StudentList(StudentBase):
    id: int
    aggregate_marks: float
    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime] = None
    
    class Config:
        orm_mode = True
        
        
# Create New Student        
class StudentCreate(StudentBase):
    pass 


# Update Student Details
class StudentUpdate(StudentBase):
    updated_at: datetime.datetime
    
    