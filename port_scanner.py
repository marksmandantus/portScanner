from IPy import IP
import socket # connecting

print("""
                      __                                                     
______   ____________/  |_     ______ ____ _____    ____   ____   __________ 
\____ \ /  _ \_  __ \   __\   /  ___// ___ \__  \  /    \ /    \_/ __ \_  __\|
|  |_> >  <_> )  | \/|  |     \___  \  \___ / __ \|   |  \   |  \  ___/|  | 
|   __/ \____/|__|   |__|    /____  >\___  >____  /___|  /___|  /\___  >__|   
|__|                  
 
 """)

def scan(target):
    converted_ip = check_ip(target)
    print("\n"+"[Scanning target...] \n"+str(target))
    for port in range(1, port_num):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip) #DNS

def get_banner(s):
    return s.recv(1024) #For best match with hardware and network realities, the value of bufsize should be a relatively small power of 2

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.2) #waiting time
        sock.connect((ipaddress, port)) #connecting
        try:
            banner = get_banner(sock)
            print("[+] Open Port "+str(port)+ " : " + str(banner.decode().strip("\n"))) #because there is no \r in the output
        except:
            print("[+] Open Port " + str(port))
    except:
        pass

targets = input("[-]Enter target/s to scan (split multiple targets with ,): " )
port_num = int(input("Enter number of ports that you want to scan: ")) #scanning up to the entered port number

if "," in targets:
    for ip_add in targets.split(","):
        scan(ip_add.strip(" ")) #because must be no space

else:
    scan(targets)




