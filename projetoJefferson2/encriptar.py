# Ler o texto do arquivo de entrada
with open('entrada.txt') as arquivo:
    texto = arquivo.read()

# Definir a chave de deslocamento
chave = int(input("Digite a chave de deslocamento: "))

# Encriptar o texto
resultado = ""
for char in texto:
    if char.isalpha():
        maiuscula = char.isupper()
        char = char.upper()
        codigo = ord(char) - ord('A')
        codigo = (codigo + chave) % 26
        char_cifrado = chr(codigo + ord('A'))
        if not maiuscula:
            char_cifrado = char_cifrado.lower()
        resultado += char_cifrado
    else:
        resultado += char

# Escrever o texto encriptado no arquivo de saída
with open('saida_cifrada.txt', 'w') as arquivo:
    arquivo.write(resultado)

print(f"Mensagem Cifrada e salva em 'saida_cifrada.txt'")