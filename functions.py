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
def endsWith(word, letter): 
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
        if endsWith(cv, "cc") and word[-1] == word[-2]:
            return True
    else:
        return False
    
# porter stemer algorithm notation *o
# determine if the word ends with double consonant
def iscvc(word): 
    cv = wordTocv(word)
    if len(cv) >= 3:
        if endsWith(cv, "cvc"):
            if word[-1] != 'w' or word[-1] != 'x' or word[-1] != 'y':
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def changeWord(word, old, new):
        if endsWith(word, old):
            word = word.replace(old, new)
        return word

    
# to get the base word from the plural form
def step1a(word):
    suffix_list = [["sses", "ss"], ["ies", "i"], ["ss", "ss"], ["s", ""]]
    for i in suffix_list:
        if endsWith(word, i[0]):
            word = word.replace(i[0], i[1])
            print("step1")
            break
    return word


def step1b(word):
    sec_and_third = False
    if wordToM(word) > 0:
        word = word.replace("eed","ee")
        if haveVowel(word):            
            if endsWith(word, "ed"):
                word = word.replace("ed","")
                print("step1b")
                sec_and_third = True

            elif endsWith(word, "ing"):
                word = word.replace("ing","")
                print("step1b")
                sec_and_third = True

            if sec_and_third:
                if endsWith(word, "at"):
                    word = word.replace("at","ate")
                    print("step1b")
                elif endsWith(word, "bl"):
                    word = word.replace("bl","ble")
                    print("step1b")
                elif endsWith(word, "iz"):
                    word = word.replace("iz","ize")
                    print("step1b")
                elif doubleConsonant(word) and not endsWith(word, "l") and not endsWith(word, "s") and not endsWith(word, "z"):
                    word = word[:-1]
                    print("step1b")
                if wordToM(word) == 1 and iscvc(word):
                    word += "e"
                    print("step1b")
                    
                    
    return word
      
def step1c(word):
    
    if endsWith(word, "y"):
        if haveVowel(word):
            word = word.replace("y","i")
    return word

def step2(word):
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
            if endsWith(word, i[0]):
                word = word.replace(i[0], i[1])
                print("step2")
                break
    return word
    
def step3(word):
    suffix_list = [["icate", "ic"], 
                   ["ative", ""], 
                   ["alize", "al"], 
                   ["iciti", "ic"], 
                   ["ical", "ic"], 
                   ["full", ""], 
                   ["ness", ""]]
    if wordToM(word)>0:
        for i in suffix_list:
            if endsWith(word, i[0]):
                word = word.replace(i[0], i[1])
                print("step3")
                break
    return word
    
def step4(word):
    suffix_list = ["al", "ance", "ence", "er", "ic", "able", "ible", "ant", "ement", "ment", "ent", "ion", "ou", "ism", "ate", "iti", "ous", "ive", "ize"]

    if wordToM(word)>1:
        for i in suffix_list:
            if i == "ion":
                if word[-1] == "s":
                    word = word.replace(i, "s")
                if word[-1] == "t":
                    word = word.replace(i, "t")
                
            if endsWith(word, i):
                word = word.replace(i, "")
                print("step4")
                break
    return word



def step5a(word):
    if wordToM(word) > 1:
        word = changeWord(word, "e", "")
        print("step5a 1")
    elif wordToM(word) == 1 and not endsWith(word, "o"):
        word = changeWord(word, "e", "")
        print("step5a 2")
        
    return word


def step5b(word):
    if wordToM(word)>1 and doubleConsonant(word) and endsWith(word,"l"):
        changeWord(word, "ll", "l")
        print("step5b")
        
    return word
        
def stem(word):
    word = word.lower()
    word = step1a(word)
    print(word, "1a")
    word = step1b(word)
    print(word, "1b")
    word = step1c(word)
    print(word, "1c")
    word = step2(word)
    print(word, "2")
    word = step3(word)
    print(word, "3")
    word = step4(word)
    print(word, "4")
    word = step5a(word)
    print(word, "5a")
    word = step5b(word)
    print(word, "5b")
    return word
