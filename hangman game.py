import random
from collections import Counter
s='cricket rugby volleyball football basketball badminton hockey tennis golf baseball running'
l=list(map(str,s.split()))
word=random.choice(l)

print('Guess the word! HINT: word is a name of a sport') 

for i in word:
    print('_',end=" ")
print()
playing=True
letterGuessed=''
chances=len(word)+2
while(chances!=0):
    print()
    chances-=1  
    try:
        guess=str(input('Enter a letter ro guess:'))
    except:
        print('Enter only a letter!')
        continue
    if not guess.isalpha():
        print('Enter only a letter!')
        continue
    elif len(guess)>1:
        print('Enter only a SINGLE letter')
        continue
    elif guess in letterGuessed:
        print('You have already guessed that letter')
        continue
    if guess in word:
        k=word.count(guess)
        for i in range(k):
            letterGuessed+=guess
    for char in word:
        if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
            print(char,end= ' ')
        elif (Counter(letterGuessed) == Counter(word)):
            print('the word is: ',end=' ')
            print(word)
            print('Congragulation,You Win the Game!')
            chances=0
            break
            break
        else:
            print('_',end=" ")
    if chances<=0 and (Counter(letterGuessed) != Counter(word)):
        print('You lost!Try again ....')
        print('The Word was',word)


        
