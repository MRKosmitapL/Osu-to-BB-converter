# Osu!-to-BB-converter
Script made by Misery

---

# Installing
make sure you have python at least v3.10.6 and download OsuPyParser
```
pip install OsuPyParser
```
then download the .py file and place it in a folder of your likings.
For example make a new folder called "OsuToBB" and place it there.

---

# Using
1. Download osu! map
2. Open downloaded map in osu!
3. After that locate your osu! folder and go to:  osu! -> Songs and search for the map you want to convert
4. Pick .osu file and copy it to the folder where the converter is (mine is OsuToBB folder so i would copy .osu file there)
5. ***Rename .osu file to "osuFile.osu"***
6. Open terminal/console and go to the converter's folder
7. run "python .\maniaTobb.py" or "python .\stdTobb.py"
8. In the same folder a file called "notes.cfg" should be created
9. Swap "notes.cfg" files inside "mods/mod_name/default/config"
10. In Beat Banger open mod via level editor, set the bpm to the song bpm and set SongOffset to 0
11. > profit

---
# FAQ

### What about sliders?

This script treats sliders as normal single notes

### What about multiple notes appearing on the same time?

Script ignores them and add only the first occuring note in [HitObjects] section of original .osu file
