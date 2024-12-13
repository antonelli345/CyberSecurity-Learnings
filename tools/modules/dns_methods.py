import socket
import dns.resolver  
# This methods resolves subdomains and get IPs with treatmenting for possible errors   
def resolve_subdomains(domain: str, file: bool = False): # Receives the domain as a parameter
    # Read the dns_dict1.txt file with the subdomains
    with open('/tools/worldlist/dns_dict1.txt', 'r') as subdomain_file:
        dictionary = subdomain_file.readlines()
        for line in dictionary: 
            full_domain = line.strip() + '.' + domain
            try:
                print(full_domain + ': ' + socket.gethostbyname(full_domain))
            except socket.gaierror:
                pass
            
def query_dns_records(domain: str, file: bool = False):
    # Read the dns_dict2.txt file with the DNS records
    records = open('/tools/wordlist/dns_dict2.txt', 'r').read().splitlines()
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '8.8.4.4', '1.1.1.1', '1.0.0.1']
    
    # This loop iterates over each record in the file with treatmenting for possible errors
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