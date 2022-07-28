@echo off
REM # Updated 16:39 28/07/2022
REM # ###

cd %~dp0 | exit 1

set HOME=.
set PYTHONHOME=c:\python\3.7\
for %%I in (.) do set REPOS=%%~nI%%~xI

echo Confirm all files are saved?
pause

echo Confirm "%REPOS%" version number has been updated (setup.cfg, docs/conf.py)?
pause

rmdir /s /q .\dist

cd .\src
forfiles /P . /M *.egg-info /C "cmd /c rmdir /s /q @file"
cd ..

cd .\docs
%PYTHONHOME%Scripts\sphinx-build.exe -a -b html . _build
cd ..

%PYTHONHOME%\python -m pip install --upgrade build
%PYTHONHOME%\python -m pip install --upgrade twine

%PYTHONHOME%\python -m build

echo Check build is correct before proceeding
pause

echo Uploading to testpypi
%PYTHONHOME%\python -m twine upload --verbose --repository testpypi dist/*

echo "%PYTHONHOME%\python -m pip install --upgrade --index-url https://test.pypi.org/simple/ %REPOS%"
echo Install from testpypi and confirm package is working
pause

echo Confirm all code submitted to GitHub with version
pause

echo Uploading to pypi
%PYTHONHOME%\python -m twine upload --verbose --repository pypi dist/*

echo "%PYTHONHOME%\python -m pip uninstall %REPOS%"
echo "%PYTHONHOME%\python -m pip install --upgrade %REPOS%"
echo Uninstall and reinstall from pypi and confirm package is working
pause

echo Completed.
pause
