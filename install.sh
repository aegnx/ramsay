set -e
echo "Downloading binary from github releases..."
curl -sL https://github.com/aegnx/ramsay/releases/download/release020/ramsay -o $HOME/.local/bin/ramsay
echo "giving it execution permissions"
chmod +x ~/.local/bin/ramsay
echo "Done! enjoy."
exit
