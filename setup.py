import os
import time

def get_status():
    try:
        return os.popen('sudo qmicli -d /dev/cdc-wdm0 --dms-get-operating-mode').read().split("\n\t")[1].split("'")[1]
    except:
        time.sleep(2)
        print("QMI Interface: Get Status Retry")
        return get_status()

def startup_comm():
    try:
        startupcommand = 'sudo qmicli -d /dev/cdc-wdm0 --dms-set-operating-mode="online"'
        os.system(startupcommand)
    except:
        time.sleep(2)
        print("QMI Interface: Starte Modem Retry")
        startup_comm()


def bring_sim7600_up():
    
    print("QMI Interface: Get Status")
    getstatus = get_status()

    if getstatus == 'online':
        print("QMI Interface: Gerät ist online")
    else:
        print("QMI Interface: Offline! ...starte Modem")
        startup_comm()
        time.sleep(2)
        getstatus2 = get_status()
        if getstatus2 == 'online':
            print("QMI Interface: Gerät ist nun online")
        else:
            print("QMI Interface: Gerätefehler - konnte nicht aktiviert werden")
            
        
def set_raw_ip_mode():
    try:
        com0 = 'sudo ip link set wwan0 down'
        com1 = 'echo Y | sudo tee /sys/class/net/wwan0/qmi/raw_ip'
        com2 = 'sudo ip link set wwan0 up'
        print("QMI Interface: Set RAW IP Mode")
        os.system(com0)
        os.system(com1)
        os.system(com2)
        print("QMI Interface: Set RAW IP Mode complete")
    except:
        print("QMI Interface: Set RAW IP Mode Retry")
        time.sleep(2)
        set_raw_ip_mode()

    
def connect_qmi():
    try:
        com_connect = 'sudo qmicli --device=/dev/cdc-wdm0 --device-open-proxy --wds-start-network="ip-type=4,apn=gprs.swisscom.ch" --client-no-release-cid'
        print("QMI Interface: Connect QMI")
        os.system(com_connect)
    except:
        print("QMI Interface: Connect QMI failed")
        time.sleep(5)
        print("QMI Interface: Connect QMI Retry")
        connect_qmi()

def connect_dhcp():
    try:
        com_dhcp = 'sudo udhcpc -i wwan0'
        print("QMI Interface: Connect start wwan0")
        os.system(com_dhcp)
    except:
        print("QMI Interface: Connect DBCH retry")
        time.sleep(2)
        connect_dhcp()


if __name__ == "__main__":
    print("QMI Interface: Start Setup")
    bring_sim7600_up()
    time.sleep(2)
    set_raw_ip_mode()
    time.sleep(2)
    connect_qmi()
    connect_dhcp()
    print("QMI Interface: Setup Complete")