# Traceroute-Data-to-IP-Geolocation-Data

This scripts picks each IPv4 address in the .txt file containing several Traceroute data captured from Google.com

Next, it makes an API call to an IP Geo-location API (https://ipgeolocation.io/) to get the Geo-location of the Public Address.

Lastly, these captured API calls are saved into a new file.

I will appreciate it if someone can write a script that converts each API call into an excel spreadsheet. All API call should be saved inside one excel spreadsheet, not several spreadsheets.


NB: To learn how to make periodic traceroute to several domain names and then capture the data into a text file, see https://github.com/network-charles/Periodic-Traceroute
