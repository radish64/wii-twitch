# Wii Twitch (rii twitch? idk i'm not your mom call it whatever)

## how 2 run
### you need yt-dlp and ffmpeg installed and i've only tested this on linux
- clone the repo
    - `git clone http://github.com/radish64/wii-twitch.git`
- create a venv 
    - `python3 -m venv wii-twitch`
- enter the directory
    - `cd wii-twitch`
- source the thing idk what it's called
    - `source bin/activate`
- install the requirements
    - `pip install flask waitress`
- run the server
    - `waitress-serve --listen=(insert your ip):1234 server:app`

## in WiiMC(-SS) now
- add the following lines to your **onlinemedia.xml**
    - `<link name="twitch" addr="http://(insert your ip):1234" />`
    - `<link name="twitch - search " addr="http://(insert your ip)/twitch/?channel=" type="search" />`
