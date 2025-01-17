# !/bin/bash
gnome-extensions enable dash-to-dock@micxgx.gmail.com
SCHEMA="org.gnome.desktop.wm.preferences"
gsettings set $SCHEMA button-layout 'close,minimize,maximize:'
mkdir ~/.themes/
mkdir ~/.icons/
cp -r ./themes/* ~/.themes/
cp -r ./icons/* ~/.icons/
# Option is 'WhiteSur-Dark' or 'WhiteSur-Light'.
gsettings set org.gnome.desktop.interface gtk-theme 'WhiteSur-Dark'
echo "export GTK_THEME=WhiteSur-Dark" >> ~/.profile
# Option is 'Os-Catalina-Night' or 'Os-Catalina-Morning'.
gsettings set org.gnome.desktop.interface icon-theme 'Os-Catalina-Night'
