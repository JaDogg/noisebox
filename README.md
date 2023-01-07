# 🎶🎵📦 NoiseBox

Background noise generator for concentration in your terminal. 

![](https://github.com/JaDogg/noisebox/blob/main/images/noisebox.png)

#### Credits
* Mug ASCII art By Morfina https://www.asciiart.eu/food-and-drinks/coffee-and-tea
* Rain Sound - https://freesound.org/people/straget/sounds/531947/
* People Talking Sound - https://freesound.org/people/priesjensen/sounds/482990/
* ICE Maker Sound - https://freesound.org/people/FreeToUseSounds/sounds/399916/
* Garbage Collector Sound - https://freesound.org/people/Zabuhailo/sounds/165776/
* Icon: By Vitaly Gorbachev - https://www.flaticon.com/free-icon/wind_959737

### Installation and use (Need Python3.6+)

```shell
git clone git@github.com:JaDogg/noisebox.git
cd noisebox
pip install -r requirements.txt
python noisebox.py
```
* Optionally Create a Virtual Environment

#### How do I customize the audio mix?
* Add any audio loops/cuts to `noise` folder.
* Edit `mix.json`
* If you want to make your own loops see [this](https://gamedevbeginner.com/create-looping-sound-effects-for-games-for-free-with-audacity/).
* You can also fork the repo and install from that and then edit `mix.json` (so you can save it to github).

### Creating an .exe in Windows

```shell
rem this uses build.cmd
build 
```
--------

    NoiseBox - Background noise generator for concentration in your terminal. 
    Copyright (C) 2020 - 2023 Bhathiya Perera

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
