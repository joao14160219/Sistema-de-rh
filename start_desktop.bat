@echo off
cd /d "%~dp0"

REM Usa SEMPRE o python da venv
".venv\Scripts\python.exe" desktop\main.py
