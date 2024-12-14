import whois
from datetime import date

def whois_resolver(domain: str): # Receive the domain as a parameter
    result = whois.whois(domain)
    output = [f"{key}: {value}" for key, value in result.items() if value]
    return output