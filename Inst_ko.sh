#!/bin/bash
cd src
sudo touch /usr/bin/dedit-ko
sudo touch /usr/bin/gmemo

sudo cp -r --force dedit-ko.py /usr/bin/dedit-ko
sudo cp -r --force gmemo.py /usr/bin/gmemo
cd ..
sudo mkdir /etc/dedit
sudo cp -r --force *.png /usr/share/pixmaps/
cd desktop
sudo cp -r --force DeltaEdit-KO.desktop /usr/share/applications
sudo cp -r --force GMemo.desktop /usr/share/applications
cd ..
cd man
sudo cp -r --force *.1.gz /usr/share/man/man1/
cd ..
cd etc
sudo cp -r --force * /etc/dedit/
cd ..
sudo chmod +x /usr/share/applications/DeltaEdit-KO.desktop
sudo chmod +x /usr/share/applications/GMemo.desktop
sudo chmod +x /usr/bin/dedit-ko
sudo chmod +x /usr/bin/gmemo
echo 'command=dedit-ko'
sudo update-mime-database /usr/share/mime
echo 'Done!'
