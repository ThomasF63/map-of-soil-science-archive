@echo off
setlocal
cd /d "%~dp0"

echo === Map of Soil Science ===
echo Mise a jour depuis GitHub (branche main)...
echo.

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo [Avertissement] Pas un depot Git. Ouverture du fichier local.
    goto :open
)

for /f "tokens=*" %%b in ('git rev-parse --abbrev-ref HEAD') do set CURRENT_BRANCH=%%b

if /i not "%CURRENT_BRANCH%"=="main" (
    echo Branche actuelle : %CURRENT_BRANCH% — bascule vers main...
    git checkout main
    if errorlevel 1 (
        echo [Avertissement] Impossible de basculer sur main ^(modifs locales non commit ?^).
        echo Ouverture de la version locale actuelle ^(branche %CURRENT_BRANCH%^).
        goto :open
    )
)

git pull --ff-only origin main
if errorlevel 1 (
    echo [Avertissement] git pull a echoue. Ouverture de la version locale.
)

:open
echo.
echo Ouverture de index.html...
start "" "index.html"
endlocal
