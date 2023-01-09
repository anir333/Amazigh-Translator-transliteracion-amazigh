# Amazigh Translator / Sistema de transliteración Amazigh
abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
tamazight = ['ⴰ', 'ⴱ', 'ⵛ', 'ⴷ', 'ⴻ', 'ⴼ', 'ⴳ', 'ⵀ', 'ⵉ', 'ⵊ', 'ⴽ', 'ⵍ', 'ⵎ', 'ⵏ', 'o', 'p', 'ⵇ', 'ⵔ', 'ⵙ', 'ⵟ', 'ⵓ', 'ⵠ', 'ⵡ', 'ⵅ', 'ⵢ', 'ⵣ']

entered = input('Enter word or phrase: ')
name = entered
entered = entered.lower()
entered = entered.split()
final_entered = []

i = 0
while i < len(entered):
    word = entered[i]
   
    e = 0
    final_word = ""
    while e < len(word):
        ind = abecedario.index(word[e])
        final_word += tamazight[ind]
        
        e += 1
        
    final_entered.append(final_word)
    i += 1

print(" ".join(final_entered), "=>", name)
