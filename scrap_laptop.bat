@echo off

REM Activate the virtual environment
call ".\venv\Scripts\activate.bat"

REM Now run the scripts using python from the venv
python "C:\Users\yongz\OneDrive - Singapore University of Technology and Design\myproject\carousell scrapper\carousell scrapping\batch_scrapping.py"

python "C:\Users\yongz\OneDrive - Singapore University of Technology and Design\myproject\carousell scrapper\carousell scrapping\scrap_main.py"

REM Remove pause for scheduled runs
REM pause

