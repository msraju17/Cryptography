#Global declaration
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Will use to convert the letters into numberical values
KEY = 3
ENGLISH_WORDS = [] #to store the dictionary words
CRYPTOANALYSIS = []

#caesar encryption algorithm
def caesar_encrypt(plain_text):

	#the encrypted message
	cipherText = ''
	#we make the algorithm case insensitive
	plain_text = plain_text.upper()
	
	#consider all the letters in the plain_text
	for letter in plain_text:
		#find the numerical representation (index) associated with that character in the alphabet
		index = ALPHABET.find(letter)
		
		#caesar encryption is just a simple shift of characters according to the key
		#In Caesar Cipher plain text will be encrypted using the formula c = E(p+k)
		index = (index+KEY)%len(ALPHABET)
		#keep appending the encrypted character to the cipher_text
		cipherText = cipherText + ALPHABET[index]
		
	return cipherText
	
#caesar decryption algorithm: basically the same but using -KEY in this case
def caesar_decrypt(cipher_text):

	plain_text = ''
	
	for letter in cipher_text:
		index = ALPHABET.find(letter)
		index = (index-KEY)%len(ALPHABET)
		plain_text = plain_text + ALPHABET[index]
		
	return plain_text


#cracking the caesar encryption algorithm with brute-force
def BruteForce(cipher_text):
        print("""
*******************************************************************************
        Cracking the caesar encryption algorithm with brute-force
*******************************************************************************
""")
        bruteForce = input("Click[Y/N] to do cryptoAnalysis with brute-force: ")
        print(" ")
        if(bruteForce.upper() == 'Y'):
                #Try all the possible key values so the size of the ALPHABET
                for key in range(len(ALPHABET)):
                        #reinitialize this to be an empty string
                        plain_text = ''

                        #we just have to make a simple caesar decryption
                        for letter in cipher_text:
                                index = ALPHABET.find(letter)
                                index = (index-key)%len(ALPHABET)
                                plain_text = plain_text + ALPHABET[index]
                        print("With key ",key," the plain text is '",plain_text,"'")
                        CRYPTOANALYSIS.append(plain_text)

#Detect the plain text is in english language or not

def get_wordList():

        #Open file
        wordList = open("english_words.txt","r");

        #Read and save all the english words
        for word in wordList.read().split('\n'):
                ENGLISH_WORDS.append(word)

        wordList.close()

#Count the number of english words in a given text
def count_words(text):

        text = text.upper()
        words = text.split(' ')
        matches = 0

        for word in words:
                if word in ENGLISH_WORDS:
                        matches = matches + 1
        return matches

#decides whether a given text is english or not
def is_text_english(text):

        #Number of words matched to wordList
        matches = count_words(text)
        wordLength = len(text.split(' '))
        #print("Matches ", matches, "wordLenth ", wordLength, "Percentage ", ((matches/wordLength)*100))
        #Assuming if the plaint text matched with 80% of english words
        #Then the text detect as the english language.
        if (((matches/wordLength)*100) >= 80):
                print("From the Brue Force Following text belong to the English Language:")
                print("------------------------------------------------------------------")
                print(text,"\n")
        

def detect_language():
        print("""
*****************************************************************
        Detect the plain text is in English Language
*****************************************************************
                """)
        detectLang = input("Click[Y/N] to find the plain text is in english: ")
        print(" ")
        if(detectLang.upper() == 'Y'):
                get_wordList()
                for text in CRYPTOANALYSIS:
                        is_text_english(text)


if __name__ == "__main__":

        print("""
**************************************************************
                   Caesar Cipher Algorithm
**************************************************************
                """)
        plainText = input("Please enter the plain text: ")
        encrypted = caesar_encrypt(plainText)
        print("Cipher Text is ",encrypted)
        decrypted = caesar_decrypt(encrypted)
        print("Decrypted text is ",decrypted)

        #Call Caesar Cipher Brute-Force Crypto anlaysis
        BruteForce(encrypted)

        #Detect english language
        detect_language()
        
        




                
