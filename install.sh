set -e
echo "Welcome To The Ramsay Installer!"
sleep 1
echo "Downloading binary..."
sleep 1
curl -LO https://github.com/aegnx/ramsay/releases/download/release020/ramsay
sleep 1
echo "copying binary to /bin"
sleep 1
echo "Please Input your Password if not in su!"
sleep 0.1
sudo cp ramsay /usr/bin/ramsay
sleep 1
rm ramsay
sleep 1
echo "Succesfully copied!"
sleep 1
echo "Giving it Execution Perms, again, enter your password if you arent in su"
sleep 1
sudo chmod +x /usr/bin/ramsay
sleep 1
echo "Done! enjoy."
sleep 1
exit
