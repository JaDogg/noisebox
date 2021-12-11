# 🎶🎵📦 NoiseBox

Background music/noise generator for concentration. 

* Please supply your own sound loops. 
  * I had to modify one on my own. But I am not allowed to redistribute it :( 
* Uses PyGame. :) 
* Use pyinstaller to build your own .exe

Icon: By Vitaly Gorbachev - https://www.flaticon.com/free-icon/wind_959737

### Installation and use.

```shell
git clone git@github.com:JaDogg/noisebox.git
cd noisebox
python3 -m venv .venv
. .venv/bin/activate # activate virtual environment in Windows this is ".\.venv\Scripts\activate"
pip install pygame
python noisebox.py
```

### Creating an .exe in Windows

```shell
rem this uses build.cmd
build 
```