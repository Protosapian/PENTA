import asyncio
import datetime
import time
import sys
import os
import random
import aiohttp

# ANSI Color Codes
RED = "\033[91s"
GREEN = "\033[92s"
YELLOW = "\033[93s"
MAGENTA = "\033[95s"
CYAN = "\033[96s"
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
            stats["latencies"].append(duration)
    except Exception as e:
        duration = time.time() - start_time
        print(f"[PENTA][{launch_time}] Req #{request_id:03d}: Sent -> FAILED | Error: {str(e)}")
        stats["failed"] += 1
        stats["errors"].append(str(e))

async def worker(session, target_url, queue, stats):
    while not queue.empty():
        request_id = await queue.get()
        await send_request(session, target_url, request_id, stats)
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

    stats = {"successful": 0, "failed": 0, "statuses": {}, "latencies": [], "errors": []}
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
                print(f"Result: {eval(expr)}")
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
    generated = "".join(random.choice(chars) for _ in range(length))
    print(f"\n{GREEN}Generated Key:{RESET} {generated}")

# ==========================================
# 4. TIMEZONE & CLOCK DASHBOARD
# ==========================================
def run_clock_dashboard():
    print(f"\n{CYAN}=== PENTA WORLD TIME INTEGRATION ==={RESET}")
    now = datetime.datetime.now()
    utc_now = datetime.datetime.utcnow()
    print(f"Local System Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Universal UTC Time: {utc_now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Epoch Timestamp:    {int(time.time())}")

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
        print("======== PENTA CONTROL SUITE ========")
        print(f"{RED}1){RESET} PENTA Website Load Tester")
        print(f"{GREEN}2){RESET} Mathematical Calculator")
        print(f"{MAGENTA}3){RESET} Secure Password Generator")
        print(f"{CYAN}4){RESET} Time & Epoch Tracker")
        print("-------------------------------------")
        print("5) Exit Console")
        print("═" * 37)
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            await run_load_tester()
        elif choice == '2':
            run_calculator()
        elif choice == '3':
            run_password_generator()
        elif choice == '4':
            run_clock_dashboard()
        elif choice == '5':
            print("\nShutting down PENTA Hub. Goodbye!")
            break
        else:
            print(f"\n{RED}Invalid selection! Please input numbers 1-5.{RESET}")
        
        input("\nPress Enter to return to the main dashboard menu...")

if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main_hub())



