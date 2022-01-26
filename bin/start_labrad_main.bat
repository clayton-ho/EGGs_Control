::Starts all main LabRAD servers

@ECHO OFF
SETLOCAL EnableDelayedExpansion

REM: Prepare LabRAD CMD
CALL %LABRAD_ROOT%\bin\prepare_labrad.bat

REM: Parse arguments for server activation
SET /a server_flag=0
FOR %%x IN (%*) DO (
    IF "%%x"=="-s" (SET /a server_flag=!1!)
)


REM: Core Servers
START "Labrad Manager" /min %HOME%\Code\scalabrad-0.8.3\bin\labrad.bat --tls-required false
START "Labrad Web GUI" /min %HOME%\Code\scalabrad-web-server-2.0.6\bin\labrad-web.bat
START "Labrad Node" /min CMD "/k activate labart && python %HOME%\Code\pylabrad\labrad\node\__init__.py"
START "" "%ProgramFiles(x86)%\chrome-win\chrome.exe" http://localhost:7667

REM: Experiment Servers
START /min CMD /c %LABRAD_ROOT%\bin\labrad\start_labrad_experiments.bat

REM: Device Bus Servers
START "GPIB Device Manager" /min CMD "/k activate labart && python %LABRAD_ROOT%\EGGS_labrad\servers\gpib\gpib_device_manager.py"
TIMEOUT 1 && START /min CMD /c %LABRAD_ROOT%\bin\labrad\start_labrad_devices.bat

REM: ARTIQ
START /min CMD /c %LABRAD_ROOT%\bin\start_artiq.bat

REM: Clients
START /min CMD /c %LABRAD_ROOT%\bin\labrad\start_labrad_clients.bat

REM: Run all device servers as specified
IF %server_flag%==1 (
    TIMEOUT 3
    START /min CMD /c %LABRAD_ROOT%\bin\labrad\start_labrad_servers.bat
    REM: Open a Python shell with all device servers already declared
    CALL %LABRAD_ROOT%\bin\server_cxn.bat
) ELSE ( CALL %LABRAD_ROOT%\bin\labart_cxn.bat )





