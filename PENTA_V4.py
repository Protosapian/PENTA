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

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

PENTA_LOGO = r"""
██████╗ ███████╗███╗   ██╗████████╗█████╗ 
██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔══██╗
██████╔╝█████╗  ██╔██╗ ██║   ██║   ███████║
██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══██║
██║     ███████╗██║ ╚████║   ██║   ██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
"""

# ==========================================
# 1. PENTA LOAD TESTER MODULE
# ==========================================
async def send_request(session, target_url, request_id, stats):
    start_time = time.time()
    launch_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    try:
        async with session.get(target_url, timeout=5) as response:
            duration = time.time() - start_time
            status = response.status
            print(f"[PENTA][{launch_time}] Req #{request_id:03d}: Sent -> Status: {status} | Time: {duration*1000:.0f}ms")
            stats["statuses"][status] = stats["statuses"].get(status, 0) + 1
            stats["successful"] += 1
            stats["total_latency"] += duration 
    except Exception as e:
        duration = time.time() - start_time
        print(f"[PENTA][{launch_time}] Req #{request_id:03d}: Sent -> FAILED | Error: {str(e)}")
        stats["failed"] += 1
        if len(stats["errors"]) < 100:  
            stats["errors"].append(str(e))

async def worker(session, target_url, queue, stats):
    while not queue.empty():
        try:
            request_id = await queue.get()
            await send_request(session, target_url, request_id, stats)
        finally:
            queue.task_done()

