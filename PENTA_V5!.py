import asyncio
import datetime
import time
import sys
import os
import secrets  
import ast      
import hashlib  
import aiohttp
import platform 
import base64   
import json     
import shutil   
import uuid     
import math     

VIBRANT_RED = "\033[38;5;196m"
NEON_PINK   = "\033[38;5;201m"
DARK_ROSE   = "\033[38;5;88m"
SOFT_PINK   = "\033[38;5;213m"
RESET       = "\033[0m"

PENTA_LOGO = rf"""{VIBRANT_RED}
┌────────────────────────────────────────────────────────┐
│  ██████╗ ███████╗███╗   ██╗████████╗█████╗  ██╗   ██╗  │
│  ██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔══██╗██║   ██║  │
│  ██████╔╝█████╗  ██╔██╗ ██║   ██║   ███████║██║   ██║  │
│  ██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══██║╚██╗ ██╔╝  │
│  ██║     ███████╗██║ ╚████║   ██║   ██║  ██║ ╚████╔╝   │
│  ╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝  ╚═══╝    │
│  [  P  E  N  T  A  _  V  5  ]                          │
└────────────────────────────────────────────────────────┘{RESET}"""

async def send_request(session, target_url, request_id, stats):
    start = time.time()
    l_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    try:
        async with session.get(target_url, timeout=5) as res:
            dur = time.time() - start
            print(f"{DARK_ROSE}[PENTA]{RESET}[{l_time}] {VIBRANT_RED}Req #{request_id:03d}:{RESET} Status: {res.status} | {dur*1000:.0f}ms")
            stats["statuses"][res.status] = stats["statuses"].get(res.status, 0) + 1
            stats["successful"] += 1
            stats["total_latency"] += dur 
    except Exception as e:
        print(f"{DARK_ROSE}[PENTA]{RESET}[{l_time}] {NEON_PINK}Req #{request_id:03d}: FAILED | Error: {str(e)}{RESET}")
        stats["failed"] += 1

async def worker(session, target_url, queue, stats):
    while not queue.empty():
        try:
            req_id = await queue.get()
            await send_request(session, target_url, req_id, stats)
        finally: proxy = queue.task_done()

async def run_load_tester():
    print(f"\n{VIBRANT_RED}┌──[ WEBSITE TESTER ]{RESET}")
    url = input(f"{VIBRANT_RED}└───►{RESET} Target URL: ").strip()
    if not url: return
    reqs = int(input(f"{NEON_PINK}├──►{RESET} Total Requests (default 1000): ") or 1000)
    users = int(input(f"{NEON_PINK}└──►{RESET} Concurrent Users (default 50): ") or 50)
    stats = {"successful": 0, "failed": 0, "statuses": {}, "total_latency": 0.0}
    queue = asyncio.Queue()
    for i in range(1, reqs + 1): await queue.put(i)
    start = time.time()
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=users), headers={"User-Agent": "PENTA_V5"}) as session:
        await asyncio.gather(*[asyncio.create_task(worker(session, url, queue, stats)) for _ in range(users)])
    print(f"\nTime: {time.time() - start:.2f}s | Success: {stats['successful']} | Failed: {stats['failed']}")

def run_calculator():
    print(f"\n{NEON_PINK}┌──[ CALCULATOR ]{RESET}")
    while True:
        expr = input(f"{NEON_PINK}Calc ═► {RESET}").strip()
        if expr.lower() in ['exit', 'quit', 'q']: break
        try:
            if all(c in "0123456789+-*/(). " for c in expr):
                print(f"{SOFT_PINK}Result ──►{RESET} {eval(compile(ast.parse(expr, mode='eval'), '<string>', 'eval'), {'__builtins__': {}}, {})}")
        except Exception as e: print(f"Error: {e}")

def run_password_generator():
    print(f"\n{VIBRANT_RED}┌──[ CRYPTO-PASS GENERATOR ]{RESET}")
    length = int(input(f"{VIBRANT_RED}└───►{RESET} Length (default 16): ") or 16)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    print(f"{NEON_PINK}Key: {''.join(secrets.choice(chars) for _ in range(length))}{RESET}")

