import os
import time

def bring_sim7600_up():
    getstatus = os.popen('sudo qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode').read().split("\n\t")[1].split("'")[1]
    if getstatus == 'online':
        print("QMI Interface: Gerät ist online")
    else:
        print("QMI Interface: Offline! ...starte Modem")
        startupcommand = 'sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode="online"'
        os.system(startupcommand)
        time.sleep(2)
        getstatus2 = os.popen('sudo qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode').read().split("\n\t")[1].split("'")[1]
        if getstatus2 == 'online':
            print("QMI Interface: Gerät ist nun online")
        else:
            print("QMI Interface: Gerätefehler - konnte nicht aktiviert werden")
            
        
def set_raw_ip_mode():
    com0 = 'sudo ip link set wwan0 down'
    com1 = 'echo Y | sudo tee /sys/class/net/wwan0/qmi/raw_ip'
    com2 = 'sudo ip link set wwan0 up'
    print("QMI Interface: Set RAW IP Mode")
    os.system(com0)
    os.system(com1)
    os.system(com2)
    print("QMI Interface: Set RAW IP Mode complete")
    
def connect_qmi():
    com_connect = 'sudo qmicli --device=/dev/cdc-wdm0 --device-open-proxy --wds-start-network="ip-type=4,apn=gprs.swisscom.ch" --client-no-release-cid'
    com_dhcp = 'sudo udhcpc -i wwan0'
    print("QMI Interface: Connect QMI")
    os.system(com_connect)
    print("QMI Interface: Connect start wwan0")
    os.system(com_dhcp)
     
if __name__ == "__main__":
    print("QMI Interface: Start Setup")
    bring_sim7600_up()
    time.sleep(2)
    set_raw_ip_mode()
    time.sleep(2)
    connect_qmi()
    print("QMI Interface: Setup Complete")