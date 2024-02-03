where /q pyinstaller
if %ERRORLEVEL% equ 0 (
    pyinstaller ^
        --distpath=./exe/windows ^
        --workpath=./exe/windows ^
        ./exe/windows/build.spec
) else (
    python -m PyInstaller ^
        --distpath=./exe/windows ^
        --workpath=./exe/windows ^
        ./exe/windows/build.spec
)