def run_clock_dashboard():
    print(f"\n{SOFT_PINK}┌──[ TIME & LOOPBACK DIAGNOSTIC ]{RESET}")
    print(f"Local: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Loopback IP: 127.0.0.1 | Status: Active")

def run_console_utilities():
    print(f"\n{NEON_PINK}┌──[ STRING HASHER ]{RESET}")
    txt = input("Text to SHA-256: ").strip()
    if txt: print(f"Hash: {hashlib.sha256(txt.encode()).hexdigest()}")

def run_system_monitor():
    print(f"\n{VIBRANT_RED}┌──[ SYSTEM MONITOR ]{RESET}")
    print(f"OS: {platform.system()} | Arch: {platform.machine()} | Python: {platform.python_version()}")

def run_base64_tool():
    print(f"\n{NEON_PINK}┌──[ BASE64 TOOL ]{RESET}")
    mode = input("1) Encode 2) Decode: ").strip()
    data = input("Text: ")
    if mode == '1': print(base64.b64encode(data.encode()).decode())
    elif mode == '2': print(base64.b64decode(data.encode()).decode())

def run_json_formatter():
    print(f"\n{SOFT_PINK}┌──[ JSON FORMATTER ]{RESET}")
    raw = input("Raw JSON: ").strip()
    try: print(json.dumps(json.loads(raw), indent=4))
    except Exception as e: print(f"Error: {e}")

def run_file_checksum_verifier():
    print(f"\n{VIBRANT_RED}┌──[ CHECKSUM VERIFIER ]{RESET}")
    path = input("File path: ").strip()
    if not os.path.exists(path): return
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(4096), b""): h.update(b)
    print(f"SHA-256: {h.hexdigest()}")

# --- NEW ADDED TOOLS START HERE ---
def run_text_reader():
    print(f"\n{NEON_PINK}┌──[ LOCAL TEXT FILE READER ]{RESET}")
    path = input("Enter file path: ").strip()
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f: print(f.read())
        except Exception as e: print(f"Error reading: {e}")
    else: print("File not found.")

def run_json_validator():
    print(f"\n{VIBRANT_RED}┌──[ JSON FILE SYNTAX VALIDATOR ]{RESET}")
    path = input("Enter .json file path: ").strip()
    if os.path.exists(path):
        try:
            with open(path, 'r') as f: json.load(f)
            print(f"{SOFT_PINK}Valid JSON Structure!{RESET}")
        except Exception as e: print(f"Invalid JSON Syntax: {e}")
    else: print("File not found.")

def run_env_finder():
    print(f"\n{SOFT_PINK}┌──[ SYSTEM ENVIRONMENT VARIABLE FINDER ]{RESET}")
    var = input("Enter Variable Key (e.g. PATH): ").strip()
    val = os.getenv(var)
    print(f"Value: {val if val else 'Variable Key not found'}")

