import socket
from datetime import datetime


remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print ("-" * 40)
print ("           PORT SCANNER")
print ("      created by: sayak naskar")
print ("-" * 40)

print ("IP is: "+remoteServerIP)
print ("please wait while scanning: ")
t1 = datetime.now()

common_ports = {'21': 'FTP', '22': 'SSH', '23': 'TELNET', '25': 'SMTP', '53': 'DNS', '69': 'TFTP', '80': 'HTTP', '109': 'POP2', '110': 'POP3', '123': 'NTP', '137': 'NETBIOS-NS', '138': 'NETBIOS-DGM', '139': 'NETBIOS-SSN', '143': 'IMAP', '156': 'SQL-SERVER', '389': 'LDAP', '443': 'HTTPS', '546': 'DHCP-CLIENT', '547': 'DHCP-SERVER', '995': 'POP3-SSL', '993': 'IMAP-SSL', '2086': 'WHM/CPANEL', '2087': 'WHM/CPANEL', '2082': 'CPANEL', '2083': 'CPANEL', '3306': 'MYSQL', '8443': 'PLESK', '10000': 'VIRTUALMIN/WEBMIN'}

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((remoteServer,port))
        if result==0: 
           print ("[*] open port: ",format(port)+" /", common_ports[format(port)])
        s.close()
except:
    pass



t2= datetime.now()

total =  t2 - t1

print ('Scanning Completed in: ', total)
