from libqtile.lazy import lazy
from libqtile.config import Key, KeyChord

mod = "mod4"
terminal = "kitty"
browser = "firefox"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn("rofi -show run"),
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="start screeshot tool"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "b", lazy.spawn(browser), desc="Spawn my browser of choice"),
    # Key chords for emacs use CTRL+e followed by "key"
    KeyChord(
        ["control"],
        "e",
        [
            Key([], "e", lazy.spawn("emacsclient -c -a 'emacs'"), desc="launch emacs"),
            Key(
                [],
                "b",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
                desc="Emacsclient Ibuffer",
            ),
            Key(
                [],
                "d",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
                desc="Emacsclient Dired",
            ),
            Key(
                [],
                "s",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
                desc="Emacsclient Eshell",
            ),
            Key(
                [],
                "v",
                lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
                desc="Emacsclient Vterm",
            ),
        ],
    ),
    # Switch focus to specific monitor (out of three)
    Key([mod], "e", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    Key([mod], "r", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    Key([mod], "w", lazy.to_screen(2), desc="Keyboard focus to monitor 3"),
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
]
