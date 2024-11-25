import whois # Importa o módulo whois

def whoisresolver():
    print("Enter the domain:")
    domain = whois.whois(input())
    print("1 - No need output in a file")
    print("2 - Need output in a file")
    option = input() # Recebe a opção do usuário
    if(option)  == '1':
        print(domain.text)
    elif(option) == '2':
        with open('whois.txt', 'w', encoding="UTF-8", errors="replace") as file:
            file.write(domain.text)
    else:
        print("Invalid option")
        whoisresolver()