async def run_load_tester():
    print(f"\n{RED}=== PENTA WEBSITE TESTER SETUP ==={RESET}")
    target_url = input("Enter target URL (e.g., https://example.com): ").strip()
    if not target_url:
        print(f"{RED}Error: URL cannot be empty.{RESET}")
        return
        
    try:
        total_requests = int(input("Enter total requests (default 10000): ") or 10000)
    except ValueError:
        total_requests = 10000
    try:
        concurrent_users = int(input("Enter concurrent users (default 100): ") or 100)
    except ValueError:
        concurrent_users = 100

    print(f"\nConfirm: Test {target_url} with {total_requests} requests?")
    confirm = input("Proceed? (yes/no): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("Test cancelled.")
        return

    stats = {"successful": 0, "failed": 0, "statuses": {}, "total_latency": 0.0, "errors": []}
    queue = asyncio.Queue()
    for i in range(1, total_requests + 1):
        await queue.put(i)

    start_time = time.time()
    headers = {"User-Agent": "PENTA"}
    connector = aiohttp.TCPConnector(limit=concurrent_users)
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        tasks = [asyncio.create_task(worker(session, target_url, queue, stats)) for _ in range(concurrent_users)]
        await asyncio.gather(*tasks)

    total_time = time.time() - start_time
    print(f"\n{RED}{PENTA_LOGO}{RESET}")
    print(f"Total Time Taken:  {total_time:.2f} seconds")
    print(f"Successful Req:    {stats['successful']} | Failed Req: {stats['failed']}")
    if stats["successful"] > 0:
        avg_latency = (stats["total_latency"] / stats["successful"]) * 1000
        print(f"Avg Latency:       {avg_latency:.0f}ms")

# ==========================================
# 2. MATHEMATICAL CALCULATOR MODULE
# ==========================================
def run_calculator():
    print(f"\n{GREEN}=== PENTA QUICK CALCULATOR ==={RESET}")
    print("Supports +, -, *, /, and (). Type 'exit' to quit.")
    print("-" * 40)
    while True:
        expr = input("Calc > ").strip()
        if expr.lower() in ['exit', 'quit', 'q']:
            break
        if not expr:
            continue
        try:
            if all(c in "0123456789+-*/(). " for c in expr):
                node = ast.parse(expr, mode='eval')
                print(f"Result: {eval(compile(node, '<string>', 'eval'), {'__builtins__': {}}, {})}")
            else:
                print(f"{RED}Error: Invalid math characters.{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

# ==========================================
# 3. PASSWORD GENERATOR UTILITY
# ==========================================
def run_password_generator():
    print(f"\n{MAGENTA}=== PENTA CRYPTO-PASS GENERATOR ==={RESET}")
    try:
        length = int(input("Enter required password length (default 16): ") or 16)
    except ValueError:
        length = 16
        
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    generated = "".join(secrets.choice(chars) for _ in range(length))
    print(f"\n{GREEN}Generated Key:{RESET} {generated}")

# ==========================================
# 4. TIMEZONE & CLOCK DASHBOARD
# ==========================================
def run_clock_dashboard():
    print(f"\n{CYAN}=== PENTA WORLD TIME INTEGRATION ==={RESET}")
    now = datetime.datetime.now()
    utc_now = datetime.datetime.now(datetime.timezone.utc) 
    print(f"Local System Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Universal UTC Time: {utc_now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Epoch Timestamp:    {int(time.time())}")
    
    print(f"\n{YELLOW}--- Local Network Info (Safe Mode) ---{RESET}")
    print(f"Target Loopback IP: 127.0.0.1")
    print(f"Subnet Mask Target: 255.255.255.0")
    print(f"Interface Status:   Active / Localhost")

# ==========================================
# 5. CONSOLE UTILITIES MODULE
# ==========================================
def run_console_utilities():
    print(f"\n{YELLOW}=== PENTA CONSOLE UTILITIES ==={RESET}")
    print("1) Mock DNS Domain Analyzer")
    print("2) SHA-256 String Hasher")
    print("3) Overhead Packet Estimator")
    print("4) Back to Main Menu")
    print("-" * 40)
    
    sub_choice = input("Select a tool (1-4): ").strip()
    
    if sub_choice == '1':
        domain = input("\nEnter domain to profile: ").strip()
        if domain:
            print(f"{CYAN}[*] Mapping infrastructure logs for {domain}...{RESET}")
            time.sleep(1)
            print(f"Host target: {domain}")
            print(f"Record Type: A (Simulation Mode)")
            print(f"Virtual VIP: 192.168.1.{secrets.randbelow(254) + 1}")
        else:
            print(f"{RED}Invalid input.{RESET}")
            
    elif sub_choice == '2':
        text_input = input("\nEnter text to encode to SHA-256: ").strip()
        if text_input:
            hashed = hashlib.sha256(text_input.encode()).hexdigest()
            print(f"\n{GREEN}SHA-256 Hash Output:{RESET}\n{hashed}")
        else:
            print(f"{RED}Input cannot be blank.{RESET}")
        
    elif sub_choice == '3':
        print(f"\n{GREEN}=== Local Overhead Estimation ==={RESET}")
        try:
            packets = int(input("Enter total packets: ") or 1000)
            size = int(input("Enter payload size per packet (bytes): ") or 64)
            total_bytes = packets * (size + 40) 
            print(f"Estimated Total Data Footprint: {total_bytes / 1024:.2f} KB")
        except ValueError:
            print(f"{RED}Invalid numeric arguments.{RESET}")
        
    elif sub_choice == '4':
        return
    else:
        print(f"{RED}Invalid selection.{RESET}")
# ==========================================
# 6. CORE TOOLKIT ADDITIONS (ALL SAFE FOR GITHUB)
# ==========================================
def run_system_monitor():
    print(f"\n{GREEN}=== PENTA LOCAL SYSTEM MONITOR ==={RESET}")
    print(f"OS Platform:  {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    print(f"Processor:    {platform.processor() or 'Generic/Unknown CPU'}")
    print(f"Python Build: {platform.python_version()} ({platform.python_implementation()})")

def run_base64_tool():
    print(f"\n{MAGENTA}=== PENTA BASE64 ENCODER / DECODER ==={RESET}")
    print("1) Text to Base64 (Encode)")
    print("2) Base64 to Text (Decode)")
    mode = input("Select operation (1-2): ").strip()
    
    if mode == '1':
        data = input("Enter text to Encode: ")
        encoded = base64.b64encode(data.encode('utf-8')).decode('utf-8')
        print(f"{GREEN}Encoded Output:{RESET} {encoded}")
    elif mode == '2':
        data = input("Enter Base64 string to Decode: ").strip()
        try:
            decoded = base64.b64decode(data.encode('utf-8')).decode('utf-8')
            print(f"{GREEN}Decoded Output:{RESET} {decoded}")
        except Exception:
            print(f"{RED}Error: Invalid Base64 payload structure.{RESET}")
    else:
        print(f"{RED}Invalid selection.{RESET}")

def run_json_formatter():
    print(f"\n{CYAN}=== PENTA JSON FORMATTING UTILITY ==={RESET}")
    print("Paste your minified raw JSON line string below:")
    raw_input = input("JSON > ").strip()
    if not raw_input:
        return
    try:
        parsed_json = json.loads(raw_input)
        formatted_str = json.dumps(parsed_json, indent=4)
        print(f"\n{GREEN}Parsed and Pretty-Printed Output:{RESET}\n{formatted_str}")
    except json.JSONDecodeError as e:
        print(f"{RED}Error Parsing JSON: {e.msg} at char {e.pos}{RESET}")

def run_file_checksum_verifier():
    print(f"\n{YELLOW}=== PENTA FILE CHECKSUM VERIFIER ==={RESET}")
    file_path = input("Enter system file path to evaluate: ").strip()
    if not file_path or not os.path.exists(file_path):
        print(f"{RED}Error: File path targets do not exist locally.{RESET}")
        return
    try:
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        print(f"\n{GREEN}Evaluation Complete:{RESET}")
        print(f"Target Path: {file_path}")
        print(f"SHA-256 Checksum: {sha256_hash.hexdigest()}")
    except Exception as e:
        print(f"{RED}Failed reading operations: {e}{RESET}")

# ==========================================
# MAIN HUB GATEWAY
# ==========================================
async def main_hub():
    if sys.platform == 'win32':
        os.system('color')  

    while True:
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

        print(f"{RED}{PENTA_LOGO}{RESET}")
        print(f"{CYAN}====================================={RESET}")
        print(f"{CYAN}       P E N T A   S U I T E         {RESET}")
        print(f"{CYAN}====================================={RESET}")
        print("======== PENTA CONTROL SUITE ========")
        print(f"{RED}1){RESET} PENTA Website Load Tester")
        print(f"{GREEN}2){RESET} Mathematical Calculator")
        print(f"{MAGENTA}3){RESET} Secure Password Generator")
        print(f"{CYAN}4){RESET} Time & Epoch Tracker")
        print(f"{YELLOW}5){RESET} Local Network & String Utilities")
        print(f"{GREEN}6){RESET} Local System Information Monitor")
        print(f"{MAGENTA}7){RESET} Base64 Encoder / Decoder Utility")
        print(f"{CYAN}8){RESET} JSON Payload Formatter & Validator")
        print(f"{YELLOW}9){RESET} Local File Integrity Checksum Verifier")
        
        choice = input("\nSelect an option (1-9): ").strip()
        
        if choice == '1':
            await run_load_tester()
        elif choice == '2':
            run_calculator()
        elif choice == '3':
            run_password_generator()
        elif choice == '4':
            run_clock_dashboard()
            input("\nPress Enter to continue...")
        elif choice == '5':
            run_console_utilities()
            input("\nPress Enter to continue...")
        elif choice == '6':
            run_system_monitor()
            input("\nPress Enter to continue...")
        elif choice == '7':
            run_base64_tool()
            input("\nPress Enter to continue...")
        elif choice == '8':
            run_json_formatter()
            input("\nPress Enter to continue...")
        elif choice == '9':
            run_file_checksum_verifier()
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    asyncio.run(main_hub())




