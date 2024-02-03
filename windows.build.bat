where /q pyinstaller
if %ERRORLEVEL% equ 0 (
    pyinstaller ^
        --distpath=./exe/windows-64bit ^
        --workpath=./exe/windows-64bit ^
        ./exe/windows-64bit/build.spec
) else (
    python -m PyInstaller ^
        --distpath=./exe/windows-64bit ^
        --workpath=./exe/windows-64bit ^
        ./exe/windows-64bit/build.spec
)