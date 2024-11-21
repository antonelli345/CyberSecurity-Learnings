import Modules.dns_methods as dns_methods # Importa o módulo dns_methods
import Modules.inputpy as inputpy # Importa o módulo inputpy

# Método principal para que o usuário escolha a funcionalidade desejada
def main():
    print("Enter the desired functionality:")
    print("1 - Resolve subdomains and get IPs (dnsresolver1)")
    print("2 - Query specific DNS records (dnsresolver2)")
    print("3 - Exit")
    option = inputpy.inputpy() # Chama o método inputpy para receber a opção do usuário
    if option == '1':
        dns_methods.dnsresolver1() # Chama a funcionalidade de resolver subdomínios e obter IPs
    elif option == '2':
        dns_methods.dnsresolver2() # Chama a funcionalidade de consultar registros DNS específicos
    elif option == '3': 
        return() # Encerra o programa  
    else:
        print("Invalid option") # Mensagem de erro para opção inválida
    main()
    
# Verifica se o módulo está sendo executado diretamente    
if __name__ == "__main__":
    main()
