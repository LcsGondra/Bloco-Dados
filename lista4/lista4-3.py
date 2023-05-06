palavra = "palavra"
palavra_plus = []
for c in list(palavra):
    c_plus = ord(c)+1
    palavra_plus.append(chr(c_plus))

print
print(f"palavra original: {palavra} \npalavra cifrada + 1: {''.join(palavra_plus)}")

