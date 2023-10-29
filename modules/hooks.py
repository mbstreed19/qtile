
from libqtile import hook
import subprocess
import os
from libqtile.utils import send_notification

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart"])
    send_notification("running autostart")


@hook.subscribe.startup_once
def screenlayout():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.screenlayout/screenlayout.sh"])
    send_notification("setting up screenlayout")
