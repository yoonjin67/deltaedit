#!/bin/bash
cd src
sudo touch /usr/bin/dedit-cn
sudo touch /usr/bin/dedit-ko
sudo touch /usr/bin/dedit-jp
sudo touch /usr/bin/gmemo
sudo cp -r --force dedit-ko.py /usr/bin/dedit-ko
sudo cp -r --force dedit-jp.py /usr/bin/dedit-jp
sudo cp -r --force dedit-cn.py /usr/bin/dedit-cn
sudo cp -r --force gmemo.py /usr/bin/gmemo
cd ..
sudo mkdir /etc/dedit
sudo cp -r --force *.png /usr/share/pixmaps/
cd desktop
sudo cp -r --force *.desktop /usr/share/applications
cd ..
cd man
sudo cp -r --force *.1.gz /usr/share/man/man1/
cd ..
cd etc
sudo cp -r --force * /etc/dedit/
cd ..
sudo chmod +x /usr/share/applications/DeltaEdit-*
sudo chmod +x /usr/share/applications/GMemo*
sudo chmod +x /usr/bin/dedit-*
sudo chmod +x /usr/bin/gmemo
echo 'execute command: dedit-ko  for Korean    dedit-cn     for Chinese/Taiwan   dedit-jp     for Japanese'
sudo update-mime-database /usr/share/mime
echo 'Done!'
