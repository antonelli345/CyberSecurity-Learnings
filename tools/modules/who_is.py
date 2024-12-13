import whois
from datetime import date

def whois_resolver(domain: str, file: bool = False): # Receives the domain as a parameter
    domain = whois.whois(domain)
    print(domain.text)
    if file:
        dateToday = date.strftime(date.today(), '%d-%m-%y')
        with open('whois-'+ dateToday +'.txt', 'w', encoding="UTF-8", errors="replace") as file:
            file.write(domain.text) # Write the output to the file
    elif not file:
        print(domain.text)