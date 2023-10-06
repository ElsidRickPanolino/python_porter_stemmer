# converts word to cv pattern
def wordTocv(word):
    cons = "bcdfghjklmnpqrstvwxz"
    vowels = "aeiouy"
    
    cv_pattern = ""
    
    if len(word)>0:
        for i in range(len(word)):
            if i==len(word)-1:
                cons = "bcdfghjklmnpqrstvwxyz"
                vowels = "aeiou"
                
            for c in cons:
                if word[i] == c:
                    cv_pattern += "c"
            for v in vowels:
                if word[i] == v:
                    cv_pattern += "v"
                    
    return cv_pattern

# group the c's and v's and returns CV patterns
def cvToCV(cv):
    CV = ""
    previous = ""
    for i in cv:
        if previous == "":
            if i == "c":
                CV += "C"
            
            if i == "v":
                CV += "V"
            previous = i
            continue
        
        if i == "c" and previous != "c":
            CV += "C"
            
        if i == "v" and previous != "v":
            CV += "V"
            
        previous = i
        
    return CV
        
# count the number of CV
def countM(CV):
    while CV !="" and CV[-1]=='C':
        CV = CV[:-1]
    m = CV.count('VC')
    return m

# combine functions to count the value of M given the word
def wordToM(word):
    cv = wordTocv(word)
    CV = cvToCV(cv)
    m = countM(CV)
    return m

# porter stemer algorithm notation *s
# determine if the word ends with s or other letter
def endsWithS(word, letter = "s"): 
    if word.endswith(letter):
        return True
    else:
        return False
    
# porter stemer algorithm notation *v*
# determine if the word ends contains vowel
def haveVowel(word): 
    if cvToCV(wordTocv(word)) == "C":
        return False
    else:
        return True
    
# porter stemer algorithm notation *d
# determine if the word ends with double consonant
def doubleConsonant(word): 
    cv = wordTocv(word)
    if(len(word)>=2):
        if endsWithS(cv, letter = "cc") and word[-1] == word[-2]:
            return True
    else:
        return False
    
# porter stemer algorithm notation *o
# determine if the word ends with double consonant
def iscvc(word): 
    cv = wordTocv(word)
    if len(cv) >= 3:
        if endsWithS(cv, letter = "cvc"):
            if word[-1] != 'w' or word[-1] != 'x' or word[-1] != 'y':
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# to get the base word from the plural form
def step1a(word):
    word = word.lower()
    suffix_list = [["sses", "ss"], ["ies", "i"], ["ss", "ss"], ["s", ""]]
    for i in suffix_list:
        if endsWithS(word, letter=i[0]):
            word = word.replace(i[0], i[1])
            break
    return word


def step1b(word):
    word = word.lower()
    sec_and_third = False
    if wordToM(word) > 0:
        word = word.replace("eed","ee")
        if haveVowel(word):
            if endsWithS(word, letter="ed"):
                word = word.replace("ed","")
                sec_and_third = True

            elif endsWithS(word, letter="ing"):
                word = word.replace("ing","")
                sec_and_third = True

            if sec_and_third:
                if endsWithS(word, letter="at"):
                    word = word.replace("at","ate")
                elif endsWithS(word, letter="bl"):
                    word = word.replace("bl","ble")
                elif endsWithS(word, letter="iz"):
                    word = word.replace("iz","ize")
                elif doubleConsonant(word) and not endsWithS(word, letter="l") and not endsWithS(word, letter="s") and not endsWithS(word, letter="z"):
                    word = word[:-1]
      
def step1c(word):
    if endsWithS(word, letter="y"):
        if haveVowel(word):
            word = word.replace("y","i")

    return word

def step2(word):
    word = word.lower()
    suffix_list = [["ational", "ate"], 
                   ["tional", "tion"], 
                   ["enci", "ence"], 
                   ["anci", "ance"], 
                   ["izer", "ize"], 
                   ["abli", "able"], 
                   ["alli", "al"], 
                   ["entli", "ent"], 
                   ["eli", "e"],
                   ["ousli", "ous"],
                   ["ization", "ize"],
                   ["ation", "ate"],
                   ["ator", "ate"],
                   ["alism", "al"],
                   ["iveness", "ive"],
                   ["fulness", "ful"],
                   ["ousness", "ous"],
                   ["aliti", "al"],
                   ["iviti", "ive"],
                   ["bility", "ble"]]

    if wordToM(word)>0:
        for i in suffix_list:
            if endsWithS(word, letter=i[0]):
                word = word.replace(i[0], i[1])
                break
        return word
    
def step3(word):
    word = word.lower()
    suffix_list = [["icate", "ic"], 
                   ["ative", ""], 
                   ["alize", "al"], 
                   ["iciti", "ic"], 
                   ["ical", "ic"], 
                   ["full", ""], 
                   ["ness", ""]]

    if wordToM(word)>0:
        for i in suffix_list:
            if endsWithS(word, letter=i[0]):
                word = word.replace(i[0], i[1])
                break
        return word
    
def step4(word):
    word = word.lower()
    suffix_list = ["al", "ance", "ence", "er", "ic", "able", "ible", "ant", "ement", "ment", "ent", "sion", "tion", "ou", "ism", "ate", "iti", "ous", "ive", "ize"]

    if wordToM(word)>1:
        for i in suffix_list:
            if endsWithS(word, letter=i):
                word = word.replace(i, "")
                break
        return word



print(step4("homologous"))

