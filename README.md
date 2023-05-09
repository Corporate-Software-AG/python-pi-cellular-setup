# python-pi-cellular-setup

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install libqmi-utils

sudo apt-get install udhcpc

sudo systemctl unmask ModemManager.service

sudo systemctl disable ModemManager.service

sudo cp cellular.service /lib/systemd/system/cellular.service

sudo chmod 644 /lib/systemd/system/cellular.service

sudo systemctl daemon-reload

sudo systemctl enable cellular.service

Fill out the correct values in env.conf and move it to the boot directory with "sudo mv env.conf /boot/env.conf"

it will show an error message which can be ignored

sudo reboot
