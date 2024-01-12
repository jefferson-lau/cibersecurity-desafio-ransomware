# Ler o texto cifrado do arquivo de entrada
with open('saida_cifrada.txt') as arquivo:
    texto = arquivo.read()

# Definir a chave de deslocamento
chave = int(input("Digite a chave de deslocamento: "))

# Descriptografar o texto
resultado = ""
for char in texto:
    if char.isalpha():
        maiuscula = char.isupper()
        char = char.upper()
        codigo = ord(char) - ord('A')
        codigo = (codigo - chave) % 26
        char_original = chr(codigo + ord('A'))
        if not maiuscula:
            char_original = char_original.lower()
        resultado += char_original
    else:
        resultado += char

# Escrever o texto descriptografado no arquivo de saída
with open('saida_descriptada.txt', 'w') as arquivo:
    arquivo.write(resultado)

print(f"Mensagem Descriptada e salva em 'saida_descriptada.txt'")