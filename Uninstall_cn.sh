
#!/bin/bash
sudo rm -rf /usr/bin/dedit-cn
sudo rm -rf /usr/bin/gmemo
sudo rm -rf /usr/share/applications/GMemo.desktop
sudo rm -rf /usr/share/applications/DeltaEdit-CN.desktop
sudo rm -rf /usr/share/man/man1/dedit.1.gz
sudo rm -rf /usr/share/man/man1/gmemo.1.gz
sudo rmdir /etc/dedit
sudo update-mime-database /usr/share/mime
echo 'Done!'
