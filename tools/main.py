import modules.dns_methods as dns_methods 
import modules.who_is as who_is 

def main():
    print("Enter the desired functionality:")
    print("1 - Resolve subdomains and get IPs (dnsresolver1)")
    print("2 - Query specific DNS records (dnsresolver2)")
    print("3 - Consult whois")
    print("0 - Exit")
    option = input()
    # Call the desired function
    if option == '1':
        dns_methods.resolve_subdomains()
    elif option == '2':
        dns_methods.query_dns_records()
    elif option == '3':
        who_is.whois_resolver()
    elif option == '0': 
        return()
    else:
        print("Invalid option")
    main()

# Verify if the script is being executed
if __name__ == "__main__":
    main()
