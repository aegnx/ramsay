# ramsay

![image](https://github.com/user-attachments/assets/c7c6e9aa-a7eb-4305-8455-a133b4426fbe)

welcome to ram**say**, a cool python project about making ascii gordon ramsay repeating his insults to you, or even saying what you want him to say.

you can find binaries on the "releases" tab, or build it with pyinstaller

to run it on linux, install it first by curling a bash script and feeding it to sh AS ADMIN
```
sudo curl https://raw.githubusercontent.com/aegnx/ramsay/main/install.sh | sh
```
then just run it
```
ramsay
```
for help just put the ``-h`` option after the command 
```
ramsay -h
```
this will NOT ensure any help other then the usage of ramsay (the program)

## running on windows
use powershell and a font that supports braille, head on to your download folder like so:
```
cd [Downloads folder]
```
and then run it like linux
```
.\ramsay.exe
```
apparently bash on windows spits out an error so just use powershell with a proper font

you can use flags too, just add them after it like so
```
.\ramsay.exe -h
```
## building it yourself

you can build with pyinstaller like so
```
pip install pyinstaller
pyinstaller --onefile ramsay.py
```
you may have to manage venvs on linux before doing so (pipx does all the work i think)

then head into ``dist`` (``cd dist`` after you are done) and grab the binary

on linux, just chmod it like so to make it executable
```
chmod +x ramsay
```
and for linux binaries, just copy it into ``/bin`` or ``/usr/bin`` like so
```
sudo cp [download location]/ramsay /bin/ramsay
```
or (for ``/usr/bin``)
```
sudo cp [download location]/ramsay /usr/bin/ramsay
```
example:
```
sudo cp /home/aegnx/Downloads/ramsay /bin/ramsay
```
or (for ``/usr/bin``)
```
sudo cp /home/aegnx/Downloads/ramsay /usr/bin/ramsay
```
and also for exe files you just have to run it using cmd or powershell, windows terminal is optional but a font is necessary

for the best experience use konsole (kde's terminal emulator on linux or freebsd) and disable the "Use unicode Braille characters contained in font" in:

menu>settings>configure konsole>profile>[profile name]>edit>appearance>color scheme & font

## building and using it with the dockerfile

clone the repo
```
git clone https://github.com/aegnx/ramsay.py
```
then build the image like so
```
docker build -t ramsay
```
and then execute it
```
docker run ramsay:latest
```
