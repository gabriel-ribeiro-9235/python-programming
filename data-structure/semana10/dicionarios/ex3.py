dicPiratas = {'sir': 'matey',
              'hotel': 'fleabag inn',
              'student': 'swabbie',
              'boy': 'matey',
              'madam': 'proud beauty',
              'professor': 'foul blaggart',
              'restaurant': 'galley',
              'your': 'yer',
              'excuse': 'arr',
              'students': 'swabbies',
              'are': 'be',
              'lawyer': 'foul blaggart',
              'the': "th'",
              'restroom': 'head',
              'my': 'me',
              'hello': 'avast',
              'is': 'be',
              'man': 'matey'
              }
frase = input("Digite uma frase em inglês: ")
nova = palavra = ''
for letra in frase.lower():
    if letra in 'abcdefghijklmnopqrstuvwxyzç':
        palavra += letra
    else:
        nova += dicPiratas.get(palavra, palavra) + letra
        palavra = ''
nova += dicPiratas.get(palavra, palavra)
print(f"\"{frase}\" na língua dos piratas é \"{nova}\"")
