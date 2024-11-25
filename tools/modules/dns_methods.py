import socket # Importa a biblioteca socket
import dns.resolver # Importa a biblioteca dns.resolver

   
# Método para resolver subdomínios e obter IPs    
def dnsresolver1():
    print("Enter the domain: ")
    domain = input()#Solicita o domínio ao usuário
    #Abre o arquivo dns_dict1.txt com os subdomínios
    with open('./DNS_Tools/Dictionary/dns_dict1.txt', 'r') as dict:
        dictionary = dict.readlines() # Lê as linhas do arquivo
        for line in dictionary: # Itera por cada subdomínio no arquivo
            DNS = line.strip() + '.' + domain # Monta o nome completo do subdomínio encontrado
            try:
                # Resolve o endereço ip do subdomínio e exibe o resultado
                print(DNS + ': ' + socket.gethostbyname(DNS))
            except socket.gaierror:
                # Ignora erros ao resolver subdomínios invalidos
                pass
    
# Método para consultar registros DNS específicos
def dnsresolver2():
    print("Enter the domain: ")
    domain = input() # Solicita o domínio ao usuário
    # Lê os tipos de registros DNS do arquivo dns_dict2.txt
    registros = open('./DNS_Tools/Dictionary/dns_dict2.txt', 'r').read().splitlines()
    resolver = dns.resolver.Resolver() # Instancia um resolvedor de DNS
    # Define os servidores dns para as consultas
    resolver.nameservers = ['8.8.8.8', '8.8.4.4', '1.1.1.1', '1.0.0.1']
    
    for registro in registros: # Itera por cada tipo de registro DNS
        try:
            # Faz a consulta DNS para o registro especificado
            answers = resolver.resolve(domain, registro)
            for rdata in answers: # Itera por cada resposta encontrada
                print(f'{domain} {registro} record: {rdata}')
        except dns.resolver.NoAnswer: 
            # Caso não haja resposta para o tipo do registro fornecido
            print(f'No {registro} record found for {domain}')
        except dns.resolver.NXDOMAIN:
            # Caso o domínio não exista
            print(f'Domain {domain} does not exist')
        except Exception as e:
            # Lida com outros erros genéricos
            print(f'An error occurred: {e}')