@echo off

REM Create and activate virtual environment
python -m venv venv
call venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Run the Flask app
python app.py