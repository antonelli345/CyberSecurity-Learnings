import socket
import os
from dotenv import load_dotenv
import ipinfo

def get_geo_loc(domain: str):
    # API key for the IP Geolocation API
    load_dotenv(".env")
    access_token = os.getenv("IPINFO_TOKEN")
    ip_address = socket.gethostbyname(domain)
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    output = [f"{key}: {value}" for key, value in details.all.items() if value]
    return output