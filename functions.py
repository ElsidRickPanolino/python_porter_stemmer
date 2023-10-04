# converts word to cv pattern
def wordTocv(word):
    cons = "bcdfghjklmnpqrstvwxz"
    vowels = "aeiouy"
    
    cv_pattern = ""
    
    for i in word:
        for c in cons:
            if i == c:
                cv_pattern += "c"
        for v in vowels:
            if i == v:
                cv_pattern += "v"
                
    return cv_pattern
''
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
    if endsWithS(cv, letter = "cc"):
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
    if wordToM(word) > 0:
        word = word.replace("eed","ee")
        if haveVowel(word):
            if endsWithS(word, letter="ed"):
                word = word.replace("ed","")
                
            if endsWithS(word, letter="ing"):
                word = word.replace("ing","")

    return word

print(step1b("plastered"))

