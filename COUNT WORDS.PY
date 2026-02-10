#NAME-KARUNA.G.S
#USN-RVUN25BCA0047
#TO COUNT NUMBERS USING FUNCTIONS

def count_words(sentence):
    words = sentence.split()
    return len(words)
text = input("Enter a sentence: ")
print("Number of words:", count_words(text))
