# Instruction

Date: 2024/11/03

Version: Debian 12.7 stable

Install `gnome-shell`, `gnome-terminal`, `gnome-boxes`, `nautilus`, `gedit`, `totem`, `gnome-shell-extension-dashtodock`, `qbittorrent` and `chromium`.

```
sh applications.sh
```

Reboot for update the feature.

Copy `themes`, `icons` to `~/.themes/`, `~/.icons/`, then set the configuration.

```
sh topic.sh
```

Install logo of terminal.

```
sh logo.sh
```

Set `gnome-shell` and `gnome-terminal`.

```
sh shell.sh
sh terminal.sh
sh stty.sh # Option
```

#### Warning

Executing this program will add some commands to the .bashrc, .profile, and gsettings files, and they cannot be automatically restored to their original state. Please proceed with caution!