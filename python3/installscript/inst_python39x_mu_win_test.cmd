@echo OFF
:: Check Admin DOS PROMPT is available
goto check_permission
:check_permission
    setlocal
    echo. Administrative permissions required. Detecting permissions..
    net session >nul 2>&1
    if %errorLevel% == 0 (
        echo. Admin Permissions confirmed.
        echo. Continuing.......
    ) else (
        echo. Admin Permissions not confired. 
        echo. Right click on the DOS Prompt and RUN AS Administrator
        echo. Exiting..........
        goto end
    )
    echo. 1%% Completed.


:time_pause2
    setlocal
    echo.
    timeout /T 5 > nul

:: clear screen
cls

:: Prompt for user to Really run this script
:start_this
    setlocal
    set _value="n"
    set /p _value=Are you sure installing Python-3.9.12 (y/[n]) ?
    if /i "%_value%" NEQ "y" goto end


:: This batch file will show details Windows 10, and install Python v3.9.12
:section_0
    setlocal
    title Install Python Software on Windows 7/8/9/10/11
    echo. Checking system information.
    timeout /T 2 > nul
    rem Switch to Downloads early on
    cd C:\Users\%USERNAME%\Downloads
    echo. 3%% Completed.

:time_pause2
    setlocal
    timeout /T 2 > nul

:: Section 1: Windows 10/11 information.
:section_1
    echo. ============================
    echo. WINDOWS INFO
    echo. ============================
    echo.
    systeminfo | findstr /c:"OS Name"
    systeminfo | findstr /c:"OS Version"
    systeminfo | findstr /c:"Hyper-V Requirements"
    echo. 5%% Completed.

:time_pause2
    setlocal
    echo.
    timeout /T 2 > nul

:: Section 2: Hardware information.
:section_2
    echo. ============================
    echo. HARDWARE INFO
    echo. ============================
    echo.
    systeminfo | findstr /c:"Total Physical Memory"
    systeminfo | findstr /c:"Virtual Memory: In Use"

:time_pause2
    setlocal
    echo.
    timeout /T 2 > nul
    echo. 8%% Completed.


:: Section 3: Python Download.
rem https://www.python.org/ftp/python/3.9.12/python-3.9.12-amd64.exe
:section_3
    echo. ============================
    echo. Checking Existing Python
    echo. ============================
    echo.

:section_3_1
    if exist "python-3.10.0-*.<" (
        echo. Found existing version of Python 3.10.0
        del python-3.10.0-*.exe
        del python-3.10.*.exe
        echo. Deleting existing version of Python
        echo.
    ) else (
        echo. No existing version of python 3.10.0 Avail.
        echo.
    )
    echo. 10%% Completed.

:time_pause2
    setlocal
    echo.
    timeout /T 2 > nul

:section_3_2
    if exist "python-3.9.*.<" (
        echo. Found existing version of Python 3.9.*
        del python-3.9.*.exe
        echo. Deleting existing version of Python
        echo.
    ) else (
        echo. No existing version of python 3.9 Found.
        echo.
    )
    echo. 15%% Completed.

:time_pause2
    setlocal
    echo.
    timeout /T 2 > nul

:section_3_3
    if exist "python-3.8.*.<" (
        echo. Found existing version of Python 3.8.*
        del python-3.8.*.exe
        echo. Deleting existing version of Python
        echo.
        ) else (
            echo. No existing version of python 3.8 Found.
            echo.
    )
    echo. 20%% Completed.

:section_3_4
    setlocal
    rem You may need to press ENTER, If the wait time is more than 10 seconds.
    echo.
    echo. You may need to press ENTER, 
    echo. If the wait time is more than 10 seconds.
    echo. or CTRL-C, if it crashed or something.
    echo.

:time_pause2
    setlocal
    echo.
    timeout /T 2 > nul


:: Section 4: Bitsadmin Download.
:section_4
    setlocal
    echo.
    echo. ============================
    echo. Checking Bitsadmin
    echo. ============================
    echo.

    REM forgot that 32bit Windows has a different location for bitsadmin
    if /i "%processor_architecture%"=="x86" (
        rem Run 32 bit
        if exist C:\Windows\System32\bitsadmin.exe (
            echo. Bitsadmin 32bit is installed on your Windows 7/8/9/10 system.
            echo. Will download Python 3 software.
            echo.
            goto section_5
        ) else (
            echo. We dont know where bitsadmin 32bit is located.
            goto end
        )
    ) else (
        rem Run 64 bit
        if exist C:\Windows\SysWOW64\bitsadmin.exe (
            echo. Bitsadmin 64bit is installed on your Windows 7/8/9/10/11 system.
            echo. Will download Python 3 software.
            echo.
            goto section_5
        ) else (
            echo. We dont know where bitsadmin 64bit is located.
            goto end
        )
    )           
    echo. 30%% Completed.


:time_pause2
    setlocal
    echo.
    timeout /T 2 > nul


:: Section 5: Python Download.
:section_5
    setlocal
    echo.
    echo. ============================
    echo. Downloading Python
    echo. ============================
    echo.

