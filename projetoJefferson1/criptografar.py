texto = input("Digite a mensagem: ")
chave = int(input("Digite a chave de deslocamento: "))

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

print(f"Mensagem Cifrada: {resultado}")