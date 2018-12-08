import subprocess
import os

def title_of_window(app_name):
    """
        Retrieves the title of application by through 'subprocess'.
        Only works on Linux.

        Params:
            app_name (string) -- name of the application to be taken the title
                ex. --> spotify
                    --> filezilla
                    --> putty
                    --> atom

        *For this SpotiLyric app:
            - app_name parameter must be equal to "spotify"
            - Retrieves song that is currently playing on Spotify Desktop App.

    """
    # Finds id of all GUI apps who running.
    # Ex. -> ['0x200000a', '0x3800007', '0x4800001', '0x2e00010', '0x3600001\n']
    active_windows = subprocess.Popen(["xprop",
                                       "-root",
                                       "_NET_CLIENT_LIST_STACKING"],
                                       stdout=subprocess.PIPE).communicate()
    active_windows_ids = active_windows[0].decode("utf-8").split("# ")[1].split(", ")
    #
    # Sends all ids to 'xprop -id' and checks. If app name equal to app_name parameter, return title of this app.
    # Ex. -> get_window.py — ~/Desktop/projects — Atom
    for active_id in active_windows_ids:
        window = subprocess.Popen(["xprop",
                                    "-id",
                                    active_id.strip(),
                                    "WM_CLASS",
                                    "_NET_WM_NAME"],
                                    stdout=subprocess.PIPE).communicate()
        window = window[0].decode("utf-8").split('"')
        if app_name == window[3].lower():
            return window[5] # return current title of window.
