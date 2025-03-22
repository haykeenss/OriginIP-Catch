# Resolve IPs with Titles
In your research on discovering the origin Ip address of a web applications, using shodan, urlx, waybackurl, gather as many IP address possible save in a txt file and automate with the script. 
This script is designed to resolve IP addresses to their respective titles by sending HTTP requests to specified ports. It utilizes Python's `asyncio` and `aiofiles` libraries for asynchronous processing and combines the use of `curl` and `httpx` tools to fetch and process HTTP responses efficiently. If you find this useful, do well to leave me a star.

## Features

- **Concurrent Resolution**: Process multiple IPs concurrently for faster execution.
- **Customizable Ports**: By default, the script checks ports 80, 443, and 8080, but this can be modified in the code.
- **Asynchronous I/O**: Efficiently handles file and subprocess operations.
- **Error Handling**: Captures and reports errors during the resolution process.

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.7+**
- **curl**: A command-line tool for transferring data.
- **httpx**: A lightweight tool for processing HTTP requests.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/haykeenss/OriginIP-Catch.git
    cd OriginIP-Catch
    ```

2. Install Python dependencies:

    ```bash
    pip install aiofiles
    ```

3. Make sure `curl` and `httpx` are installed and available in your PATH.

    ```bash
    sudo apt install curl
    sudo apt install httpx # or install httpx using your package manager // sudo apt install httpx-toolkit
    ```

## Usage

1. **Prepare the IP List**
   - Create a text file containing one IP address per line. For example:

     ```
     192.168.1.1
     10.0.0.2
     172.16.0.3
     ```

2. **Run the Script**
   - Execute the script using Python:

     ```bash
     python3 resolve_ips.py
     ```

3. **Provide Input File**
   - When prompted, enter the path to your IP list file.

4. **Check Results**
   - The resolved titles and IP-port combinations will be saved to a file named `resolved_ip.txt`.

## Script Overview

### Functions

#### `get_input_file()`
Prompts the user for the path to an input file containing IP addresses and validates the file's existence.

#### `resolve_ip(ip, ports)`
Processes a single IP address by attempting to resolve titles for the specified ports (default: 80, 443, 8080) using `curl` and `httpx`. Returns a list of resolved titles.

#### `main()`
Coordinates the resolution process by:
- Reading the input file
- Concurrently processing IP addresses
- Writing results to the output file

### Output

Results are saved in `resolved_ip.txt` with the format:

```
<IP>:<Port> - <Title>
```

## Example Output

For an input file with the following IPs:

```
192.168.1.1
10.0.0.2
```

The `resolved_ip.txt` might contain:

```
192.168.1.1:80 - Apache Server Default Page
192.168.1.1:443 - Secure Apache Server
10.0.0.2:8080 - Custom Application Title
```

## Troubleshooting

- **File Not Found**: Ensure the file path is correct and accessible.
- **curl/httpx Errors**: Verify that `curl` and `httpx` are correctly installed and configured.(if httpx not working for you, you can use install httpx-toolkit, the script is configured for both.)
- **Empty Results**: Confirm the IPs are reachable and the ports are open.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For questions or support, contact the repository owner at [haytech46@gmail.com].

