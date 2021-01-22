@echo OFF
::
:: This was one of the most complicated software 
:: i had ever written in DOS scripting !
:: 
cls
:: Prompt for user to Really run this script
setlocal
set Value="n"
:PROMPT
SET /P Value=Are you sure (y/[n])?
IF /I "%Value%" NEQ "y" GOTO END

:: This batch file will show details Windows 10, and install Python v3.8.7.
TITLE Install Python Software on Windows 7/8/9/10
echo.Checking system information.
TIMEOUT /T 2 > nul

:: Switch to Downloads early on
cd %userprofile%/Downloads

echo.
echo.
:: Section 1: Windows 10 information.
echo.============================
echo.WINDOWS INFO
echo.============================
echo.
systeminfo | findstr /c:"OS Name"
systeminfo | findstr /c:"OS Version"
systeminfo | findstr /c:"Hyper-V Requirements"

:: Quick Pause
echo.
TIMEOUT /T 2 > nul

echo.
echo.
:: Section 2: Hardware information.
echo.============================
echo.HARDWARE INFO
echo.============================
echo.
systeminfo | findstr /c:"Total Physical Memory"
systeminfo | findstr /c:"Virtual Memory: In Use"
:: wmic diskdrive GET index,caption,name,size /format:table
:: wmic diskdrive GET index,Model,SerialNumber,Size,Status


:: Quick Pause
echo.
TIMEOUT /T 2 > nul

echo.
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
IF EXIST "python-3.8.6-*.<" (
  echo.Found existing version of Python 3.8.6
  del python-3.8.6-amd64.exe
  echo.Deleting existing version of Python
  echo.
  TIMEOUT /T 2 > nul
) ELSE (
  TIMEOUT /T 2 > nul
  echo.No existing version of python 3.8.6 Found.
  echo.
)
::
TIMEOUT /T 2 > nul
::
IF EXIST "python-3.8.7-*.<" (
  echo.Found existing version of Python 3.8.7
  del python-3.8.7-amd64.exe
  echo.Deleting existing version of Python
  echo.
  TIMEOUT /T 2 > nul
) ELSE (
  TIMEOUT /T 2 > nul
  echo.No existing version of python 3.8.7 Found.
  echo.
)

:: Quick Pause
echo.
TIMEOUT /T 5 > nul

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
TIMEOUT /T 2 > nul
echo.
echo.
bitsadmin /transfer PythonDownload /download /priority normal https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe %userprofile%\Downloads\python-3.8.6-amd64.exe

:: Quick Pause
echo.
echo.
TIMEOUT /T 1 > nul
TIMEOUT /T 1 > nul
echo.Checking to see if this python file has been downloaded.

IF EXIST python-3.8.6-amd64.exe (
  echo.Python file has been Found.
  echo.Will now Install this Software.
  echo.
  TIMEOUT /T 4 > nul
) ELSE (
  TIMEOUT /T 3 > nul
  echo.Software not found.
  echo.Perhaps, try to run this file again.
  echo.
  goto end
)
echo.Finish downloading the Python Software.
echo.

echo.
echo.
:: Section 4: Python Installation.
echo.============================
echo.Installing Python
echo.============================
echo.

echo.
echo.Installing Python version 3.8.6.
echo.This process will take as much as 15 mins if there is no SSD.
echo.
echo.Go grab Koffie or something before coming back to your Laptop.
:: This python install process is weird, it will simply return prompt once it had been executed but the process
:: will not be 100 percent completed before continuing as we have learned.
:: Came across another problem where installAllusers must be 0
:: before the Python38 dir will stay around in the C:\ driectory
%userprofile%\Downloads\python-3.8.6-amd64.exe /quiet InstallAllUsers=0 TargetDir=C:\Python38 AssociateFiles=1 CompileAll=1 PrependPath=0 Shortcuts=0 Include_doc=1 Include_debug=0 Include_dev=0 Include_exe=1 Include_launcher=1 InstallLauncherAllUsers=1 Include_lib=1 Include_pip=1 Include_symbol=0 Include_tcltk=1 Include_test=1 Include_tools=1
::
::
:: This is quite sensitive wait time during installation.
:: It is compiling and creating all the dirs before all
:: files are compiled. It then do other things too.
:: Not sure what would be a good wait time before moving onto the next process.
:: it is wise to wait for atleast 3 mins actually due to compilation
:: of lots of tiny files inside python.
::
echo.
echo.Still compiling Python modules........
:: TIMEOUT 400
:: Buffer Zone
TIMEOUT /T 2 > nul
echo.
SET num=389
for /L %%I IN (1, 1, %num%) do (
  echo. | set /p="%%I " 
  TIMEOUT /T 1 > nul
)
echo.
echo.
echo.Finished Installing Python Software
echo.
echo.
::
::
echo.Be Patient, Almost done.
::
::
echo.
echo.
:: Section 4: Third Party Software Installation.
echo.============================
echo.Installing Third Party Software
echo.============================
echo.
::
:: Checking the file to see if it was made
::
echo.
:check
if exist C:\Python38\Tools\pynche\Main.py (
    echo.Checking Files if they were Created.....
    TIMEOUT /T 4 > nul
    echo.
    echo.They were created.
) else (
    echo.Files still not created.....
    echo.Still compiling code, maybe.
    TIMEOUT /T 4 > nul
    echo.
    TIMEOUT /T 4 > nul
    echo.Problem with installation. PRESS: CTRL-C to End Installation process only if after three printed messages.
    goto check
)

echo.
echo.
echo.Updating pip the module manager tool.
::
:: Updating pip on Windows
C:\Python38\python.exe -m pip install --upgrade pip
::
TIMEOUT /T 3 > nul
echo.
echo.Finished Updating pip.
::
:: Waiting for the previous process to finish
::
echo.
echo.
echo.Installing Additional required Modules
TIMEOUT /T 4 > nul
C:\Python38\scripts\pip.exe install --user requests diceware scipy numpy pandas matplotlib seaborn wordcloud wikipedia pillow pandas_datareader
TIMEOUT /T 8 > nul
::
echo.
echo.Finished installing Required Modules.
::
echo.
echo.
:: Section 4: Execute runme.bat.
echo.============================
echo.Execute runme.bat
echo.============================
echo.
::
echo set PATH=C:\Python38;%PATH% > %userprofile%\runme.bat
del /s %userprofile%\Downloads\python-3.8.6-amd64.exe >nul 2>&1
echo."Done Installing"
call %userprofile%\runme.bat
python -c "print(\"Welcome, Python installation Success !\")"
:end