@echo off
setlocal

:: Auto-detect venv
if exist ".venv\Scripts\activate.bat" (
    set VENV_DIR=.venv\Scripts
) else if exist "venv\Scripts\activate.bat" (
    set VENV_DIR=venv\Scripts
) else (
    echo ❌ No virtual environment found. Please create one.
    exit /b 1
)

:: Create reports folder if not exists
if not exist reports mkdir reports

:: Create timestamp
set DATESTAMP=%date:~-4%-%date:~7,2%-%date:~4,2%_%time:~0,2%-%time:~6,2%
set DATESTAMP=%DATESTAMP: =0%

:: Define report folders
set ALLURE_RESULTS=reports\allure-results-%DATESTAMP%
set ALLURE_REPORT=reports\allure-report-%DATESTAMP%

:: Path to previous history (latest report)
set PREV_REPORT=reports\allure-report-latest
set HISTORY_FOLDER=%PREV_REPORT%\history

echo === Running API tests with Pytest + Allure ===
%VENV_DIR%\pytest --alluredir=%ALLURE_RESULTS% -q
if errorlevel 1 (
    echo ❌ Tests failed. Skipping report generation.
    exit /b 1
)

echo === Generating Allure Report ===
if exist "%HISTORY_FOLDER%" (
    echo 🔄 Preserving history from previous report
    mkdir "%ALLURE_RESULTS%\history"
    xcopy "%HISTORY_FOLDER%" "%ALLURE_RESULTS%\history" /E /I /Y
)

allure generate "%ALLURE_RESULTS%" -o "%ALLURE_REPORT%"

:: Save latest report path
if exist "%PREV_REPORT%" rmdir /s /q "%PREV_REPORT%"
xcopy "%ALLURE_REPORT%" "%PREV_REPORT%" /E /I /Y

echo === Opening Allure Report in Chrome ===
explorer "%ALLURE_REPORT%\index.html"

echo ✅ Allure report generated -> %ALLURE_REPORT%\index.html

endlocal
pause
