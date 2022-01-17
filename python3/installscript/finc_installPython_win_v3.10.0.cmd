@echo OFF
::
cls
:: Prompt for user to Really run this script
setlocal
set Value="n"
:PROMPT
SET /P Value=Are you sure installing Python-3.10.0 (y/[n])?
IF /I "%Value%" NEQ "y" GOTO END

:: This batch file will show details Windows 10, and install Python v3.10.0
TITLE Install Python Software on Windows 7/8/9/10/11
echo.Checking system information.
timeout /T 2 > nul

:: Switch to Downloads early on
cd %userprofile%/Downloads

echo.
echo.
:: Section 1: Windows 10/11 information.
echo.============================
echo.WINDOWS INFO
echo.============================
echo.
systeminfo | findstr /c:"OS Name"
systeminfo | findstr /c:"OS Version"
systeminfo | findstr /c:"Hyper-V Requirements"

:: Quick Pause
echo.
timeout /T 2 > nul

echo.
echo.
:: Section 2: Hardware information.
echo.============================
echo.HARDWARE INFO
echo.============================
echo.
systeminfo | findstr /c:"Total Physical Memory"
systeminfo | findstr /c:"Virtual Memory: In Use"

:: Quick Pause
echo.
timeout /T 2 > nul

echo.
:: Section 3: Python Download.
echo.============================
echo.Checking Existing Python
echo.============================
echo.
::
echo. Checking for existing version of Python
::
::
:: https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
IF EXIST "python-3.10.0-*.<" (
  echo.Found existing version of Python 3.10.0
  del python-3.10.0-amd64.exe
  echo.Deleting existing version of Python
  echo.
  timeout /T 2 > nul
) ELSE (
  timeout /T 2 > nul
  echo.No existing version of python 3.10.0 Found.
  echo.
)
::
:: Quick Pause
timeout /T 2 > nul
::
IF EXIST "python-3.9.*.<" (
  echo.Found existing version of Python 3.9.*
  del python-3.9.*.*
  echo.Deleting existing version of Python
  echo.
  timeout /T 2 > nul
) ELSE (
  timeout /T 2 > nul
  echo.No existing version of python 3.9 Found.
  echo.
)
echo.
echo.you may need to press ENTER, 
echo.If the wait time is more than 10 seconds.
::
:: Quick Pause
timeout /T 2 > nul
::
IF EXIST "python-3.8.*.<" (
  echo.Found existing version of Python 3.8.*
  del python-3.8.*.*
  echo.Deleting existing version of Python
  echo.
  timeout /T 2 > nul
) ELSE (
  timeout /T 2 > nul
  echo.No existing version of python 3.8 Found.
  echo.
)
echo.
echo.you may need to press ENTER, 
echo.If the wait time is more than 10 seconds.
::
:: Quick Pause
echo.
timeout /T 2 > nul
::
:: Check to see if bitsadmin is located here
echo.
echo.
:: Section 3: Bitsadmin Download.
echo.============================
echo.Checking Bitsadmin
echo.============================
echo.
::
IF EXIST C:\Windows\SysWOW64\bitsadmin.exe (
  echo.Bitsadmin is installed on your Windows 7/8/9/10/11 system.
  echo.Will download Python 3 software.
  echo.
  timeout /T 2 > nul
) ELSE (
  timeout /T 2 > nul
  echo.Apparently, Bitsadmin.exe not found.
  echo.Raise your hand and ask Instructor for help.
  echo.
  goto end
)
::
:: Quick Pause
timeout /T 2 > nul
::
echo.
echo.
:: Section 3: Python Download.
echo.============================
echo.Downloading Python
echo.============================
echo.
::
echo.Downloading Python Software.
::
::
timeout /T 2 > nul
echo.
echo.
C:\Windows\SysWOW64\bitsadmin.exe /transfer PythonDownload /download /priority normal https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe %userprofile%\Downloads\python-3.10.0-amd64.exe
::
echo.
echo.
timeout /T 1 > nul
timeout /T 1 > nul
echo.Checking to see if this python file has been downloaded.
::
IF EXIST python-3.10.0-amd64.exe (
  echo.Python file has been Found.
  echo.Will now Install this Software.
  echo.
  timeout /T 2 > nul
) ELSE (
  timeout /T 2 > nul
  echo.Software not found.
  echo.Perhaps, try to run this file again.
  echo.
  goto end
)
echo.Finish downloading the Python Software.
echo.
::
echo.
echo.
:: Section 4: Python Installation.
echo.============================
echo.Installing Python
echo.============================
echo.
echo.Installing Python version 3.10.0
echo.This process will take as much as 15 mins if there is no SSD.
echo.
echo.Go grab Koffie or something before coming back to your Laptop.
:: Installing Python
::
%userprofile%\Downloads\python-3.10.0-amd64.exe /quiet InstallAllUsers=0 TargetDir=C:\Python310 AssociateFiles=1 CompileAll=1 PrependPath=0 Shortcuts=0 Include_doc=1 Include_debug=0 Include_dev=0 Include_exe=1 Include_launcher=1 InstallLauncherAllUsers=1 Include_lib=1 Include_pip=1 Include_symbol=0 Include_tcltk=1 Include_test=1 Include_tools=1
::
echo.
echo.
echo.Compiling and Installing Python modules........
echo.
:: TIMEOUT 40
:: Quick Pause
timeout /T 2 > nul
echo.
set num=40
for /L %%I IN (1, 1, %num%) do (
  echo. | set /p="%%I " 
  timeout /T 1 > nul
)
echo.
echo.
echo.Finished Installing Python Software
echo.
echo.
::
echo.Be Patient, Almost done.
::
echo.
echo.
:: Section 4: Third Party Software Installation.
echo.============================
echo.Installing Finance  Software
echo.============================
echo.
echo.
::
:: Checking the file to see if it was made
::
echo.
echo.
:check
if exist C:\Python310\Tools\pynche\Main.py (
    echo.Checking Files if Python has been installed.....
    timeout /T 3 > nul
    echo.
    echo. Python Software has been Installed.
) else (
    echo. Python has not been installed.
    timeout /T 1 > nul
    echo.
    timeout /T 1 > nul
    echo.Problem with installation. PRESS: CTRL-C to End Installation process only if after three printed messages.
    goto check
)
::
echo.
echo.
echo.Updating pip the module manager tool.
::
:: Updating pip on Windows
C:\Python310\python.exe -m pip install --upgrade pip
::
:: Quick Pause
timeout /T 2 > nul
echo.
echo.Finished Updating pip.
::
:: Waiting for the previous process to finish
::
echo.
echo.
echo.Installing Additional required Modules
echo.PRESS ENTER HERE If wait time is Longer than 8 seconds
:: Quick Pause
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user wheel
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user pandas_datareader requests ta scipy numpy plotly
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user pandas matplotlib seaborn statsmodels QuantLib pyfinlab
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user yfinance PyAlgoTrade Statistics-pyt backtrader
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user arrow prettypandas beautifier tabulate
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user keras BeautifulSoup4 scrapy
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user nltk pybrain
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user pydot pygal
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: To download unbuildable packages: go to UC Irvine
:: https://www.lfd.uci.edu/~gohlke/pythonlibs
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo.
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::  Cant install these things via pip on windows
::  Failed to build numba llvmlite scikit-learn
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo.
timeout /T 1 > nul
::
echo.
echo.Finished installing Modules.
echo.
::
echo.
echo.
:: Section 4: Execute runme.bat.
echo.============================
echo.Execute runme.bat
echo.============================
echo.
echo.
::
echo set PATH=C:\Python310;%PATH% > %userprofile%\runme.bat
del /s %userprofile%\Downloads\python-3.10.0-amd64.exe >nul 2>&1
call %userprofile%\runme.bat
echo.
echo.
python -c "print(\"Welcome, Python installation Success.\")"
echo.
echo.
:end
