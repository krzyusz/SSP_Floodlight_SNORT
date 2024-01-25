import requests
import time
import json

# Define default values for the flow
default_flow = {
    "switch": "00:00:00:00:00:00:00:02",
    "name": "blockflow",
    "priority": "32768",
    "eth_type": 2048,
    "ipv4_src": "",
    "ipv4_dst": "",
    "active": True,
    "actions": ""
}

# Initialize a counter for the flow names
flow_count = 1

# Function to send POST request with the given source and destination IPs
def send_post_request(ipv4_src, ipv4_dst):
    global flow_count
    # Update the default flow with new src and dst values, and increment the flow name
    flow = default_flow.copy()
    flow["ipv4_src"] = ipv4_src
    flow["ipv4_dst"] = ipv4_dst
    flow["name"] = default_flow['name']+str(flow_count)
    flow_count += 1  # Increment the flow name counter
    
    # Define the URL for the POST request
    url = "http://127.0.0.1:8080/wm/SnortAPI/snort/block"
    
    # Send the POST request with the JSON payload
    response = requests.post(url, data=json.dumps(flow))
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Flow {} sent successfully", flow)
    else:
        print("Failed to send flow {}. Status code: {}, Response: {}",flow,response.status_code,response.text)

# Function to process the file and wait for new lines
def process_file_forever(file_path):
    with open(file_path, 'r') as file:
        # Go to the end of the file
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Sleep briefly to avoid busy waiting
                continue
            if "Blocking ICMP Packet" in line:
                parts = line.split(" ")
                ipv4_src = parts[-3].replace("\n","").strip().split(":")[0]
                ipv4_dst = parts[-1].replace("\n","").strip().split(":")[0]
                send_post_request(ipv4_src, ipv4_dst)
            elif "TCP SYN Flood" in line:
                parts = line.split(" ")
                ipv4_src = parts[-3].replace("\n","").strip().split(":")[0]
                ipv4_dst = parts[-1].replace("\n","").strip().split(":")[0]
                send_post_request(ipv4_src, ipv4_dst)


# Path to the file that is being piped in real-time
file_path = '/tmp/alert'  # Replace with the actual file path

# Call the function to start processing the file
process_file_forever(file_path)
