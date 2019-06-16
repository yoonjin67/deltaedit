#!/bin/bash
sudo rm -rf /usr/bin/dedit-ko
sudo rm -rf /usr/bin/gmemo
sudo rm -rf /usr/share/applications/GMemo.desktop
sudo rm -rf /usr/share/applications/DeltaEdit-KO.desktop
sudo rm -rf /usr/share/man/man1/dedit.1.gz
sudo rm -rf /usr/share/man/man1/gmemo.1.gz
sudo rm -rf /usr/share/pixmaps/gmemo.png
sudo rm -rf /usr/share/pixmaps/dedit.png
sudo rm -rf /usr/share/pixmaps/dedit_logo.png
sudo rmdir /etc/dedit
sudo update-mime-database /usr/share/mime
echo 'Done!'
