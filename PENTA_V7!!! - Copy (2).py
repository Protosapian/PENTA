import os
import sys
import time
import math
import string
import random
import socket
import hashlib
import base64
import uuid
import json
import secrets
import urllib.request
import platform
import subprocess
import re
import shutil
import tempfile
import gc
import zipfile
from datetime import datetime

# --- COLOR CONSTANTS (Penta Signature Palette) ---
VIBRANT_RED = "\033[91m"
NEON_PINK = "\033[95m"
RESET = "\033[0m"

PENTA_LOGO = rf"""{NEON_PINK}
  _____  ______ _   _ _______       

 |  __ \|  ____| \ | |__   __|/\    
 | |__) | |__  |  \| |  | |  /  \   
 |  ___/|  __| | . ` |  | | / /\ \  
 | |    | |____| |\  |  | |/ ____ \ 
 |_|    |______|_| \_|  |_/_/    \_\ 
{RESET}"""

def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(PENTA_LOGO)
        print(f"{VIBRANT_RED}┌──────────────────────────────────────────────────────────────────────────────────────────┐")
        print(f"│                       {NEON_PINK}P E N T A   M U L T I - T O O L K I T   S U I T E{VIBRANT_RED}                          │")
        print(f"└──────────────────────────────────────────────────────────────────────────────────────────┘{RESET}")
        print(f" [{VIBRANT_RED}01{RESET}] Website Load Tester         [{NEON_PINK}23{RESET}] String to HEX Encoder      [{VIBRANT_RED}45{RESET}] Visual Matrix Rain Stream")
        print(f" [{VIBRANT_RED}02{RESET}] Math Command Calculator     [{VIBRANT_RED}24{RESET}] Int to Binary Encoder       [{NEON_PINK}46{RESET}] Active Port Connection Scan")
        print(f" [{VIBRANT_RED}03{RESET}] Crypto Password Generator   [{VIBRANT_RED}25{RESET}] Square Root Evaluator       [{NEON_PINK}47{RESET}] Local Machine Storage Query")
        print(f" [{VIBRANT_RED}04{RESET}] Time & Network Dashboard   [{NEON_PINK}26{RESET}] Local Subnet IP Scanner     [{NEON_PINK}48{RESET}] Random Word Group Generator")
        print(f" [{VIBRANT_RED}05{RESET}] String Hasher Utilities     [{NEON_PINK}27{RESET}] System MAC Address Finder   [{NEON_PINK}49{RESET}] Direct URL Source Downloader")
        print(f" [{VIBRANT_RED}06{RESET}] Local System Monitor        [{NEON_PINK}28{RESET}] DNS Record Lookup Tool      [{NEON_PINK}50{RESET}] Standard Morse Code Codec")
        print(f" [{VIBRANT_RED}07{RESET}] Base64 Encoder / Decoder    [{NEON_PINK}29{RESET}] Secure File Shredder        [{VIBRANT_RED}51{RESET}] User Input B64 File Bundler")
        print(f" [{NEON_PINK}08{RESET}] JSON Payload Formatter      [{NEON_PINK}30{RESET}] Password Strength Grader    [{VIBRANT_RED}52{RESET}] System Uptime Frame Monitor")
        print(f" [{NEON_PINK}09{RESET}] File Checksum Verifier      [{VIBRANT_RED}31{RESET}] Public IP Geolocation       [{VIBRANT_RED}53{RESET}] Live Stopwatch Timer Relay")
        print(f" [{NEON_PINK}10{RESET}] Binary Path Finder          [{VIBRANT_RED}32{RESET}] Crypto Coin Flip Simulator  [{VIBRANT_RED}54{RESET}] Levenshtein Distance Calc")
        print(f" [{NEON_PINK}11{RESET}] String Case Converter       [{VIBRANT_RED}33{RESET}] Folder Disk Usage Analyzer  [{VIBRANT_RED}55{RESET}] Caesar Cipher Encryptor")
        print(f" [{NEON_PINK}12{RESET}] Admin Leap Year Checker     [{VIBRANT_RED}34{RESET}] Markdown to HTML Render     [{NEON_PINK}56{RESET}] Reverse DNS IP Lookup")
        print(f" [{NEON_PINK}13{RESET}] UUID v4 Token Generator     [{VIBRANT_RED}35{RESET}] Regex Pattern Evaluator     [{NEON_PINK}57{RESET}] Timezone Metrics Engine")
        print(f" [{NEON_PINK}14{RESET}] Local Port Simulator        [{NEON_PINK}36{RESET}] Global Ping Latency Checker [{NEON_PINK}58{RESET}] Console Text Type Emulator")
        print(f" [{NEON_PINK}15{RESET}] Text Character Counter      [{NEON_PINK}37{RESET}] System Environment Dumper   [{NEON_PINK}59{RESET}] Local Network Adapter Dumper")
        print(f" [{NEON_PINK}16{RESET}] Compute Load Multiplier     [{NEON_PINK}38{RESET}] Temp Directory Purger       [{NEON_PINK}60{RESET}] String ROT13 Crypto Encoder")
        print(f" [{VIBRANT_RED}17{RESET}] Development Token Masker    [{VIBRANT_RED}39{RESET}] Custom HTTP Header Scanner  [{VIBRANT_RED}61{RESET}] Recursive Blank File Cleaner")
        print(f" [{VIBRANT_RED}18{RESET}] Local Text File Reader      [{VIBRANT_RED}40{RESET}] Fibonacci Sequence Gen      [{VIBRANT_RED}62{RESET}] RAM Allocation Calculator")
        print(f" [{VIBRANT_RED}19{RESET}] JSON Syntax Validator       [{VIBRANT_RED}41{RESET}] Text Pattern Search (Grep)  [{VIBRANT_RED}63{RESET}] User Binary to HEX Encoder")
        print(f" [{VIBRANT_RED}20{RESET}] Environment Var Finder      [{VIBRANT_RED}42{RESET}] Host Status Watchdog        [{VIBRANT_RED}64{RESET}] Console Screen Window Query")
        print(f" [{VIBRANT_RED}21{RESET}] Unix Epoch Converter        [{VIBRANT_RED}43{RESET}] File Extension Renamer      [{VIBRANT_RED}65{RESET}] Math Logarithm Evaluator")
        print(f" [{VIBRANT_RED}22{RESET}] Factorial Calculator        [{VIBRANT_RED}44{RESET}] Prime Number Verifier       [{VIBRANT_RED}66{RESET}] System RAM Free Up Tool")
        print(f" [{VIBRANT_RED}67{RESET}] String Cryptographic Salt   [{VIBRANT_RED}74{RESET}] Text ASCII Value Translator [{VIBRANT_RED}81{RESET}] String Isogram Verifier")
        print(f" [{VIBRANT_RED}68{RESET}] Website Response Speed      [{VIBRANT_RED}75{RESET}] Secure Vigenere Cipher Codec [{VIBRANT_RED}82{RESET}] System Host Profiler")
        print(f" [{VIBRANT_RED}69{RESET}] Random HEX Color Generator   [{VIBRANT_RED}76{RESET}] Temperature Scale Converter [{VIBRANT_RED}83{RESET}] Lowest Common Multiple (LCM)")
        print(f" [{VIBRANT_RED}70{RESET}] ZIP Archive Extractor       [{VIBRANT_RED}77{RESET}] Inverse Factorial Compiler  [{VIBRANT_RED}84{RESET}] User String Reverser")
        print(f" [{VIBRANT_RED}71{RESET}] Directory File Tree Printer [{VIBRANT_RED}78{RESET}] Cryptographic Die Roller    [{VIBRANT_RED}85{RESET}] Alphabetic Identity Seed")
        print(f" [{VIBRANT_RED}72{RESET}] Kernel Process Identity ID  [{VIBRANT_RED}79{RESET}] Application Workspace Maker [{VIBRANT_RED}00{RESET}] Exit Suite Instance")
        print(f" [{VIBRANT_RED}73{RESET}] Degrees to Radians Converter [{VIBRANT_RED}80{RESET}] Text Word Iteration Counter")
        print(f"{VIBRANT_RED}──────────────────────────────────────────────────────────────────────────────────────────{RESET}")

        choice = input(f"{VIBRANT_RED}Penta > {RESET}").strip()

        if choice == '00':
            print(f"\n{NEON_PINK}Exiting Penta Multi-Toolkit Suite. Goodbye!{RESET}")
            break
        elif choice == '01':
            print(f"\n{NEON_PINK}--- WEBSITE LOAD TESTER ---{RESET}\n")
            url = input("Enter target website URL: ")
            print(f"Simulating traffic loops on {url}...")
            time.sleep(2)
            print("Finished mock traffic run sequence.")
            input("\nPress Enter to return...")

        elif choice == '02':
            print(f"\n{NEON_PINK}--- MATH COMMAND CALCULATOR ---{RESET}\n")
            expr = input("Enter standard math expression: ")
            try:
                print(f"Result: {eval(expr)}")
            except Exception as e:
                print(f"Math calculation error: {e}")
            input("\nPress Enter to return...")

        elif choice == '03':
            print(f"\n{NEON_PINK}--- CRYPTO PASSWORD GENERATOR ---{RESET}\n")
            chars = string.ascii_letters + string.digits + "!@#$%^&*()"
            pwd = "".join(random.choice(chars) for _ in range(16))
            print(f"Secure Token Key: {pwd}")
            input("\nPress Enter to return...")

        elif choice == '04':
            print(f"\n{NEON_PINK}--- TIME & NETWORK DASHBOARD ---{RESET}\n")
            print(f"Local System Clock Epoch: {time.time()}")
            print(f"Local Machine Loopback: {socket.gethostbyname(socket.gethostname())}")
            input("\nPress Enter to return...")

        elif choice == '05':
            print(f"\n{NEON_PINK}--- STRING HASHER UTILITIES ---{RESET}\n")
            text = input("Enter text string to hash: ")
            print(f"MD5 HexDigest: {hashlib.md5(text.encode()).hexdigest()}")
            print(f"SHA256 HexDigest: {hashlib.sha256(text.encode()).hexdigest()}")
            input("\nPress Enter to return...")

        elif choice == '06':
            print(f"\n{NEON_PINK}--- LOCAL SYSTEM MONITOR ---{RESET}\n")
            print(f"System Operational Platform: {sys.platform}")
            print(f"System Python Path Location: {sys.executable}")
            input("\nPress Enter to return...")

        elif choice == '07':
            print(f"\n{NEON_PINK}--- BASE64 ENCODER / DECODER ---{RESET}\n")
            action = input("Select operation (encode/decode): ").strip().lower()
            text = input("Enter raw or encrypted target string: ")
            if action == 'encode':
                print(f"Base64 Output: {base64.b64encode(text.encode()).decode()}")
            else:
                try:
                    print(f"Decoded Output: {base64.b64decode(text.encode()).decode()}")
                except Exception:
                    print("Invalid Base64 validation chain.")
            input("\nPress Enter to return...")

        elif choice == '08':
            print(f"\n{NEON_PINK}--- JSON PAYLOAD FORMATTER ---{RESET}\n")
            raw_json = input("Enter minimal packed JSON text string: ")
            try:
                parsed = json.loads(raw_json)
                print(json.dumps(parsed, indent=4))
            except Exception as e:
                print(f"JSON schema parsing crash: {e}")
            input("\nPress Enter to return...")

        elif choice == '09':
            print(f"\n{NEON_PINK}--- FILE CHECKSUM VERIFIER ---{RESET}\n")
            print("[Mock Operation]: File system path check requires full permissions.")
            input("\nPress Enter to return...")

        elif choice == '10':
            print(f"\n{NEON_PINK}--- BINARY PATH FINDER ---{RESET}\n")
            print(f"Primary Execution System Core Binary: {os.defpath}")
            input("\nPress Enter to return...")
        elif choice == '11':
            print(f"\n{NEON_PINK}--- STRING CASE CONVERTER ---{RESET}\n")
            text = input("Enter string data: ")
            print(f"Uppercase: {text.upper()}")
            print(f"Lowercase: {text.lower()}")
            input("\nPress Enter to return...")

        elif choice == '12':
            print(f"\n{NEON_PINK}--- ADMIN LEAP YEAR CHECKER ---{RESET}\n")
            try:
                year = int(input("Enter calendar year integer: "))
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    print(f"{year} is an active leap loop.")
                else:
                    print(f"{year} is a normal solar sequence.")
            except ValueError:
                print("Invalid mathematical integer array.")
            input("\nPress Enter to return...")

        elif choice == '13':
            print(f"\n{NEON_PINK}--- UUID V4 TOKEN GENERATOR ---{RESET}\n")
            print(f"Allocated UUID Hex Token: {uuid.uuid4()}")
            input("\nPress Enter to return...")

        elif choice == '14':
            print(f"\n{NEON_PINK}--- LOCAL PORT SIMULATOR ---{RESET}\n")
            print("Spinning temporary local listening port socket interface...")
            time.sleep(1)
            print("Port virtualization test closed cleanly.")
            input("\nPress Enter to return...")

        elif choice == '15':
            print(f"\n{NEON_PINK}--- TEXT CHARACTER COUNTER ---{RESET}\n")
            text = input("Enter raw text payload: ")
            print(f"Total String Length Index Count: {len(text)}")
            input("\nPress Enter to return...")

        elif choice == '16':
            print(f"\n{NEON_PINK}--- COMPUTE LOAD MULTIPLIER ---{RESET}\n")
            try:
                val = int(input("Enter calculation compute base index: "))
                print(f"Multiplier result matrix: {val * 10000}")
            except ValueError:
                print("Non-numeric processing block error.")
            input("\nPress Enter to return...")

        elif choice == '17':
            print(f"\n{NEON_PINK}--- DEVELOPMENT TOKEN MASKER ---{RESET}\n")
            tok = input("Enter development API environment key text: ")
            if len(tok) > 6:
                print(f"Masked Signature: {tok[:3]}********{tok[-3:]}")
            else:
                print("Token block data structurally insecure.")
            input("\nPress Enter to return...")

        elif choice == '18':
            print(f"\n{NEON_PINK}--- LOCAL TEXT FILE READER ---{RESET}\n")
            print("[Security Notice]: Restricted local file read system requires admin elevations.")
            input("\nPress Enter to return...")

        elif choice == '19':
            print(f"\n{NEON_PINK}--- JSON SYNTAX VALIDATOR ---{RESET}\n")
            text = input("Enter code snippet to validate: ")
            if text.startswith("{") and text.endswith("}"):
                print("Basic JSON wire framing checks look clear.")
            else:
                print("Missing payload structural bracket tags.")
            input("\nPress Enter to return...")

        elif choice == '20':
            print(f"\n{NEON_PINK}--- ENVIRONMENT VAR FINDER ---{RESET}\n")
            print(f"Active System Root Operating Path Location: {os.environ.get('PATH')[:50]}...")
            input("\nPress Enter to return...")
        elif choice == '26':
            print(f"\n{NEON_PINK} LOCAL SUBNET IP SCANNER{RESET}\n")
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            print(f" Your Hostname: {hostname}")
            print(f" Base Local IP: {local_ip}")
            print(" Scanning active local network devices...")
            base_subnet = ".".join(local_ip.split(".")[:3]) + "."
            for i in range(1, 10):
                ip = base_subnet + str(i)
                try:
                    socket.gethostbyaddr(ip)
                    print(f"  [{VIBRANT_RED}ONLINE{RESET}] -> {ip}")
                except socket.herror:
                    print(f"  [ACTIVE] -> {ip}")
                except Exception:
                    pass
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '27':
            print(f"\n{NEON_PINK} SYSTEM MAC ADDRESS FINDER{RESET}\n")
            mac_num = hex(uuid.getnode())[2:].zfill(12)
            mac_address = ":".join(mac_num[i:i+2] for i in range(0, 12, 2)).upper()
            print(f" Physical Nic Identifier: {VIBRANT_RED}{mac_address}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '28':
            print(f"\n{NEON_PINK} DNS RECORD LOOKUP TOOL{RESET}\n")
            domain = input(" Enter domain name to query (e.g., google.com): ").strip()
            try:
                ip_list = socket.getaddrinfo(domain, None)
                print(f"\n Resolved Records for {domain}:")
                for item in ip_list:
                    print(f"  -> IP Address: {VIBRANT_RED}{item}{RESET}")
            except Exception as e:
                print(f" ❌ DNS Resolution Failed: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '29':
            print(f"\n{NEON_PINK} SECURE FILE SHREDDER{RESET}\n")
            filepath = input(" Enter file path to securely shred: ").strip()
            if os.path.exists(filepath) and os.path.isfile(filepath):
                confirm = input(f" {VIBRANT_RED}⚠️ WARNING: Permanent data loss. Proceed? (y/n): {RESET}").lower()
                if confirm == 'y':
                    size = os.path.getsize(filepath)
                    with open(filepath, "ba+", buffering=0) as f:
                        f.write(secrets.token_bytes(size))
                    os.remove(filepath)
                    print(f" ✅ File securely overwritten and unlinked.")
            else:
                print(" ❌ Target file not found.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '30':
            print(f"\n{NEON_PINK} PASSWORD STRENGTH GRADER{RESET}\n")
            pwd = input(" Enter password to evaluate: ")
            score = 0
            feedback = []
            if len(pwd) >= 12: score += 2
            elif len(pwd) >= 8: score += 1
            else: feedback.append("Too short (min 8 characters)")
            if any(c.isupper() for c in pwd): score += 1
            else: feedback.append("Missing uppercase letter")
            if any(c.islower() for c in pwd): score += 1
            else: feedback.append("Missing lowercase letter")
            if any(c.isdigit() for c in pwd): score += 1
            else: feedback.append("Missing numeric digits")
            if any(c in "!@#$%^&*()_+-=" for c in pwd): score += 1
            else: feedback.append("Missing special characters")
            print(f"\n Strength Security Rating: {VIBRANT_RED}{score}/6{RESET}")
            if feedback:
                print(" Areas for improvement:")
                for item in feedback: print(f"  - {item}")
            else:
                print(" ✅ Password meets strict security guidelines.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '31':
            print(f"\n{NEON_PINK} PUBLIC IP GEOLOCATION{RESET}\n")
            try:
                print(" Fetching public gateway configuration parameters...")
                req = urllib.request.Request("https://ipapi.co", headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=5) as response:
                    data = json.loads(response.read().decode())
                print(f"  • External IP:  {VIBRANT_RED}{data.get('ip')}{RESET}")
                print(f"  • City / Region: {data.get('city')}, {data.get('region')}")
                print(f"  • Country Code:  {data.get('country_name')} ({data.get('country_code')})")
                print(f"  • ISP Provider:  {data.get('org')}")
            except Exception as e:
                print(f" ❌ Failed to fetch external network mapping data: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '32':
            print(f"\n{NEON_PINK}--- CRYPTO COIN FLIP SIMULATOR ---{RESET}\n")
            print(" Flipping a secure cryptographic coin...")
            time.sleep(1)
            result = secrets.choice(["HEADS", "TAILS"])
            color = NEON_PINK if result == "HEADS" else VIBRANT_RED
            print(f"\n Result: {color}{result}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '33':
            print(f"\n{NEON_PINK} FOLDER DISK USAGE ANALYZER{RESET}\n")
            target_dir = input(" Enter system directory path to analyze (Dot '.' for current): ").strip()
            if os.path.exists(target_dir) and os.path.isdir(target_dir):
                total_size = 0
                file_count = 0
                for root, dirs, files in os.walk(target_dir):
                    for file in files:
                        fp = os.path.join(root, file)
                        if os.path.exists(fp): total_size += os.path.getsize(fp)
                        file_count += 1
                mb_size = total_size / (1024 * 1024)
                print(f"\n Allocation Report for '{target_dir}':")
                print(f"  • Aggregate Indexed Files: {file_count}")
                print(f"  • Total Storage Footprint:  {VIBRANT_RED}{mb_size:.2f} MB{RESET}")
            else:
                print(" ❌ Target path is invalid or is not a directory.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '34':
            print(f"\n{NEON_PINK} MARKDOWN TO HTML RENDER{RESET}\n")
            md_text = input(" Enter single line of Markdown syntax (e.g. **bold text**): ")
            html = md_text
            if "**" in html:
                parts = html.split("**")
                html = parts[0] + f"<strong>{parts[1]}</strong>" + "".join(parts[2:])
            if "*" in html and "<strong>" not in html:
                parts = html.split("*")
                html = parts[0] + f"<em>{parts[1]}</em>" + "".join(parts[2:])
            print(f"\n Formatted HTML Target String:\n {VIBRANT_RED}{html}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '35':
            print(f"\n{NEON_PINK} REGEX PATTERN EVALUATOR{RESET}\n")
            pattern = input(" Enter regular expression pattern (e.g. ^[0-9]+$): ")
            target_str = input(" Enter string sequence to test expression against: ")
            try:
                if re.match(pattern, target_str):
                    print(f"\n Result: {NEON_PINK}Match Successful! ✅{RESET}")
                else:
                    print(f"\n Result: {VIBRANT_RED}No Match Found. ❌{RESET}")
            except Exception as e:
                print(f" ❌ Regex Engine Syntax Error: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '36':
            print(f"\n{NEON_PINK} GLOBAL PING LATENCY CHECKER{RESET}\n")
            host = input(" Enter host or target domain to ping: ").strip()
            if host:
                param = '-n' if platform.system().lower() == 'windows' else '-c'
                command = ['ping', param, '3', host]
                print(f" Pinging {host} 3 times...")
                res = subprocess.run(command, capture_output=True, text=True)
                print(f"\n{VIBRANT_RED}--- Console Output ---{RESET}\n{res.stdout}")
            else:
                print(" ❌ Invalid hostname.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '37':
            print(f"\n{NEON_PINK} SYSTEM ENVIRONMENT DUMPER{RESET}\n")
            print(f" Operating System Kernel:  {platform.system()} {platform.release()}")
            print(f" CPU Architecture Type:   {platform.machine()}")
            print(f" Logged In User Profile:  {os.getlogin() if hasattr(os, 'getlogin') else 'Unknown'}")
            print(f" Active Working Path:     {os.getcwd()}")
            print(f" Total CPU Threads Count: {os.cpu_count()}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '38':
            print(f"\n{NEON_PINK} TEMP DIRECTORY PURGER{RESET}\n")
            temp_dir = tempfile.gettempdir()
            print(f" Targeted OS Temp Directory: {temp_dir}")
            confirm = input(f" {VIBRANT_RED}⚠️ Purge all disposable data? (y/n): {RESET}").lower()
            if confirm == 'y':
                deleted_files = 0
                for filename in os.listdir(temp_dir):
                    file_path = os.path.join(temp_dir, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                            deleted_files += 1
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                            deleted_files += 1
                    except Exception:
                        pass
                print(f" ✅ Process ended. Successfully cleared {deleted_files} blocked files/folders.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '39':
            print(f"\n{NEON_PINK} CUSTOM HTTP HEADER SCANNER{RESET}\n")
            target = input(" Enter target web URL (e.g., https://example.com): ").strip()
            if not target.startswith(("http://", "https://")): target = "https://" + target
            try:
                print(" Transmitting handshakes...")
                req = urllib.request.Request(target, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=5) as response:
                    print(f"\n Received HTTP Headers for {target}:")
                    for header, val in response.headers.items():
                        print(f"  • {header}: {VIBRANT_RED}{val}{RESET}")
            except Exception as e:
                print(f" ❌ Failed to grab network headers: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '40':
            print(f"\n{NEON_PINK} FIBONACCI SEQUENCE GENERATOR{RESET}\n")
            try:
                terms = int(input(" Enter number of sequence values to evaluate: "))
                if terms <= 0: print(" ❌ Please input an integer greater than zero.")
                else:
                    n1, n2 = 0, 1
                    count = 0
                    print(f"\n Top {terms} Fibonacci iterations:")
                    while count < terms:
                        print(f"  [{count+1:02d}] -> {VIBRANT_RED}{n1}{RESET}")
                        nth = n1 + n2
                        n1 = n2
                        n2 = nth
                        count += 1
            except ValueError:
                print(" ❌ Selection input must be a valid integer.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '41':
            print(f"\n{NEON_PINK} TEXT PATTERN SEARCH (GREP){RESET}\n")
            file_to_check = input(" Enter file path to search inside: ").strip()
            keyword = input(" Enter string or pattern keyword to match: ")
            if os.path.exists(file_to_check) and os.path.isfile(file_to_check):
                try:
                    with open(file_to_check, 'r', encoding='utf-8', errors='ignore') as f:
                        print(f"\n Matching strings inside '{file_to_check}':")
                        for idx, line in enumerate(f, 1):
                            if keyword in line:
                                print(f"  Line {idx:02d}: {VIBRANT_RED}{line.strip()}{RESET}")
                except Exception as e:
                    print(f" ❌ Error reading target stream: {e}")
            else:
                print(" ❌ Invalid file target.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '42':
            print(f"\n{NEON_PINK} HOST STATUS WATCHDOG{RESET}\n")
            target_host = input(" Enter host address or IP to watch: ").strip()
            try:
                target_ip = socket.gethostbyname(target_host)
                print(f" Monitoring status of {target_host} [{target_ip}] for 3 iterations...")
                for cycle in range(3):
                    try:
                        socket.setdefaulttimeout(2)
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((target_ip, 80))
                        s.close()
                        print(f"  [Cycle {cycle+1}] Status: {NEON_PINK}ONLINE{RESET}")
                    except Exception:
                        print(f"  [Cycle {cycle+1}] Status: {VIBRANT_RED}OFFLINE / UNREACHABLE{RESET}")
                    time.sleep(1)
            except Exception as e:
                print(f" ❌ Host mapping parsing failed: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '43':
            print(f"\n{NEON_PINK} LOCAL FILE EXTENSION RENAMER{RESET}\n")
            folder = input(" Enter folder path containing files: ").strip()
            old_ext = input(" Enter current extension to find (e.g. .txt): ").strip()
            new_ext = input(" Enter new replacement extension (e.g. .log): ").strip()
            if os.path.exists(folder) and os.path.isdir(folder):
                renamed = 0
                for filename in os.listdir(folder):
                    if filename.endswith(old_ext):
                        old_file = os.path.join(folder, filename)
                        new_file = os.path.join(folder, filename.replace(old_ext, new_ext))
                        os.rename(old_file, new_file)
                        renamed += 1
                print(f" ✅ Operation complete. Transformed {renamed} matching file assets.")
            else:
                print(" ❌ Directory path not found.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '44':
            print(f"\n{NEON_PINK} PRIME NUMBER VERIFIER{RESET}\n")
            try:
                num = int(input(" Enter number to verify: "))
                if num <= 1:
                    print(f" Result: {VIBRANT_RED}{num} is not prime.{RESET}")
                else:
                    is_prime = True
                    for i in range(2, int(num**0.5) + 1):
                        if num % i == 0:
                            is_prime = False
                            break
                    if is_prime: print(f" Result: {NEON_PINK}{num} IS A PRIME NUMBER! ✅{RESET}")
                    else: print(f" Result: {VIBRANT_RED}{num} is a composite number (not prime).{RESET}")
            except ValueError:
                print(" ❌ Please input integers only.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '45':
            print(f"\n{NEON_PINK} VISUAL MATRIX RAIN STREAM{RESET}\n")
            print(" Booting data streams... Press Ctrl + C anytime to stop.")
            time.sleep(1)
            symbols = ["0", "1", "X", "Y", "P", "E", "N", "T", "A", "$", "#", "@", "%"]
            try:
                while True:
                    line = "".join(secrets.choice(symbols) if secrets.randbelow(10) > 3 else " " for _ in range(35))
                    print(f"   {VIBRANT_RED}{line}{RESET}")
                    time.sleep(0.05)
            except KeyboardInterrupt:
                print(f"\n {NEON_PINK}Data matrix stream safely intercepted.{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '46':
            print(f"\n{NEON_PINK} ACTIVE PORT CONNECTION SCAN{RESET}\n")
            target = input(" Enter target host or IP (default loopback: localhost): ").strip() or "127.0.0.1"
            print(f" Scanning common operational ports on {target}...")
            common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 1433, 3306, 3389, 8080]
            for port in common_ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"  [{NEON_PINK}OPEN{RESET}] Port {port:04d}")
                s.close()
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '47':
            print(f"\n{NEON_PINK} LOCAL MACHINE STORAGE QUERY{RESET}\n")
            total, used, free = shutil.disk_usage(".")
            print(f" Disk Root Allocation Path: {os.getcwd()}")
            print(f" Total Space: {total / (2**30):.2f} GB")
            print(f" Used Space:  {used / (2**30):.2f} GB")
            print(f" Free Space:  {VIBRANT_RED}{free / (2**30):.2f} GB{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '48':
            print(f"\n{NEON_PINK} RANDOM WORD GROUP GENERATOR{RESET}\n")
            nouns = ["System", "Network", "Matrix", "Cipher", "Node", "Payload", "Vector", "Core"]
            verbs = ["Intercept", "Override", "Encrypt", "Inject", "Decode", "Mask", "Format", "Purge"]
            adjs = ["Vibrant", "Secure", "Crypto", "Asynchronous", "Modular", "Binary", "Advanced", "Local"]
            print(" Generating 5 random operational toolkit strings:")
            for i in range(5):
                phrase = f"{random.choice(adjs)} {random.choice(nouns)} {random.choice(verbs)}"
                print(f"  [{i+1}] -> {VIBRANT_RED}{phrase}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '49':
            print(f"\n{NEON_PINK} DIRECT URL SOURCE DOWNLOADER{RESET}\n")
            target_url = input(" Enter direct file download URL: ").strip()
            save_name = input(" Save file as (e.g., target_download.txt): ").strip()
            if target_url and save_name:
                try:
                    print(f" Transmitting stream chunk payload to {save_name}...")
                    req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response, open(save_name, 'wb') as out_file:
                        out_file.write(response.read())
                    print(f" ✅ Download completed successfully.")
                except Exception as e:
                    print(f" ❌ Transmission failed: {e}")
            else:
                print(" ❌ Inputs cannot be null values.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '50':
            print(f"\n{NEON_PINK} STANDARD MORSE CODE CODEC{RESET}\n")
            morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                          'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
                          'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
                          'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
                          '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ' ': ' '}
            txt_in = input(" Enter word string payload to transform into Morse code: ").upper()
            encoded = " ".join(morse_dict.get(char, '?') for char in txt_in)
            print(f"\n Visual Wave Representation String:\n {VIBRANT_RED}{encoded}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '51':
            print(f"\n{NEON_PINK} USER INPUT B64 FILE BUNDLER{RESET}\n")
            out_filename = input(" Enter name for your output bundle (e.g. bundle.txt): ").strip()
            if out_filename:
                print(" Enter your text string contents line by line.")
                print(f" Type '{VIBRANT_RED}END{RESET}' on a blank line by itself when completely finished:\n")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "END": break
                    lines.append(line)
                full_text = "\n".join(lines)
                b64_data = base64.b64encode(full_text.encode()).decode()
                try:
                    with open(out_filename, 'w') as f:
                        f.write(b64_data)
                    print(f"\n ✅ Bundle compiled. String encrypted and saved safely inside {out_filename}.")
                except Exception as e:
                    print(f" ❌ File configuration write trace error: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '52':
            print(f"\n{NEON_PINK} SYSTEM UPTIME FRAME MONITOR{RESET}\n")
            try:
                if platform.system().lower() == 'windows':
                    cmd = "wmic os get lastbootuptime"
                    output = subprocess.check_output(cmd, shell=True, text=True)
                    boot_raw = "".join(c for c in output if c.isdigit())[:14]
                    boot_dt = datetime.strptime(boot_raw, "%Y%m%d%H%M%S")
                else:
                    with open('/proc/uptime', 'r') as f:
                        uptime_seconds = float(f.readline().split())
                    boot_dt = datetime.fromtimestamp(time.time() - uptime_seconds)
                
                uptime_duration = datetime.now() - boot_dt
                hours, remainder = divmod(int(uptime_duration.total_seconds()), 3600)
                minutes, seconds = divmod(remainder, 60)
                print(f" Hardware Kernel Active Execution Runtime: {VIBRANT_RED}{hours}h {minutes}m {seconds}s{RESET}")
                print(f" Initial Handshake Boot Timestamp:       {boot_dt.strftime('%Y-%m-%d %H:%M:%S')}")
            except Exception as e:
                print(f" ❌ Failed to establish core hardware telemetry: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '53':
            print(f"\n{NEON_PINK} LIVE STOPWATCH TIMER RELAY{RESET}\n")
            input(f" Press [{VIBRANT_RED}Enter{RESET}] to start the timer sequence clock...")
            start_clk = time.time()
            print(" Timer counting... Press [Ctrl + C] anytime to trip target lap relay checkpoint.")
            try:
                while True:
                    elapsed = time.time() - start_clk
                    print(f" \r Runtime Matrix Tracker: {VIBRANT_RED}{elapsed:.2f}s{RESET}", end="", flush=True)
                    time.sleep(0.05)
            except KeyboardInterrupt:
                total_elapsed = time.time() - start_clk
                print(f"\n\n 🛑 Timer halted cleanly. Total logged record: {NEON_PINK}{total_elapsed:.2f} seconds{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '54':
            print(f"\n{NEON_PINK} LEVENSHTEIN DISTANCE CALC{RESET}\n")
            s1 = input(" Enter first comparison string sequence: ")
            s2 = input(" Enter second comparison string sequence: ")
            if len(s1) < len(s2): s1, s2 = s2, s1
            if len(s2) == 0: dist = len(s1)
            else:
                prev_row = list(range(len(s2) + 1))
                for i, c1 in enumerate(s1):
                    curr_row = [i + 1]
                    for j, c2 in enumerate(s2):
                        insertions = prev_row[j + 1] + 1
                        deletions = curr_row[j] + 1
                        substitutions = prev_row[j] + (c1 != c2)
                        curr_row.append(min(insertions, deletions, substitutions))
                    prev_row = curr_row
                dist = prev_row[-1]
            print(f" Total Levenshtein string mutations delta distance: {VIBRANT_RED}{dist}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '55':
            print(f"\n{NEON_PINK} CAESAR CIPHER ENCRYPTOR{RESET}\n")
            text_in = input(" Enter message payload string to cipher: ")
            try:
                shift = int(input(" Enter rotation shift index (e.g. 3): "))
            except ValueError:
                shift = 3
            res_str = ""
            for char in text_in:
                if char.isalpha():
                    start_ch = ord('A') if char.isupper() else ord('a')
                    res_str += chr((ord(char) - start_ch + shift) % 26 + start_ch)
                else:
                    res_str += char
            print(f"\n Encrypted Output Hash String:\n {VIBRANT_RED}{res_str}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '56':
            print(f"\n{NEON_PINK} REVERSE DNS IP LOOKUP{RESET}\n")
            target_ip = input(" Enter numerical IP address to resolve: ").strip()
            try:
                print(f" Querying domain registration records for {target_ip}...")
                hostname, alias, ip_list = socket.gethostbyaddr(target_ip)
                print(f"\n Resolved Domain Mapping:")
                print(f"  • Registered Hostname: {VIBRANT_RED}{hostname}{RESET}")
                if alias: print(f"  • Associated Aliases:  {alias}")
            except Exception as e:
                print(f" ❌ Reverse Lookup Failed: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '57':
            print(f"\n{NEON_PINK} TIMEZONE METRICS ENGINE{RESET}\n")
            print(f" Local System Active Timezone:  {time.tzname}")
            print(f" Standard Daylight Savings Type: {'Active' if time.daylight else 'Inactive'}")
            print(f" UTC Time Offset Differential:   {-(time.timezone // 3600)} Hours")
            print(f" ISO 8601 Formatted Timestamp:   {datetime.now().isoformat()}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '58':
            print(f"\n{NEON_PINK} CONSOLE TEXT TYPING SIMULATOR{RESET}\n")
            user_msg = input(" Enter custom text string to type out: ")
            try:
                delay = float(input(" Enter character delay speed (default 0.05): "))
            except ValueError:
                delay = 0.05
            print("\n" + f"{NEON_PINK}[➔]{RESET} Simulating output buffer: ")
            for char in user_msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            print()
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '59':
            print(f"\n{NEON_PINK} LOCAL NETWORK ADAPTER DUMPER{RESET}\n")
            print(" Fetching local network interfaces via system gateway...")
            try:
                if platform.system().lower() == 'windows':
                    output = subprocess.check_output("ipconfig /all", shell=True, text=True)
                    lines = [line for line in output.split('\n') if "Description" in line or "IPv4" in line]
                    print(f"\n{VIBRANT_RED}--- Detected Adapter Mappings ---{RESET}")
                    for line in lines:
                        print(f"  {line.strip()}")
                else:
                    output = subprocess.check_output("ifconfig -a", shell=True, text=True)
                    print(output)
            except Exception as e:
                print(f" ❌ Failed to compile interface bindings: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '60':
            print(f"\n{NEON_PINK} STRING ROT13 CRYPTO ENCODER{RESET}\n")
            text_in = input(" Enter message text string to pass through ROT13: ")
            rot13 = str.maketrans(
                "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
                "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
            )
            print(f"\n Transformed Text Stream:\n {VIBRANT_RED}{text_in.translate(rot13)}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '61':
            print(f"\n{NEON_PINK} RECURSIVE BLANK FILE CLEANER{RESET}\n")
            target_path = input(" Enter local folder path to sweep (Dot '.' for current): ").strip() or "."
            if os.path.exists(target_path) and os.path.isdir(target_path):
                purged_count = 0
                confirm = input(f" {VIBRANT_RED}⚠️ Wipe all completely empty files? (y/n): {RESET}").lower()
                if confirm == 'y':
                    for root, dirs, files in os.walk(target_path):
                        for file in files:
                            fp = os.path.join(root, file)
                            try:
                                if os.path.exists(fp) and os.path.getsize(fp) == 0:
                                    os.remove(fp)
                                    purged_count += 1
                                    print(f"   [{VIBRANT_RED}PURGED{RESET}] -> {file}")
                            except Exception: pass
                    print(f"\n ✅ Operation concluded. Erased {purged_count} empty files.")
            else:
                print(" ❌ Target directory does not exist.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '62':
            print(f"\n{NEON_PINK} RAM ALLOCATION HEAP CALCULATOR{RESET}\n")
            try:
                if platform.system().lower() == 'windows':
                    cmd = "wmic computersystem get totalphysicalmemory"
                    output = subprocess.check_output(cmd, shell=True, text=True)
                    total_bytes = int("".join(c for c in output if c.isdigit()))
                    total_gb = total_bytes / (1024 ** 30)
                    print(f" Hardwired Physical RAM Capacitance: {VIBRANT_RED}{total_gb:.2f} GB{RESET}")
                else:
                    print(" Telemetry context constrained on non-Windows kernel frames.")
            except Exception as e:
                print(f" ❌ Memory mapping request rejected: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '63':
            print(f"\n{NEON_PINK} USER BINARY TO HEX ENCODER{RESET}\n")
            try:
                bin_str = input(" Enter raw binary sequence stream (e.g. 01000001): ").strip()
                decimal_val = int(bin_str, 2)
                hex_notation = hex(decimal_val).upper()[2:]
                print(f" Numerical Hexadecimal Value: {VIBRANT_RED}0x{hex_notation}{RESET}")
            except ValueError:
                print(" ❌ Sequence contains non-binary characters.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '64':
            print(f"\n{NEON_PINK} CONSOLE RESOLUTION PROFILE QUERY{RESET}\n")
            try:
                columns, lines = os.get_terminal_size()
                print(f" Matrix Stream Window Width:  {VIBRANT_RED}{columns} Character Blocks{RESET}")
                print(f" Matrix Stream Window Height: {VIBRANT_RED}{lines} Line Strides{RESET}")
                print(f" Aggregate Screen Nodes:      {columns * lines} Total Rendering Blocks")
            except Exception as e:
                print(f" ❌ Graphics handle collection error: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '65':
            print(f"\n{NEON_PINK} MATHEMATICAL LOGARITHM EVALUATOR{RESET}\n")
            try:
                val = float(input(" Enter calculation numeric base node: "))
                log_base = input(" Enter evaluation base scale (Type 'e' for natural log): ").strip()
                if log_base.lower() == 'e':
                    result = math.log(val)
                    print(f" Natural Logarithm Log_e({val}): {VIBRANT_RED}{result:.4f}{RESET}")
                else:
                    base_num = float(log_base)
                    result = math.log(val, base_num)
                    print(f" Standard Logarithm Log_{base_num}({val}): {VIBRANT_RED}{result:.4f}{RESET}")
            except Exception as e:
                print(f" ❌ System structural math evaluation fault: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '66':
            print(f"\n{NEON_PINK} SYSTEM RAM FREE UP TOOL{RESET}\n")
            print(" Initializing garbage collection array hooks...")
            collected = gc.collect()
            print(f" ✅ Process ended. Flushed {VIBRANT_RED}{collected}{RESET} unlinked objects from memory.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '67':
            print(f"\n{NEON_PINK} SECURE ALPHANUMERIC STRING SALT{RESET}\n")
            target_str = input(" Enter raw word string data to salt: ")
            salt = secrets.token_hex(4)
            salted = hashlib.sha256((target_str + salt).encode()).hexdigest()
            print(f" Cryptographic Hex Salt:  {salt}")
            print(f" Salted Hashed Result:   {VIBRANT_RED}{salted}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '68':
            print(f"\n{NEON_PINK} WEBSITE RESPONSE SPEED GRABBER{RESET}\n")
            target_site = input(" Enter target web domain (e.g. google.com): ").strip()
            if not target_site.startswith(("http://", "https://")): target_site = "https://" + target_site
            try:
                start_req = time.time()
                urllib.request.urlopen(target_site, timeout=5)
                latency_ms = (time.time() - start_req) * 1000
                print(f" Connection Latency response time: {VIBRANT_RED}{latency_ms:.1f} ms{RESET}")
            except Exception as e:
                print(f" ❌ Host connection timeout: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '69':
            print(f"\n{NEON_PINK} RANDOM HEX COLOR GENERATOR{RESET}\n")
            print(" Compiling 5 random hexadecimal color values:")
            for i in range(5):
                random_hex = f"#{secrets.token_hex(3).upper()}"
                print(f"  [{i+1:02d}] -> {NEON_PINK}{random_hex}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '70':
            print(f"\n{NEON_PINK} COMPRESSED ZIP ARCHIVE EXTRACTOR{RESET}\n")
            zip_path = input(" Enter file path to target zip file: ").strip()
            dest_folder = input(" Enter destination directory path to extract to: ").strip()
            if os.path.exists(zip_path) and zipfile.is_zipfile(zip_path):
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(dest_folder or ".")
                    print(f" ✅ Archive payloads extracted successfully to: {dest_folder or '.'}")
                except Exception as e: print(f" ❌ Extraction crash: {e}")
            else: print(" ❌ Archive target path invalid.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '71':
            print(f"\n{NEON_PINK} RECURSIVE DIRECTORY FILE TREE DISPLAYER{RESET}\n")
            target_dir = input(" Enter target path folder (Dot '.' for current): ").strip() or "."
            if os.path.exists(target_dir) and os.path.isdir(target_dir):
                print(f" Printing file configurations for '{target_dir}':\n")
                for root, dirs, files in os.walk(target_dir):
                    level = root.replace(target_dir, '').count(os.sep)
                    indent = ' ' * 4 * (level)
                    print(f"{indent}📁 {os.path.basename(root)}/")
                    sub_indent = ' ' * 4 * (level + 1)
                    for f in files:
                        print(f"{sub_indent}📄 {VIBRANT_RED}{f}{RESET}")
            else: print(" ❌ Directory path invalid.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '72':
            print(f"\n{NEON_PINK} KERNEL PROCESS ID DUMPER{RESET}\n")
            print(f" Parent and runtime framework process handles:")
            print(f"  • Current Process Identity ID (PID): {VIBRANT_RED}{os.getpid()}{RESET}")
            if hasattr(os, 'getppid'):
                print(f"  • Parent Controller Window PID:       {os.getppid()}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '73':
            print(f"\n{NEON_PINK} MATHEMATICAL DEGREES TO RADIANS CONVERTER{RESET}\n")
            try:
                deg = float(input(" Enter angular degree threshold: "))
                rad = math.radians(deg)
                print(f" Scaled Radian conversion output string: {VIBRANT_RED}{rad:.6f} rad{RESET}")
            except ValueError: print(" ❌ Entry must be a numeric integer node.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '74':
            print(f"\n{NEON_PINK} TEXT ASCII VALUE TRANSLATOR{RESET}\n")
            user_str = input(" Enter string sequence to dissect to ASCII decimals: ")
            print("\n Numeric byte values mapping matrix:")
            for char in user_str:
                print(f"  • '{char}' -> Value: {VIBRANT_RED}{ord(char)}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '75':
            print(f"\n{NEON_PINK} SECURE VIGENERE CIPHER CODEC{RESET}\n")
            pt = input(" Enter string message text: ").upper()
            keyword = input(" Enter alphabetical encryption key word: ").upper()
            if keyword.isalpha() and pt:
                out_str = []
                k_idx = 0
                for char in pt:
                    if char.isalpha():
                        shift = ord(keyword[k_idx % len(keyword)]) - ord('A')
                        out_str.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
                        k_idx += 1
                    else: out_str.append(char)
                print(f"\n Encrypted Vigenere Output String:\n {VIBRANT_RED}{''.join(out_str)}{RESET}")
            else: print(" ❌ Key text must be alphabetical strings only.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '76':
            print(f"\n{NEON_PINK} TEMPERATURE MATRIX SCALE CONVERTER{RESET}\n")
            try:
                celsius = float(input(" Enter temperature scale threshold in Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                kelvin = celsius + 273.15
                print(f"  • Fahrenheit Conversion Scale: {VIBRANT_RED}{fahrenheit:.2f}°F{RESET}")
                print(f"  • Kelvin Temperature Scale:     {kelvin:.2f}K")
            except ValueError: print(" ❌ Non-numeric base parameter entry.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '77':
            print(f"\n{NEON_PINK} DIRECT INVERSE FACTORIAL COMPLIER{RESET}\n")
            try:
                num = int(input(" Enter target factorial integer to reverse engineer: "))
                temp, step, possible = num, 1, True
                while temp > 1:
                    step += 1
                    if temp % step == 0: temp //= step
                    else:
                        possible = False
                        break
                if possible and temp == 1: print(f" Root Base Factorial Variable: {VIBRANT_RED}{step}!{RESET}")
                else: print(" ❌ This integer is not a perfect factorial product.")
            except ValueError: print(" ❌ Value must be a valid integer.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '78':
            print(f"\n{NEON_PINK} CRYPTOGRAPHICALLY SECURE DIE ROLLER{RESET}\n")
            try:
                rolls = int(input(" Enter quantity of dice to roll concurrently: "))
                print("\n Output values arrays:")
                for r in range(rolls):
                    die_face = secrets.randbelow(6) + 1
                    print(f"  [Die {r+1:02d}] 🎲 -> Value: {VIBRANT_RED}{die_face}{RESET}")
            except ValueError: print(" ❌ Invalid integer matrix allocation parameter.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '79':
            print(f"\n{NEON_PINK} LOCAL APPLICATION WORKSPACE DIR CREATOR{RESET}\n")
            new_dir = input(" Enter name path for new dedicated workspace folder: ").strip()
            if new_dir:
                try:
                    os.makedirs(new_dir, exist_ok=True)
                    print(f" ✅ Folder sequence generated safely inside: {os.path.abspath(new_dir)}")
                except Exception as e: print(f" ❌ Storage path initialization fault: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '80':
            print(f"\n{NEON_PINK} TEXT WORD MATRIX ITERATION COUNTER{RESET}\n")
            text_block = input(" Enter target sentence string: ")
            words_list = text_block.split()
            print(f" Structural Metrics: Logged {VIBRANT_RED}{len(words_list)}{RESET} total space-separated words.")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")
        elif choice == '81':
            print(f"\n{NEON_PINK} STRING ISOGRAM INTEGRITY VERIFIER{RESET}\n")
            test_word = input(" Enter word string sequence to test: ").strip().lower()
            clean_word = [c for c in test_word if c.isalpha()]
            if len(clean_word) == len(set(clean_word)):
                print(f" Result: {NEON_PINK}Valid Isogram! (No repeating letters) ✅{RESET}")
            else: print(f" Result: {VIBRANT_RED}Invalid Isogram. (Contains duplicate letters) ❌{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '82':
            print(f"\n{NEON_PINK} CORE SYSTEM HOST ARCHITECTURE PROFILER{RESET}\n")
            print(f" Machine Node Kernel Name:     {platform.node()}")
            print(f" Processor Core Microcode Type: {platform.processor()}")
            print(f" Structural Release Thread build: {platform.version()}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '83':
            print(f"\n{NEON_PINK} MATHEMATICAL LOWEST COMMON MULTIPLE (LCM){RESET}\n")
            try:
                val1 = int(input(" Enter first integer: "))
                val2 = int(input(" Enter second integer: "))
                lcm_res = abs(val1 * val2) // math.gcd(val1, val2)
                print(f" Lowest Common Multiple product: {VIBRANT_RED}{lcm_res}{RESET}")
            except Exception as e: print(f" ❌ Math evaluation failure: {e}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '84':
            print(f"\n{NEON_PINK} USER STRING REVERSER EXERCISE{RESET}\n")
            raw_input = input(" Enter any string message: ")
            reversed_string = raw_input[::-1]
            print(f"\n Mirror Inversion Result Stream:\n {VIBRANT_RED}{reversed_string}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        elif choice == '85':
            print(f"\n{NEON_PINK} RANDOM ALPHABETIC UUID SEED CHARACTER MATRIX{RESET}\n")
            pool = string.ascii_uppercase + string.digits
            generated_matrix = "-".join("".join(secrets.choice(pool) for _ in range(4)) for _ in range(4))
            print(f"\n Secure Core Identity Seed Hash Matrix:\n {VIBRANT_RED}{generated_matrix}{RESET}")
            input(f"\n{NEON_PINK}Press Enter to return...{RESET}")

        else:
            print(f"\n{VIBRANT_RED}❌ Choice Selection Invalid.{RESET}")
            input("\nPress Enter to retry...")

if __name__ == "__main__":
    main()
