#!/bin/bash
cd src
sudo touch /usr/bin/dedit-jp
sudo touch /usr/bin/gmemo

sudo cp -r --force dedit-jp.py /usr/bin/dedit-jp
sudo cp -r --force gmemo.py /usr/bin/gmemo
cd ..
sudo mkdir /etc/dedit
sudo cp -r --force *.png /usr/share/pixmaps/
cd desktop
sudo cp -r --force DeltaEdit-JP.desktop /usr/share/applications
sudo cp -r --force GMemo.desktop /usr/share/applications
cd ..
cd man
sudo cp -r --force *.1.gz /usr/share/man/man1/
cd ..
cd etc
sudo cp -r --force * /etc/dedit/
cd ..
sudo chmod +x /usr/share/applications/DeltaEdit-JP.desktop
sudo chmod +x /usr/share/applications/GMemo.desktop
sudo chmod +x /usr/bin/dedit-jp
sudo chmod +x /usr/bin/gmemo
echo 'command=dedit-jp'
sudo update-mime-database /usr/share/mime
echo 'Done!'
