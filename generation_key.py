'''
Шифрование
'''
closed_key = 78768758758768
alphabit = ['П', '33', 'Р', '38']
text = 'П'

gg = str(text)
gg = alphabit.index(gg)
gg = int(gg)
gg = gg + 1
crypto_text = alphabit[gg]
print(crypto_text)
crypto_text = int(crypto_text)
open_key = crypto_text*closed_key

print(open_key)

'''
Расшифровка
'''
crypto_text = open_key//closed_key
gg = str(crypto_text)
gg = alphabit.index(gg)
gg = int(gg)
gg = gg - 1
crypto_text = alphabit[gg]
print(crypto_text)

