@echo off
REM Change directory to the app folder
cd /d C:\apps\ocr

REM Clear any previous FLASK_APP variable
set FLASK_APP=
set FLASK_ENV=development

REM Set FLASK_APP correctly
set FLASK_APP=app.py

REM Run Flask without auto-reloader
python -m flask run --no-reload

pause
