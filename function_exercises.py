#1
number = input("Please enter your number:")

def is_two(number):
    if number == 2 or number == "2": #just do return if number etc to return the boolen value
        return True
    else: return False

print(is_two(number))    

#2
vowel_list = ("a", "e", "i", "o", "u") #can just make this a string
vowel = input("Please input your vowel:")
vowel = vowel.lower()

def is_vowel(vowel):
    if vowel in vowel_list: #if string in vowels
        return True
    else: return False
    
    
print(is_vowel(vowel))   

#3
string_1 = input("please enter your string:")
not is_vowel(string_1)

#4
word = input("Please enter your word:")
def wordCaps(word):
    
    return word.capitalize()

print(wordCaps(word))

#5
billAmount = float(input("please enter your bill amount:"))
tipPercentage = int(input("Please enter your desired tip percentage:"))

def calculate_tip(tipPercentage, billAmount):
    return (billAmount * (tipPercentage * .01)) + billAmount

print(calculate_tip(tipPercentage, billAmount))

#6
def apply_discount(orgPrice , discPercent):
    return orgPrice - (orgPrice * (discPercent * .01))

print(apply_discount(orgPrice=float(input("Please enter your item price:")), discPercent=int(input("Please enter your discount: ")) ))

#7

def handle_commas(number_string):
    number_string = number_string.replace(",","")
    return int(number_string) #can put .replace and int and return all in one line

print(handle_commas(number_string=input("Pleas enter you number: ")))


#8
def get_letter_grade(grade):
   
    if grade >= 90:
        return('A')
    elif grade >= 80:
        return('B')
    elif grade >=70:
        return('C')
    elif grade >= 60:
        return('D')
    else:
        return('F')
    
print(get_letter_grade(grade = int(input("Please grade: "))))

#9

def remove_vowels(string_to_remove_vowels):
    string_to_remove_vowels.lower()
    return string_to_remove_vowels.translate({ord(i): None for i in 'aeiou'})

print(remove_vowels(string_to_remove_vowels= input("Please enter your string:")))

#10

def normalize_name(string_to_norm):
    string_to_norm=string_to_norm.strip() #chain these together: string_to_norm.strip().lower().replace().translate()
    string_to_norm = string_to_norm.lower()
    string_to_norm = string_to_norm.replace(" ", "_")
    return string_to_norm.translate({ord(i): None for i in "*%$#@!*&^~<>?"})


print(normalize_name(string_to_norm = input("Please enter your string:")))

#11

count = "yes"
number_list = []
while count == "yes":
    numberToAdd = int(input("Please enter a number to add to the list: "))
    number_list.append(numberToAdd)
    count = input("Would you like to continue?")

def cumulative_sum(*number_list):
    new_cumalitve_sum = []
    new_number = 0
    for number in number_list:
        new_number = new_number + number 
        
        new_cumalitve_sum.append(new_number)
    return new_cumalitve_sum

print(cumulative_sum(*number_list))    



