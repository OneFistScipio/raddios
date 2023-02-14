import shodan
import socket
import os

# Replace YOUR_API_KEY with your actual Shodan API key
api = shodan.Shodan("YOUR_API_KEY")

# Get the local IP address
local_ip = socket.gethostbyname(socket.gethostname())

# Get the network range from the local IP
ip_split = local_ip.split(".")
network_range = ip_split[0]+"."+ip_split[1]+"."+ip_split[2]+".0/24"

# Use Shodan to search for devices in the network range
results = api.search(network_range)

# Write the results to a text file
with open("results.txt", "w") as file:
    file.write("Results from Shodan search for devices in network range: " + network_range + "\n\n")
    for result in results['matches']:
        file.write("IP: " + result['ip_str'] + "\n")
        file.write("Hostnames: " + str(result.get('hostnames', 'None')) + "\n")
        file.write("Domains: " + str(result.get('domains', 'None')) + "\n")
        file.write("Country: " + str(result.get('country', 'None')) + "\n")
        file.write("ISP: " + str(result.get('isp', 'None')) + "\n")
        file.write("Product: " + str(result.get('product', 'None')) + "\n")
        file.write("Ports: " + str(result['port']) + "\n")
        file.write("Organization: " + result.get('org', 'None') + "\n")
        file.write("CVEs: " + str(result.get('CVEs', 'None')) + "\n")
        file.write("ASN Block: " + str(result.get('asn', 'None')) + "\n")
        file.write("\n")

print("Scan written to results.txt")
