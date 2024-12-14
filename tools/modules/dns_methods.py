import socket
import dns.resolver  
import os

def resolve_subdomains(domain: str):
    # Path to the wordlist file 
    current_dir = os.path.dirname(os.path.abspath(__file__))  # path of script
    wordlist_path = os.path.join(current_dir, "../worldlist/dns_dict1.txt")  # relative path to wordlist

    try:
        with open(wordlist_path, "r") as subdomain_file:
            dictionary = subdomain_file.readlines()

        for line in dictionary:
            full_domain = line.strip() + "." + domain
            print(f"Resolved: {full_domain}")

    except FileNotFoundError:
        print(f"Error: Wordlist file not found at {wordlist_path}")
        raise            
            
def query_dns_records(domain: str):
    # path to the wordlist file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    wordlist_path = os.path.join(current_dir, "../worldlist/dns_dict2.txt")
    records = open(wordlist_path, 'r').read().splitlines()
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '8.8.4.4', '1.1.1.1', '1.0.0.1']
    for record in records:
        try:
            answers = resolver.resolve(domain, record)
            for rdata in answers:
                print(f'{domain} {record} record: {rdata}')
        except dns.resolver.NoAnswer: 
            print(f'No {record} record found for {domain}')
        except dns.resolver.NXDOMAIN:
            print(f'Domain {domain} does not exist')
        except Exception as e:
            print(f'An error occurred: {e}')