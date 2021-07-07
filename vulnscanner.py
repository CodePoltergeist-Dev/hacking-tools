import portscanner

targets_ip = input('[+] * Enter The Target IP to scan for vulnerable open ports: ')
port_number = int(input('[+] * Enter Amount of Ports Ypu Want to Scan(100 - first 100 ports): '))
vul_file = input('[+] * Enter Path To the File With Vulnerable Software: ')
print('\n')

target = portscanner.Portscan(targets_ip, port_number)
target.scan()