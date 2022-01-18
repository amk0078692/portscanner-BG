import socket
from IPy import IP

#Second -

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[Scanning Target] ' + str(target))
    for port in range(1,1000):
        scan_port(converted_ip, port)

# if the target is ip address then this will execute
def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:                 #if the target is domain name then this will be executed
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

# main part of the program
# this will let us no if port is open or closed

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Open Port ' + str(port))
    except:                        #closed ports will not be printed by using this
        pass

#first -
# if we are importing our code in another .py file then to not execute this code again we will use this -
if __name__ == "__main__": #this is used and this program will only run if we execute portscanner.py file
    targets = input('[+] Enter Target/s To Scan(split multiple targets with ,): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
