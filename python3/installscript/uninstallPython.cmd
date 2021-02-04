@echo OFF
::
:: Python Uninstall script: Found the Registry Key Uninstall Value.
:: Should now work.
:: 
cls
:: Prompt for user to Really run this script
setlocal
set Value="n"
:PROMPT
SET /P Value=Are you sure to uninstall Python38 (y/[n])?
IF /I "%Value%" NEQ "y" GOTO END

:: This batch file will show details Windows 10, and Uninstall Python v3.8.6.
TITLE Uninstall Python Software on Windows 7/8/9/10
echo.Checking system information.
TIMEOUT /T 2 > nul

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

:: Quick Pause
echo.
TIMEOUT /T 2 > nul

echo.
echo.
:: Section 3: Python Download.
echo.============================
echo.Delete from OS if found
echo.============================
echo.
::
:: Default Python 3.8.x location
:: %LocalAppData%\Local\Programs\Python\Python38\python.exe /quiet /passive /uninstall
echo. Checking for existing version of Python
::
::
if exist C:\Python38\python.exe (
  echo.Python file has been Found.
  echo.Will now Delete this Software.
  
  cd "%LocalAppData%\Package Cache\{fef707d7-d438-4dd9-bb0f-5788ee658f4f}" 
  python-3.8.6-amd64.exe" /uninstall /quiet
  cd "%LocalAppData%\
  rmdir /s /q pip\
  echo.Continuing to delete Python Software
  echo.
  TIMEOUT /T 4 > nul
  echo.Python has been deleted.
  echo.
  goto end
) ELSE (
  TIMEOUT /T 3 > nul
  echo.Not Found Python installed in thid Custom location. 
  echo.Will try a second location.
  echo.
  goto checkagain
  echo.
)
::
:checkagain
echo.
SET num=5
for /L %%I IN (1, 1, %num%) do (
  echo. | set /p="%%I " 
  TIMEOUT /T 1 > nul
)
::
:: Default Python 3.8.x location
:: %LocalAppData%\Local\Programs\Python\Python38\python.exe /quiet /passive /uninstall
echo. Checking for the second location in window for Python38
::
::
if exist %LocalAppData%\Local\Programs\Python\Python38\python.exe (
  echo.Python file has been Found.
  echo.Will now Delete this Software.
  
  cd "%LocalAppData%\Local\Package Cache\{fef707d7-d438-4dd9-bb0f-5788ee658f4f}" 
  python-3.8.6-amd64.exe" /uninstall /quiet
  cd "%LocalAppData%\
  rmdir /s /q pip\
  echo.Continuing to delete Python Software
  echo.
  TIMEOUT /T 4 > nul
  echo.Python has been deleted.
  echo.
  goto end
) ELSE (
  TIMEOUT /T 3 > nul
  echo.
  echo.Not Found Python installed in this Default location. 
  echo.no other options.
  echo.We dont know where python v3.8 install location if installed previously
  echo.Maybe try using the GUI to Uninstall it.
  echo.We Will end this Uninstall Process.
  goto end
)
:end