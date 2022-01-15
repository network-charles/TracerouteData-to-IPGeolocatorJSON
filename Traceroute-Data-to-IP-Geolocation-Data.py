# This module is for making API requests
import requests

# This module is for working with IP Address
from netaddr import *

# This module is for using Regex to manipulate strings 
import re

# The captured Traceroute data is opened up, and assigned a variable name 
with open("Google.txt", "r") as file:
    
    # Each line of the file is scanned to pick IP Addresses
    for line in file:
        
        # A string to match an IPv4 Address in a line is crafted, shout out to https://feralpacket.org/?p=817
        regex = "(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"

        # The raw data of the captured IPv4 Address is saved to a variable called "result"
        result = re.search(regex, line)

        # A Condition is defined that if the Result is True, save the unraw data (a string) of the captured IPv4 Address 
        if result:
            
            regex_result = result.group(0)
            
            # The string of the IPv4 Address is converted into an actual IPv4 Address using the Netaddr library
            each_index_of_ipv4_address_operated_by_netAddr_library = IPAddress(regex_result)
            
            # This checks if it is a Public IPv4 Address or not
            bool_public_IP = each_index_of_ipv4_address_operated_by_netAddr_library.is_unicast() and not each_index_of_ipv4_address_operated_by_netAddr_library.is_private()
            
            # This checks if it is a Private IPv4 Address or not
            bool_private_IP = each_index_of_ipv4_address_operated_by_netAddr_library.is_private()
            
            # The IPv4 Address being checked is printed out 
            print(each_index_of_ipv4_address_operated_by_netAddr_library)
            
            # IF the IPv4 Address is private, no API call is made
            if each_index_of_ipv4_address_operated_by_netAddr_library.is_private():
                continue

            # The actual IPv4 leveraging the NetAddr library is converted back to a string
            string_of_each_index_of_ipv4_address_operated_by_netAddr_library = str(each_index_of_ipv4_address_operated_by_netAddr_library)

            # The API call URL is converted to a List so the URL can be manipulated to take any IPv4 Address
            string_of_IP_Geolocation_API = list("requests.get('https://api.ipgeolocation.io/ipgeo?apiKey=API&ip=1.1.1.1&fields=geo')")

            # The String is added to the IPv4 Address section off the API call URL
            string_of_IP_Geolocation_API[92:99] = string_of_each_index_of_ipv4_address_operated_by_netAddr_library

            # The URL is converted from a List back to a String
            add_the_IPv4_address_from_file = "".join(string_of_IP_Geolocation_API)

            # The String is converted back to a class so the API Call can be executed
            converted_string_of_IP_Geolocation_API_to_a_class = eval(add_the_IPv4_address_from_file)

            # The JSON File is printed out
            print(converted_string_of_IP_Geolocation_API_to_a_class.text)

            # An API Call to https://ipgeolocation.io/ is made
            json_text = converted_string_of_IP_Geolocation_API_to_a_class.text
            
            # A new file is created. Now strings of files can be appended to the empty file
            f = open("json_result.json", "a")
            
            # The API Response is added to the file
            f.write(json_text)
            
            # The File is closed
            f.close()

    print("Completed")

