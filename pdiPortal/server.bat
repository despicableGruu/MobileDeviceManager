

SET /P ARG = %1

CALL :CASE_%ARG%
IF ERRORLEVEL 1 CALL :DEFAULT_CASE

:CASE_run
    python manage.py runserver --settings=pdiPortal.settings.local\
    GOTO END_CASE
:CASE_make
    python manage.py makemigrations --settings=pdiPortal.settings.local\
    GOTO END_CASE
:CASE_migrate
    python manage.py migrate --settings=pdiPortal.settings.local\
    GOTO END_CASE
:DEFAULT_CASE
    ECHO Unknown argument: "%ARG%"
    GOTO END_CASE
:END_CASE
    VER > NUL
    GOTO :EOF