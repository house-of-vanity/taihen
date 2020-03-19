#!/usr/bin/env python3
'''
yTermPlayer by TimeTraveller
(https://github.com/TimeTraveller-San/yTermPlayer)
Special thanks for these libraries and their contributors:
- urwid
- pafy
- python-mpv
'''
import os
import urwid
from taihen.music_api import TaihenPlayer
from taihen.ui import player_ui
from taihen.settings import PL_DIR

# Palette for the urwid UI
palette = [
    ('reversed', 'standout', ''),
    ('b', 'black', 'dark gray'),
    ('highlight', 'black', 'light blue'),
    ('bg', 'black', 'dark blue'),
]


def main():
    """Main script function."""
    os.makedirs(PL_DIR, exist_ok=True)
    new_player = player_ui()
    loop = urwid.MainLoop(new_player.draw_ui(),
                          palette,
                          unhandled_input=new_player.handle_keys)
    loop.set_alarm_in(2, new_player.update_name)
    loop.run()


if __name__ == "__main__":
    main()
