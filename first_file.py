sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

vocab_list = ['function','inputs','none','lists']

def word_checker(word_to_check, vocab_list,number):
    #quick function to check to see if a word is in the vocab list
    for word in vocab_list:
        if word_to_check in vocab_list[number]: #the word to check is also sent with it's matching number
            return word_to_check
        else:
            return None
        
#Inputs: word to be matched. This is from user input. Number in the paragraph.
#        Paragraph(s) to do the matching in.
#Output: String where the word has been replaced.
def word_replacer(word,number,paragraph):
    replaced = []
    #found = 0
    formatted_number = "___" + str(number + 1) + "___"
    para_string = paragraph.split()
    for index in para_string: #iterate through the paragraph
        if index == formatted_number or (formatted_number + "s"): #we've found a match for the number
            checked_word = word_checker(word, vocab_list,number) #check the word we passed in to see if vocab
            if checked_word != None: #we found the word
                #print checked_word #debug
                #replace the number with checked word in the paragraph
                index = index.replace(formatted_number,checked_word)
                replaced.append(index)
            else:
                return found
        else:
            replaced.append(index)
            
    replaced = " ".join(replaced)    
    return replaced
            
def start_game():
    
    number = 0 #this is the number that will matched to a vocab word ie."___1___'
    guesses = 5
    vocab_list_length = 4
    wrong_guess = 0
    text = sample
    while guesses >= 1 and number < vocab_list_length:
        if wrong_guess == 1:
            user_input = raw_input("Wrong answer, dumbass. Type in another one:")
        else:    
            user_input = raw_input("Type in a word:")              
        word = user_input
        
        if word_replacer(word,number,sample) == 0:
            guesses = guesses - 1
            wrong_guess = 1
        else:
            text = word_replacer(word, number, text) 
            print word_replacer(word,number,text)
            wrong_guess = 0
            number += 1
        print wrong_guess
    if guesses == 0:
        print "You ran out of guesses. GAME OVER, DUDE"
    else:
        print "Congrats, I guess...."
   
start_game()