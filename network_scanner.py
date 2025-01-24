import scapy.all as scapy
import socket
import threading

# Threaded function to scan the network
def scan_network_thread(ip_range, devices_list, lock):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    for element in answered_list:
        device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        with lock:
            devices_list.append(device_info)

# Function to perform network scan with multiple threads
def scan_network(ip_range):
    devices_list = []
    lock = threading.Lock()

    threads = []
    for i in range(1, 255):  # Divide the range into subnets and use threading
        ip_range_subnet = f"{ip_range.rsplit('.', 1)[0]}.{i}/24"
        thread = threading.Thread(target=scan_network_thread, args=(ip_range_subnet, devices_list, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return devices_list

# Function to get hostname from IP
def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = "N/A"
    return hostname

# Print the results
def print_results(devices):
    print("IP Address\t\tMAC Address\t\t\tHostname")
    print("-" * 60)
    for device in devices:
        ip = device["ip"]
        mac = device["mac"]
        hostname = get_hostname(ip)
        print(f"{ip}\t\t{mac}\t\t{hostname}")

def main():
    ip_range = "192.168.1.0/24"
    print("Scanning the network, please wait...\n")
    devices = scan_network(ip_range)
    print_results(devices)

if __name__ == "__main__":
    main()
