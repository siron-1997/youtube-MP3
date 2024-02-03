if command -v pyinstaller > /dev/null 2>&1; then
    pyinstaller \
        --distpath=./exe/linux-ubuntu \
        --workpath=./exe/linux-ubuntu \
        ./exe/linux-ubuntu/build.spec
else
    python -m PyInstaller \
        --distpath=./exe/linux-ubuntu \
        --workpath=./exe/linux-ubuntu \
        ./exe/linux-ubuntu/build.spec
fi