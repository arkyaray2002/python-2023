f = open('file.txt', 'r')
data = f.read()
print(data)

words = data.split()
for word in words:
    if word[-2:] == 'um':
        print(word)

for word in words:
    if word[1:3] == 'or':
        print(word)

for word in words:
   if len(set(word).intersection(set('aeiouAEIOU'))) == 0:
       print(word)

    
f.close()