def run_epoch_converter():
    print(f"\n{NEON_PINK}┌──[ UNIX EPOCH TIMESTAMP CONVERTER ]{RESET}")
    try:
        ts = int(input("Enter Epoch timestamp: ").strip())
        print(f"Date: {datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e: print(f"Invalid format: {e}")

def run_factorial_calc():
    print(f"\n{VIBRANT_RED}┌──[ FACTORIAL MATHEMATICS CALCULATOR ]{RESET}")
    try:
        num = int(input("Enter whole integer: ").strip())
        print(f"Factorial result: {math.factorial(num)}")
    except Exception as e: print(f"Invalid whole integer: {e}")
# ==========================================
# EXTRA TOOLS MODULE (16 TO 25)
# ==========================================
def run_path_finder():
    print(f"\n{SOFT_PINK}┌──[ BINARY PATH FINDER ]{RESET}")
    binary = input("Enter command name (e.g., git, curl): ").strip()
    if not binary: return
    location = shutil.which(binary)
    if location: print(f"Path: {location}")
    else: print("Binary not found in environment PATH.")

def run_case_converter():
    print(f"\n{VIBRANT_RED}┌──[ TEXT CASE CONVERTER ]{RESET}")
    text = input("Enter text string: ")
    print(f"UPPER: {text.upper()} | lower: {text.lower()} | snake: {text.lower().replace(' ', '_')}")

def run_leap_checker():
    print(f"\n{NEON_PINK}┌──[ LEAP YEAR CHECKER ]{RESET}")
    try:
        year = int(input("Enter calendar year: ") or datetime.datetime.now().year)
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        print(f"Result: {year} is {'IS' if is_leap else 'NOT'} a Leap Year.")
    except ValueError: print("Invalid numeric formatting.")

def run_uuid_generator():
    print(f"\n{SOFT_PINK}┌──[ RANDOM UUID V4 GENERATOR ]{RESET}")
    print(f"Token: {uuid.uuid4()}")

def run_port_simulator():
    print(f"\n{VIBRANT_RED}┌──[ PORT BINDING SIMULATOR ]{RESET}")
    try:
        port = int(input("Enter local port (e.g., 80, 8080): ") or 80)
        print(f"Testing local binding sockets configuration layout on 127.0.0.1:{port}...")
        time.sleep(0.5)
        print("Simulated Binding Result: FREE / AVAILABLE FOR HOST SERVICES")
    except ValueError: print("Ports must be whole integers.")

def run_character_counter():
    print(f"\n{NEON_PINK}┌──[ TEXT METRIC METERS ]{RESET}")
    text_data = input("Enter text string: ")
    print(f"Chars: {len(text_data)} | Stripped: {len(text_data.replace(' ', ''))} | Words: {len(text_data.split())}")

def run_env_multiplier():
    print(f"\n{SOFT_PINK}┌──[ COMPUTE LOAD MULTIPLIER ]{RESET}")
    try:
        base = int(input("Enter base units (default 1000): ") or 1000)
        print(f"Calculation Factor Load Result: {base ** 2}")
    except ValueError: print("Invalid scaling parameters.")

def run_token_masker():
    print(f"\n{VIBRANT_RED}┌──[ DEVELOPMENT TOKEN MASKER ]{RESET}")
    raw_token = input("Paste credentials token string: ").strip()
    if len(raw_token) > 8: print(f"Masked Layout: {raw_token[:4]}****{raw_token[-4:]}")
    else: print("Token string too short to safely mask.")

def run_hex_converter():
    print(f"\n{NEON_PINK}┌──[ STRING TO HEX ENCODER ]{RESET}")
    text = input("Enter string to convert: ")
    print(f"Hex Output: {text.encode('utf-8').hex()}")

def run_binary_converter():
    print(f"\n{SOFT_PINK}┌──[ INT TO BINARY ENCODER ]{RESET}")
    try:
        num = int(input("Enter integer number: ") or 10)
        print(f"Binary Output: {bin(num)}")
    except ValueError: print("Must enter a valid whole number.")

def run_math_squareroot():
    print(f"\n{VIBRANT_RED}┌──[ SQUARE ROOT EVALUATOR ]{RESET}")
    try:
        num = float(input("Enter positive number: ") or 25)
        print(f"Square Root Result: {math.sqrt(num)}")
    except ValueError: print("Negative or invalid float metrics cannot be parsed.")


# ==========================================
# MAIN HUB CONTROL LAYOUT AND GRID
# ==========================================
async def main_hub():
    if sys.platform == 'win32': os.system('color')  

    while True:
        if sys.platform == 'win32': os.system('cls')
        else: os.system('clear')

        print(PENTA_LOGO)
        print(f"{VIBRANT_RED}┌────────────────────────────────────────────────────────┐")
        print(f"│  {NEON_PINK}P E N T A   M U L T I - T O O L K I T   S U I T E{VIBRANT_RED}     │")
        print(f"└────────────────────────────────────────────────────────┘{RESET}")
        print(f" [{VIBRANT_RED}01{RESET}] Website Load Tester         [{NEON_PINK}14{RESET}] Local Port Simulator")
        print(f" [{VIBRANT_RED}02{RESET}] Math Command Calculator     [{NEON_PINK}15{RESET}] Text Character Counter")
        print(f" [{VIBRANT_RED}03{RESET}] Crypto Password Generator   [{NEON_PINK}16{RESET}] Compute Load Multiplier")
        print(f" [{VIBRANT_RED}04{RESET}] Time & Network Dashboard   [{NEON_PINK}17{RESET}] Development Token Masker")
        print(f" [{VIBRANT_RED}05{RESET}] String Hasher Utilities     [{VIBRANT_RED}18{RESET}] Local Text File Reader")
        print(f" [{VIBRANT_RED}06{RESET}] Local System Monitor        [{VIBRANT_RED}19{RESET}] JSON Syntax Validator")
        print(f" [{VIBRANT_RED}07{RESET}] Base64 Encoder / Decoder    [{VIBRANT_RED}20{RESET}] Environment Var Finder")
        print(f" [{NEON_PINK}08{RESET}] JSON Payload Formatter      [{VIBRANT_RED}21{RESET}] Unix Epoch Converter")
        print(f" [{NEON_PINK}09{RESET}] File Checksum Verifier      [{VIBRANT_RED}22{RESET}] Factorial Calculator")
        print(f" [{NEON_PINK}10{RESET}] Binary Path Finder          [{VIBRANT_RED}23{RESET}] String to HEX Encoder")
        print(f" [{NEON_PINK}11{RESET}] String Case Converter       [{VIBRANT_RED}24{RESET}] Int to Binary Encoder")
        print(f" [{NEON_PINK}12{RESET}] Admin Leap Year Checker     [{VIBRANT_RED}25{RESET}] Square Root Evaluator")
        print(f" [{NEON_PINK}13{RESET}] UUID v4 Token Generator")
        print(f"{DARK_ROSE}──────────────────────────────────────────────────────────{RESET}")
        
        choice = input(f"{VIBRANT_RED}Select option (1-25) ═► {RESET}").strip()
        
        if choice in ['1', '01']: await run_load_tester()
        elif choice in ['2', '02']: run_calculator()
        elif choice in ['3', '03']: run_password_generator()
        elif choice in ['4', '04']: run_clock_dashboard()
        elif choice in ['5', '05']: run_console_utilities()
        elif choice in ['6', '06']: run_system_monitor()
        elif choice in ['7', '07']: run_base64_tool()
        elif choice in ['8', '08']: run_json_formatter()
        elif choice in ['9', '09']: run_file_checksum_verifier()
        elif choice == '10': run_path_finder()
        elif choice == '11': run_case_converter()
        elif choice == '12': run_leap_checker()
        elif choice == '13': run_uuid_generator()
        elif choice == '14': run_port_simulator()
        elif choice == '15': run_character_counter()
        elif choice == '16': run_env_multiplier()
        elif choice == '17': run_token_masker()
        elif choice == '18': run_text_reader()
        elif choice == '19': run_json_validator()
        elif choice == '20': run_env_finder()
        elif choice == '21': run_epoch_converter()
        elif choice == '22': run_factorial_calc()
        elif choice == '23': run_hex_converter()
        elif choice == '24': run_binary_converter()
        elif choice == '25': run_math_squareroot()
        
        input(f"\n{DARK_ROSE}Press Enter to return to menu...{RESET}")


# ==========================================
# FAILSAFE WINDOW WRAPPER
# ==========================================
if __name__ == "__main__":
    try:
        asyncio.run(main_hub())
    except Exception as error_crash:
        # Keeps the window frozen open if a syntax or runtime bug happens
        print(f"\n\033[91m!!! CRITICAL RUNTIME CRASH LOGGED !!!\033[0m")
        print(f"Error Details: {error_crash}")
        input("\nExecution stopped safely. Press Enter to force close window...")


