# student-csv app

# After setting up virtual env with required installed libraries from requirement.txt.

# To set up virtual env for linux based system please follow these steps:

<!-- #install virtualenv
sudo apt-get install virtualenv

#create virtualenv
virtualenv -p python3 "student_env" -->


# All set to go

# Alembic is used here to track database migrations.

# For database migrations and table creation/updation in database:(For this project do'nt need to worry about  database installation in your system and and performing migration steps as i have connected this project with sqlite database which is itself in this project).

# Run these commands in terminal after database installation in your local if you want some other new database:

# "alembic upgrade head" (To sync with migration versioning)

# " alembic revision --autogenerate -m "all table initiation" " (To create sqlalchemy migrations in alembic folder as migration files) (This step can be skiped if migrations are already made)

# Again run to finally migrate: "alembic upgrade head"

# And now run server:

# uvicorn main:app --reload

# Api doc swagger url:

# http://localhost:8000/docs

# Open Api doc:

# http://localhost:8000/redoc

# Front end url of application:

# http://localhost:8000/v1/
