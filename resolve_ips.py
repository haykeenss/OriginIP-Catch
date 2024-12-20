import subprocess
import asyncio
import aiofiles

# Function to prompt for input file
async def get_input_file():
    while True:
        input_file = input("Enter the path to the IP list file: ").strip()
        try:
            async with aiofiles.open(input_file, "r") as f:
                print(f"File '{input_file}' loaded successfully.")
                return input_file
        except FileNotFoundError:
            print(f"File not found: {input_file}. Please try again.")

# Output file
output_file = "resolved_ip.txt"

# Function to perform curl request and resolve with httpx
async def resolve_ip(ip, ports):
    resolved_titles = []
    print(f"Starting resolution for IP: {ip}")
    for port in ports:
        try:
            # Build the full URL with the port
            url = f"http://{ip}:{port}" if port != 443 else f"https://{ip}"

            # Run the curl command and pipe to httpx
            print(f"Resolving {ip}:{port}...")
            curl_command = ["curl", "-s", url]
            httpx_command = ["httpx", "-title"]

            # Run curl and pipe the output to httpx
            curl_process = await asyncio.create_subprocess_exec(
                *curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            curl_output, _ = await curl_process.communicate()

            if curl_output:
                httpx_process = await asyncio.create_subprocess_exec(
                    *httpx_command,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                httpx_output, _ = await httpx_process.communicate(input=curl_output)

                if httpx_output:
                    title = httpx_output.decode().strip()
                    resolved_titles.append(f"{ip}:{port} - {title}")
                    print(f"Resolved {ip}:{port} - Title: {title}")
                else:
                    print(f"No title found for {ip}:{port}")
            else:
                print(f"No response from {ip}:{port}")
        except Exception as e:
            print(f"Error resolving {ip}:{port} - {e}")
    return resolved_titles

# Main function
async def main():
    ports = [80, 443, 8080]
    tasks = []

    # Prompt for input file
    input_file = await get_input_file()

    # Read IP addresses from the input file
    async with aiofiles.open(input_file, "r") as f:
        ips = [line.strip() for line in await f.readlines()]
    print(f"Read {len(ips)} IP addresses from the file.")

    # Process each IP concurrently
    for ip in ips:
        tasks.append(resolve_ip(ip, ports))

    # Gather results
    print("Starting resolution of IPs...")
    all_results = await asyncio.gather(*tasks)

    # Write results to the output file
    print(f"Writing results to {output_file}...")
    async with aiofiles.open(output_file, "w") as f:
        for results in all_results:
            for result in results:
                await f.write(result + "\n")

    print(f"Resolved IPs and titles saved to {output_file}")

# Run the script
if __name__ == "__main__":
    asyncio.run(main())

