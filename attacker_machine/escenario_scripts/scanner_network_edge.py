import random
from scapy.all import *
import nmap
target_IP_OPC = "10.0.0.3" #port 4840

target_IP_Mod = "10.0.0.2" #port 502

target_IP_s7 ="10.0.0.1" #port 102

used_ips = []

def get_random_ip():
    valid_ip = False
    while not valid_ip:
        first_part = "172.18.0."
        last_part = str(random.randint(1,254))
        final_ip = first_part + last_part
        if final_ip not in used_ips:
            used_ips.append(final_ip)
            valid_ip = True
    return final_ip


def select_type_scan():
    scan_agurment = {"1":"-sS","2":"-sT","3":"-sU","4":"-sN","5":"-sF","6":"-sX","7":"-sA"}
    print("Select which kind of scan would you like to make:\n 1)TCP SYN scan\n2)TCP connect scan\n3)UDP Scan\n4)TCP NULL\n5)TCP FIN\n6)TCP XMAS\n7)TCP ACK")
    return scan_agurment.get(input("Option: "))

#Will make the scan of each machine with a specific ip (random generally) and with the first 10000 ports 
def scan_network(ip,machines_ips):
    scan = nmap.PortScanner()
    type_scan= select_type_scan()
    while True:
        try:
            scan.scan(hosts=machines_ips,arguments="-p1-10000 {}".format(type_scan))
            print(scan.scanstats())
        except KeyboardInterrupt:
            option = input("Would you like to finish(F) or Change type scan(C): ")
            if option == "C" or option == "c":
                type_scan= select_type_scan()
            else:
                exit()


#return IP's of the machines implicated to each case under study
def get_machines_case(case):
    case_gap = {"1":"1-3","2":"4-6","3":"7-8","4":"1-6","5":"1-8"}
    gap = case_gap.get(case)
    return "10.0.0." + gap



if __name__=="__main__":
    print("Welcome to scanner app for Entorno Doc by Sergio")
    protocols = input("Enter which case would like to activate? (1:OT, 2:IoT, 3:IT, 4:OT & IoT, 5:All): ")
    

    n_threads = 1
    #n_threads = input("How many scanners would you like to deploy?: ") ##Peding to implement####

    machines_to_scan = get_machines_case(protocols)

    src_ip = get_random_ip()
    scan_network(src_ip,machines_to_scan)


   