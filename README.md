A simple explorer that receives a webpage as parameter to launch the game. You can create .desktop icon directly using the ``-d`` option (see the help for mor info).

### Usage
    ./mgl.py [options] url

### Example

#### Launching a game
    ./mgl.py -m theexamplegame.com

#### Creating a .desktop
    ./mgl.py -f theexample.com -d $HOME/Desktop/thegame.desktop -t "A fantastic game" -c "Minino;Games;" -i /usr/share/pixmaps/game.png

### Requirements
- python-webkit

### --help
    Usage: mgl.py [options or -h] url

    Options:
      -h, --help            show this help message and exit
      -f, --fullscreen      start the launcher at fullscreen
      -m, --maximized       start the launcher maximized
      -t TITLE, --title=TITLE
                            window title
      --width=WIDTH         window width
      --height=HEIGHT       window height

      Creating .desktop icons:
        -c CATEGORIES, --categories=CATEGORIES
                            ; separated categories to the icon
        -d DESKTOP, --desktop=DESKTOP
                            path to save the .desktop
        -i ICON, --icon=ICON
                            icon to use at the .desktop file
