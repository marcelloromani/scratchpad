VSCODE_PATH="/Applications/Visual Studio Code.app/Contents/MacOS/Electron"
function code {
    "${VSCODE_PATH}" $@ >/dev/null 2>&1 &
}
