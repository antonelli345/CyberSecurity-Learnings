import socket
import dns.resolver  
import os

def resolve_subdomains(domain: str):
    # Path to the wordlist file 
    current_dir = os.path.dirname(os.path.abspath(__file__))  # path of script
    wordlist_path = os.path.join(current_dir, "../worldlist/dns_dict1.txt")  # relative path to wordlist
    output = []
    try:
        with open(wordlist_path, "r") as subdomain_file:
            dictionary = subdomain_file.readlines()

        for line in dictionary:
            full_domain = line.strip() + "." + domain
            result = f"Resolved: {full_domain}"
            output.append(result)

    except FileNotFoundError:
        result = f"Error: Wordlist file not found at {wordlist_path}"
        output.append(result)
        raise   
    return output
            
def query_dns_records(domain: str):
    # path to the wordlist file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    wordlist_path = os.path.join(current_dir, "../worldlist/dns_dict2.txt")
    records = open(wordlist_path, 'r').read().splitlines()
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '8.8.4.4', '1.1.1.1', '1.0.0.1']
    output = []
    for record in records:
        try:
            answers = resolver.resolve(domain, record)
            for rdata in answers:
                result = f'{domain} {record} record: {rdata}'
                output.append(result)
        except dns.resolver.NoAnswer: 
            result = f'No {record} record found for {domain}'
            output.append(result)
        except dns.resolver.NXDOMAIN:
            result = f'Domain {domain} does not exist'
            output.append(result)
        except Exception as e:
            result = f'An error occurred: {e}'
            output.append(result)
    return output