:: Section 5: Python Download.
:check_arch
    setlocal
    echo.
    if /i "%processor_architecture%"=="x86" (
            C:\Windows\System32\bitsadmin.exe /transfer PythonDownload /download /priority normal https://www.python.org/ftp/python/3.9.12/python-3.9.12.exe C:\Users\%USERNAME%\Downloads\python-3.9.12.exe
        ) else (
            rem Run 64 bit download
            C:\Windows\SysWOW64\bitsadmin.exe /transfer PythonDownload /download /priority normal https://www.python.org/ftp/python/3.9.12/python-3.9.12-amd64.exe C:\Users\%USERNAME%\Downloads\python-3.9.12-amd64.exe
        )           
    echo. 40%% Completed.
    echo.

:time_pause4
    setlocal
    echo.
    timeout /T 4 > nul


:: Checking to see if this python file has been downloaded.
:section_6
    setlocal
    echo.
    echo. Checking to see if this python file has been downloaded.
    if exist python-3.9.12-amd64.exe (
        echo. Python executable has been Found.
        echo. Will now Install this Software.
        echo.
        ) ELSE (
            echo. Software not found.
            echo. Perhaps, try to run this file again.
            echo.
            goto end
        )
    echo. 50%% Completed.
    echo.

:time_pause4
    setlocal
    echo.
    timeout /T 4 > nul

:: Finish downloading the Python Software
:section_7
    setlocal
    echo.
    rem nothing here to see
    timeout /T 1 > nul

:: Installing Python
:section_8
    setlocal
    echo.
    echo. ============================
    echo. Installing Python
    echo. ============================
    echo.
    echo. Go grab Koffie or something, installion will take sometime since we had configured it to compile a few items.
    if /i "%processor_architecture%"=="x86" (
        C:\Users\%USERNAME%\Downloads\python-3.9.12.exe /quiet /passive InstallAllUsers=0 TargetDir=C:\Python3912 AssociateFiles=1 CompileAll=1 PrependPath=0 Shortcuts=0 Include_doc=1 Include_debug=0 Include_dev=1 Include_exe=1 Include_launcher=1 InstallLauncherAllUsers=1 Include_lib=1 Include_pip=1 Include_symbol=0 Include_tcltk=1 Include_test=1 Include_tools=1
        timeout /t 4 > nul
    ) else (
        C:\Users\%USERNAME%\Downloads\python-3.9.12-amd64.exe /quiet /passive InstallAllUsers=0 TargetDir=C:\Python3912 AssociateFiles=1 CompileAll=1 PrependPath=0 Shortcuts=0 Include_doc=1 Include_debug=0 Include_dev=1 Include_exe=1 Include_launcher=1 InstallLauncherAllUsers=1 Include_lib=1 Include_pip=1 Include_symbol=0 Include_tcltk=1 Include_test=1 Include_tools=1
        timeout /t 4 > nul
    )
    echo. 60%% Completed.

:time_pause4
    setlocal
    echo.
    timeout /T 4 > nul


:: Compiling and Installing Python Modules
:section_9
    setlocal
    echo.
    echo. =======================================
    echo. Compiling and Installing Python Modules
    echo. =======================================
    echo.
    set num=12
    for /L %%I IN (1, 1, %num%) do (
        echo. | set /p="%%I " 
        timeout /T 1 > nul
    )
    echo. 65%% Completed.


:: Check to see if Python was installed 
:section_10
    echo.
    if exist C:\Python3912\Tools\pynche\Main.py (
        echo.
        echo. Checking whether Python has been installed...
        echo.
        echo. Python Software has been Installed.
        echo.
    ) else (
        echo.
        echo. Python has not been installed.
        echo.
        echo. Problem with installation. PRESS: CTRL-C to End Installation process only if after three printed messages.
        echo.
        goto check
    )
    echo. 70%% Completed.
    echo.

:: Check to see if Python was installed 
:section_11
    setlocal
    echo.
    echo. ========================
    echo. Updating pip the modules
    echo. ========================
    echo.
    rem Updating pip on Windows
    C:\Python3912\python.exe -m pip install --upgrade pip
    echo. 75%% Completed.
    echo.

:: Finished Updating pip
:section_12
    setlocal
    echo.
    echo. ======================
    echo. Finished Updating pip
    echo. ======================
    echo.
    echo. 80%% Completed.
    echo.

:time_pause2
    setlocal
    echo.
    timeout /T 2 > nul


:: Installing Additional Modules
:section_13
    setlocal
    echo. =============================
    echo. Installing Additional Modules
    echo. =============================
    echo.
    C:\Python3912\Scripts\pip.exe install --user wheel
    echo. 85%% Completed.
    echo.

:time_pause2
    setlocal
    echo.
    timeout /T 2 > nul

:: Finished installing Modules
:section_14
    setlocal
    echo.
    echo. ===========================
    echo. Finished installing Modules
    echo. ===========================
    echo.
    echo. 90%% Completed.
    echo.

:: Execute runme.bat.
:section_15
    setlocal
    echo.
    echo. ============================
    echo. Execute runme.bat
    echo. ============================
    echo set PATH=C:\Python3912;%PATH% > C:\Users\%USERNAME%\runme.bat
    del /s C:\Users\%USERNAME%\Downloads\python-3.9.12-amd64.exe >nul 2>&1
    call C:\Users\%USERNAME%\runme.bat
    echo.

cls
:: Run Python
:section_16
    setlocal
    echo.
    python -c "print(\"Welcome, Python installation Success.\")"
    echo.

:section_17
    echo.
    echo. 100%% Completed !
    echo.
:end