import Modules.dns_methods as dns_methods 
import Modules.who_is as who_is 

def main():
    print("Enter the desired functionality:")
    print("1 - Resolve subdomains and get IPs (dnsresolver1)")
    print("2 - Query specific DNS records (dnsresolver2)")
    print("3 - Consult whois")
    print("0 - Exit")
    option = input()
    # Call the desired function
    if option == '1':
        dns_methods.dnsresolver1()
    elif option == '2':
        dns_methods.dnsresolver2()
    elif option == '3':
        who_is.whoisresolver()
    elif option == '0': 
        return()
    else:
        print("Invalid option")
    main()

if __name__ == "__main__":
    main()
