set -e
echo "welcome! hope you ran it as sudo"
echo "downloading binary."
curl -LO https://github.com/aegnx/ramsay/releases/download/release020/ramsay
echo "copying binary to /bin, hope the binary is in the same folder you're in"
cp ramsay /usr/bin/ramsay
echo "succesfully copied"
echo "giving it execution perms"
chmod +x /usr/bin/ramsay
echo "done! enjoy."