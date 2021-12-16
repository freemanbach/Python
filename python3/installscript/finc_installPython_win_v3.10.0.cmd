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
:: wmic diskdrive GET index,caption,name,size /format:table
:: wmic diskdrive GET index,Model,SerialNumber,Size,Status


:: Quick Pause
echo.
timeout /T 2 > nul

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
:: C:\Windows\SysWOW64\bitsadmin.exe
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
::
timeout /T 2 > nul

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
:: bitsadmin /transfer PythonDownload /download /priority normal https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe %userprofile%\Downloads\python-3.8.6-amd64.exe

:: Quick Pause
echo.
echo.
timeout /T 1 > nul
timeout /T 1 > nul
echo.Checking to see if this python file has been downloaded.

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

echo.
echo.
:: Section 4: Python Installation.
echo.============================
echo.Installing Python
echo.============================
echo.

echo.
echo.Installing Python version 3.10.0
echo.This process will take as much as 15 mins if there is no SSD.
echo.
echo.Go grab Koffie or something before coming back to your Laptop.
:: Download Python
:: https://www.python.org/downloads/release/python-396/
::
:: This python install process is weird, it will simply return prompt once it had been executed but the process
:: will not be 100 percent completed before continuing as we have learned.
:: Came across another problem where installAllusers must be 0
:: before the Python39 dir will stay around in the C:\ driectory
%userprofile%\Downloads\python-3.10.0-amd64.exe /quiet InstallAllUsers=0 TargetDir=C:\Python310 AssociateFiles=1 CompileAll=1 PrependPath=0 Shortcuts=0 Include_doc=1 Include_debug=0 Include_dev=0 Include_exe=1 Include_launcher=1 InstallLauncherAllUsers=1 Include_lib=1 Include_pip=1 Include_symbol=0 Include_tcltk=1 Include_test=1 Include_tools=1
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
if exist C:\Python310\Tools\pynche\Main.py (
    echo.Checking Files if they were Created.....
    timeout /T 2 > nul
    echo.
    echo.They were created.
) else (
    echo.Files still not created.....
    echo.Still compiling code, maybe.
    timeout /T 2 > nul
    echo.
    timeout /T 2 > nul
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
timeout /T 3 > nul
echo.
echo.Finished Updating pip.
::
:: Waiting for the previous process to finish
::
echo.
echo.
echo.Installing Additional required Modules
echo.PRESS ENTER HERE If wait time is Longer than 8 seconds
:: It is a large download in the lines below, therefore i took it as a seperate install
timeout /T 2 > nul
C:\Python310\Scripts\pip.exe install --user wheel
:: This stuff required VisualStudio with c++ or XCode on mac OSX
:: somehow they needed to be installed with wheel and in sourcecode form
::timeout /T 1 > nul
::C:\Python310\Scripts\pip.exe install --user scikit-learn keras theano
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user pandas_datareader requests ta scipy numpy plotly
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user pandas matplotlib seaborn statsmodels QuantLib pyfinlab
timeout /T 1 > nul
C:\Python310\Scripts\pip.exe install --user yfinance PyAlgoTrade yahoo_fin Statistics-pyt backtrader
:: C:\Python38\scripts\pip.exe install --user pyfin vollib quantpy ffn tia pynance mplfinance plotly 
:: C:\Python38\scripts\pip.exe install --user yahoo_fin vaderSentiment xlsxwriter xlrd openpyxl
:: C:\Python38\scripts\pip.exe install --user quandl tqdm ta
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: To download unbuildable packages: go to UC Irvine
:: https://www.lfd.uci.edu/~gohlke/pythonlibs
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: additional finance Software 
:: https://financetrain.com/best-python-librariespackages-finance-financial-data-scientists/
:: https://www.datacamp.com/community/tutorials/finance-python-trading
:: https://medium.com/fintechexplained/automating-stock-investing-technical-analysis-with-python-81c669e360b2
:: https://pythonrepo.com/repo/bukosabino-ta-python-finance
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::  Cant install these things via pip on windows
::  Failed to build numba llvmlite scikit-learn
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
timeout /T 2 > nul
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
echo set PATH=C:\Python310;%PATH% > %userprofile%\runme.bat
del /s %userprofile%\Downloads\python-3.10.0-amd64.exe >nul 2>&1
echo."Done Installing"
call %userprofile%\runme.bat
python -c "print(\"Welcome, Python installation Success !\")"
:end
