import socket
import dns.resolver

   
# This methods resolves subdomains and get IPs with treatmenting for possible errors   
def dnsresolver1():
    print("Enter the domain: ")
    domain = input()
    # Read the dns_dict1.txt file with the subdomains
    with open('./tools/dictionary/dns_dict1.txt', 'r') as dict:
        dictionary = dict.readlines()
        for line in dictionary: 
            DNS = line.strip() + '.' + domain
            try:
                print(DNS + ': ' + socket.gethostbyname(DNS))
            except socket.gaierror:
                pass
            
# This methods queries specific DNS records
def dnsresolver2():
    print("Enter the domain: ")
    domain = input()
    # Read the dns_dict2.txt file with the DNS records
    records = open('./tools/dictionary/dns_dict2.txt', 'r').read().splitlines()
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