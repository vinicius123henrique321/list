def inverte_string(string):
    invertida = ""
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    return invertida

string_original = str(input("Digite uma palavra que deseje inverter: "))

string_invertida = inverte_string(string_original)

print("String original:", string_original)
print("String invertida:", string_invertida)
