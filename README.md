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
and to add you quote just
```
# not in path
/path/to/binary/ramsay [quote here]

# in path
ramsay [quote here]
```

## running on windows
need to compile yourself, not developed yet

## building it yourself

you can build with pyinstaller like so
```
pip install pyinstaller
pyinstaller --onefile ramsay.py
```
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
