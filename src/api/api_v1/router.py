from fastapi import APIRouter, Request, Depends, UploadFile, File
from sqlalchemy.orm import Session

# pagination
from fastapi_pagination import Page, paginate

# templates
from fastapi.templating import Jinja2Templates

# Database Dependency
from db.base import get_db

# self packages
from crud.crud_student import (
    get_students,
    upload_csv_data_database,
)


routers = APIRouter(
	prefix="/v1",
	tags=['AUTH API'],
)


templates = Jinja2Templates(directory="templates")


#  return homepage with students_list
@routers.get('/')
def homepage(request: Request, db: Session = Depends(get_db)):
    try:
        result = get_students(db)
        print(result)
        student_list = result[0]
        chart_analysis = result[1]
        return templates.TemplateResponse("index.html", {"request": request, "students": student_list, "chart_analysis": chart_analysis })
    
    except Exception as e:
        return str(e)



# upload csv data to database
@routers.post('/')
def upload_data(request: Request, db: Session = Depends(get_db), csv_file: UploadFile = File(...)):
    try:
        result = upload_csv_data_database(csv_file, db)
        students = get_students(db)
        
        return templates.TemplateResponse("index.html", {"request": request, "result": result, "students": students})
    
    except Exception as e:
        return str(e)