import sys # Importa a biblioteca sys

# Método para solicitar entrada do usuário de forma compatível com Python 2 e 3
def inputpy():
    if sys.version_info.major == 2:
        return raw_input() # raw_input() para Python 2
    elif sys.version_info.major == 3:
        return input() # input() para Python 3
