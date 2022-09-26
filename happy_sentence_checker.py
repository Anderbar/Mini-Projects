sentence = input("Enter a sentence => ")
print(sentence)

lowercase_everything = sentence.lower()

def number_happy(sentence):
    
    laugh = 'laugh'
    happiness = 'happiness'
    love = 'love'
    excellent = 'excellent'
    good = 'good'
    smile = 'smile'
    
    
    find_laugh = lowercase_everything.count(laugh)
    find_happiness = lowercase_everything.count(happiness)
    find_love = lowercase_everything.count(love)
    find_good = lowercase_everything.count(good)
    find_excellent = lowercase_everything.count(excellent)
    find_smile = lowercase_everything.count(smile)
    happy_sentence = find_laugh + find_happiness + find_love + find_excellent + find_smile + find_good
    
    
    count = happy_sentence
    return count

positive_signs = number_happy(lowercase_everything) * '+'



def number_sad(sentence):
    
    bad = 'bad'
    sad = 'sad'
    terrible = 'terrible'
    horrible = 'horrible'
    problem = 'problem'
    hate = 'hate'
    
    find_bad = lowercase_everything.count(bad)
    find_sad = lowercase_everything.count(sad)
    find_terrible = lowercase_everything.count(terrible)
    find_horrible = lowercase_everything.count(horrible)
    find_problem = lowercase_everything.count(problem)
    find_hate = lowercase_everything.count(hate)
    sad_sentence = find_bad + find_sad + find_terrible + find_horrible + find_problem + find_hate

    count = sad_sentence
    return count

negative_signs = number_sad(lowercase_everything) * '-'
    

print("Sentiment:", positive_signs, negative_signs)

if number_sad(lowercase_everything) == number_happy(lowercase_everything):
    print('This is a neutral sentence.')
else:
    if number_happy(lowercase_everything) > number_sad(lowercase_everything):
        print('This sentence is a happy sentence.')
    else: 
        print('This sentence is a sad sentence.')
         
