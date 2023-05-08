# python-pi-cellular-setup

sudo apt-get update

sudo apt-get upgrade

sudo apt-get install libqmi-utils

sudo apt-get install udhcpc


sudo cp cellular.service /lib/systemd/system/cellular.service

sudo chmod 644 /lib/systemd/system/cellular.service

sudo systemctl daemon-reload

sudo systemctl enable cellular.service

sudo reboot