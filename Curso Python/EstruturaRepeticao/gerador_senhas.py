import getpass
print("projeto gerador de senhas".title())

chave = getpass.getpass("digite a base da sua senha: ".title())

senha = ""
for letra in chave:
    if letra in "Aa": senha += "1"
    elif letra in "Bb": senha += "@"
    elif letra in "Cc": senha += "2"
    elif letra in "Dd": senha += "3"
    elif letra in "Ee": senha += "4"
    elif letra in "Ff": senha += "5"
    elif letra in "Rr": senha += "#"
    elif letra in "Ss": senha += "%"
    elif letra in "Mm": senha += "$"
    elif letra in "Ww": senha += "&"
    elif letra in "Ii": senha += "©"
    else: senha = senha + letra

print(senha)