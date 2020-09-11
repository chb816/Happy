with open('word.txt','r') as file :
    for word in file :
        word = word.strip('\n')
        if word == ''.join(reversed(word)) :
            print(word)
