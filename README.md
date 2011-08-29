A simple explorer that receives a webpage as parameter to launch the game.

### Usage
./mgl.py [options] url

### Example
./mgl.py -m google.com

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
