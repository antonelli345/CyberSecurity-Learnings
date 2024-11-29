import whois
from datetime import date

def whois_resolver():
    print("Enter the domain:")
    domain = whois.whois(input())
    print("1 - No need output in a file")
    print("2 - Need output in a file")
    option = input() # Receives the user's choice
    dateToday = date.strftime(date.today(), '%d-%m-%y')
    if(option)  == '1':
        print(domain.text)
    elif(option) == '2':
        with open('whois-'+ dateToday +'.txt', 'w', encoding="UTF-8", errors="replace") as file:
            file.write(domain.text) # Write the output to the file
    else:
        print("Invalid option")
        whois_resolver()

