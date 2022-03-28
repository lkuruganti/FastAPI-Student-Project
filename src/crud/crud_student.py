from fastapi import UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


from datetime import datetime
import pandas as pd 
import numpy as np
import random

# self packages
from db.models.students import Student



def get_students(db: Session):
    """ get all students from the database """
    try:
        result = []

        students_list = db.query(Student).all()
        result.append(students_list)
        
        location_name = db.query(Student.location).all()
        locations = list(dict.fromkeys(location_name))
        chart_anlaysis = []
        for loc in locations:
            student_count = db.query(Student).filter(Student.location == loc[0]).count()
            loc_data = {}
            loc_data["location_name"] = loc[0]
            loc_data["student_count"] = student_count 
            chart_anlaysis.append(loc_data)

        result.append(chart_anlaysis)
        
        
        return result
        
    except Exception as e:
        detail = {
            'msg': str(e),
            'alert': "error",
        }
        return detail




def student_data(csv_file):
    
    df = pd.read_csv(csv_file.file)

    df.interpolate()

    new_df = df.fillna(method="ffill")
    
    # random data for null values
    PGROUP = ['BPC', 'MPC']
    GRADE = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12']
    GROUP = ['Biology', 'Math', 'Physics', 'English', 'History', 'Hindi', 'Marathi']
    LOCATION = ['Chennai', 'Banglore', 'Delhi', 'Pune', 'Mumbai', 'Jalgaon']
    SUBJECT = ['Biology1', 'Math2', 'Physics1', 'English2', 'History1', 'Hindi2', 'Marathi3']

    random.shuffle(PGROUP)
    p_group = PGROUP[0]
    
    random.shuffle(GRADE)
    grade = GRADE[0]
    
    random.shuffle(GROUP)
    group = GROUP[0]
    
    random.shuffle(LOCATION)
    location = LOCATION[0]
    
    random.shuffle(SUBJECT)
    subject = SUBJECT[0]
    """
    new_df = df.fillna({
        'Grade': grade,
        'Pgroup': p_group,
        'Group': group,
        'Subject': subject,
        'Virtual class/Physical': 'True', 
        'Location': location,
    })    
    """
    return new_df





    
    
def upload_csv_data_database(csv_file: UploadFile, db: Session):
    try:
        
        """
            Check validation for csv file
            Extract data from csv file
            Upload to the database  
        """
        
        df = student_data(csv_file)
        print("ttttttt",df)
        if df.empty:
            detail = {
                    "msg": "CSV file is empty!!",
                    "alert": "warning",
                }
            return detail
        
        for index, row in df.iterrows():
            
            student = db.query(Student).filter(Student.student == row["Student"]).first()
            
            if not student:
    
                student = Student(
                    grade=str(row["Grade"]),
                    pgroup= str(row["Pgroup"]),
                    group= str(row["Group"]),
                    subject = str(row["Subject"]),
                    total_students = int(row["Total students"]),
                    buffer_size = int(row["Buffer"]),
                    is_physical = str(row["Virtual class/Physical"]),
                    student = str(row["Student"]),
                    marks = int(row["Marks"]),
                    location = str(row["Location"]),
                    created_at = datetime.now(),
                )
                db.add(student)
                db.commit()
                db.refresh(student)
                
            else:
                continue

        
        detail = {
            "msg": "CSV Data Uploaded to database successfully!!",
            "alert": "success",
        }
        return detail
        
    
    except Exception as e:
        detail = {
            'msg': str(e),
            'alert': "error",
        }
        return detail
    
    
    
