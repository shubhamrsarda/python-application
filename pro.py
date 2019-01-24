import json
from difflib import get_close_matches

data=json.load(open("data.json"))
print("Hello Welcome to Dictiory")
ch='y'
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you Mean :== %s insted enter y or n " %get_close_matches(word,data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn =='n':
            return "word u want dosent exists"
        else:
            return "we didnt understsnd your entry"


    else:
        return "Word dosent exists .check it....!"
while ch == 'y':
    ind=input("Enter Word:")
    output=translate(ind)
#    print("Defination of the Word is:=\n")
    if type(output) == list:
        for i in output:
            print(i+"\n")
    else:
        print(output)
    ch=input("Do you want to continue ..? y/n")
    ch=ch.lower()
