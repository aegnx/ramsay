# ramsay.py

welcome to ram**say**.py, a cool python project about making ascii gordon ramsay repeating his insults to you, or even saying what you want him to say.

you can find binaries on the "releases" tab, or build it with pyinstaller

to run it on linux, just do the command below
```
# not in path
/path/to/binary/ramsay

# in path
ramsay
```
and also there is no ``--help`` flag so you have to use the -h option

just do this command below
```
# not in path
/path/to/binary/ramsay -h

# in path
ramsay -h
```
## running on windows
need to build yourself using pip and pyinstaller like down below, not developed yet

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
and also for exe files (soon, or just compile it yourself) you just have to run it using cmd or powershell or even git bash

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
