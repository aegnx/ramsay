# ramsay

![image](https://github.com/user-attachments/assets/c7c6e9aa-a7eb-4305-8455-a133b4426fbe)

welcome to ram**say**, a cool python project about making ascii gordon ramsay repeating his insults to you, or even saying what you want him to say.

you can find binaries on the "releases" tab, or build it with pyinstaller

to run it on linux, install it first by curling a bash script and feeding it to sh
```
curl https://raw.githubusercontent.com/aegnx/ramsay/main/install.sh | sh
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

its a fucking python script. you dont have to fucking build jack shit

the author really is a fan of destroying your package manager, im not.
instead of putting it in fucking `/usr/bin` (bad idea), put it in `~/.local/bin` (good idea)

## building and using it with the dockerfile

WHY THE FUCK DO YOU NEED A DOCKERFILE FOR A FUCKING PYTHON SCRIPT????? MY MAGIC 8BALL HAS BETTERS IDEAS THAN YOU
