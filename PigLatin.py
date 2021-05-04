print("Welcome to the Pig Latin program!")
word = input("Please Enter a Word: ")
word = word.lower()

if word.isalpha() and len(word) > 0:
    print(word[1:]+ word[0] + "ay")
else:
    print("Sorry, that input did not work. Try again.")
    
