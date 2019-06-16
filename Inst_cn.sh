#!/bin/bash
cd src
sudo touch /usr/bin/dedit-cn
sudo touch /usr/bin/gmemo
sudo cp -r --force dedit-cn.py /usr/bin/dedit-cn
sudo cp -r --force gmemo.py /usr/bin/gmemo
cd ..
sudo mkdir /etc/dedit
sudo cp -r --force *.png /usr/share/pixmaps/
cd desktop
sudo cp -r --force DeltaEdit-CN.desktop /usr/share/applications
sudo cp -r --force GMemo.desktop /usr/share/applications
cd ..
cd man
sudo cp -r --force *.1.gz /usr/share/man/man1/
cd ..
cd etc
sudo cp -r --force * /etc/dedit/
cd ..
sudo chmod +x /usr/share/applications/DeltaEdit-CN.desktop
sudo chmod +x /usr/share/applications/GMemo.desktop
sudo chmod +x /usr/bin/dedit-cn
sudo chmod +x /usr/bin/gmemo
echo 'command=dedit-cn'
sudo update-mime-database /usr/share/mime
echo 'Done!'
