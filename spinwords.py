def spin_words(sentence):
    # Your code goes here
    list_words = sentence.split()
    for w, word in enumerate(list_words):
        length = len(word)    
        if length >= 5:                        
            list_words[w] = word[::-1]                    
    return ' '.join(list_words)
