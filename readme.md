# **0xD4rKEYe DDoS Tool**

**Version:** 1.0 
**Status:** Beta

## Overview

`0xD4rKEYe` is an advanced Layer 7 DDoS (Distributed Denial of Service) attack tool that performs HTTP flood attacks on a specified target. It uses multi-threading to send a high volume of HTTP requests to overwhelm the target, making it inaccessible to legitimate users. The tool provides real-time statistics during the attack, including the total number of requests sent and requests per second (RPS).

## Features

- **Multi-Threaded Attacks:** Leverages multi-threading to maximize the number of HTTP requests sent to the target.
- **Real-Time Statistics:** Displays attack metrics in real-time, such as total requests sent and RPS.
- **Randomized User Agents:** Utilizes a pool of user agents to simulate requests from different browsers and devices.
- **Automatic Thread Calculation:** Automatically determines the optimal number of threads based on the system’s CPU cores.
- **Customizable Attack Parameters:** Allows users to customize the number of threads and the duration of the attack.

## **Installation**

### Requirements

This tool requires Python 3.x and the following Python libraries:

- `requests`: For sending HTTP requests.
- `colorama`: For colored terminal output.
- `psutil`: To determine the number of CPU cores.
- `pyfiglet`: For ASCII art display of the tool name.

To install the required libraries, use the following command:

```bash
pip install -r requirements.txt
```

### Downloading the Tool

You can clone the repository or download the script directly:

```bash
git clone https://github.com/Padmapriyan27/0xD4rKEYe-ddos-tool.git
cd 0xD4rKEYe-ddos-tool
```

## Usage

To launch an attack, run the script with the target URL and optional parameters for the number of threads and attack duration:

```bash
python 0xD4rKEYe.py <target> [--threads <number_of_threads>] [--duration <seconds>]
```

### Command-Line Arguments

- **target:** The URL or IP address of the target (required).
- **--threads:** The number of threads to use (optional, default is auto-calculated based on CPU cores).
- **--duration:** The duration of the attack in seconds (optional, default is 60 seconds).

### Example

```bash
python 0xD4rKEYe.py http://example.com --threads 100 --duration 120
```

This command will launch an attack on `http://example.com` using 100 threads for 120 seconds.

## How It Works

The tool sends HTTP GET requests to the specified target URL. It uses multiple threads to increase the number of requests sent per second. The user can specify the number of threads to use, or let the tool automatically calculate the optimal number based on the system's CPU cores.

During the attack, the tool displays real-time statistics, including the current time, total requests sent, and the number of requests per second (RPS). This allows users to monitor the impact of the attack in real-time.

## Real-Time Statistics

The tool provides a live display of statistics, including:

- **Time:** The current time.
- **Requests:** The total number of requests sent since the start of the attack.
- **RPS:** Requests per second, calculated dynamically based on the elapsed time.

These statistics help in understanding the effectiveness of the attack in real-time.

## Legal Disclaimer

**Warning:** This tool is intended for educational purposes only. Unauthorized use of this tool against websites, servers, or any other systems without explicit permission is illegal and unethical. Misuse of this tool can result in severe legal consequences, including criminal charges and civil lawsuits. The author and contributors of this tool do not take any responsibility for any misuse or damage caused by this tool. Always ensure you have proper authorization before using this tool.
