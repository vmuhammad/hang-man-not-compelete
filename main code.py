#hangman
import random
list=['toyota', 'lexus', 'kia', 'cerato', 'pickup', 'benz', 'porchse',' audi',' opel'
      , 'honda']
d=random.choice(list)
g=(len (d))
print(d)


for line in range (g):
 print('-',end=' ')


for line in range (g):
    char=input('enter a letter: ')
    
if char in (d):
   print('that is correct')
else:
    print('try again')
    

           



