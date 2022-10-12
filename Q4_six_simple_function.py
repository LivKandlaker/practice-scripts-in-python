# Mission 1
def calc_price(Age,Gender):
    """
    The total price is 100 NIS, under 18 get 30% discount, over 65 get 25% discount and women over 18 get 5% discount
    :param Age:
    :param Gender:
    :return: The total price after discount per Age
    """
    Total_Price = 100

    # Check if the age is under 18 or above 65 and return the total price after discount else do nothing
    if Age < 18:
        Total_Price = Total_Price*0.7
    elif Age > 65:
        Total_Price = Total_Price*0.75
    else:
        Total_Price = Total_Price

    # Check if the gender is female and the age is above 18  and return the total price after discount else do nothing
    if Gender == "F":
        if Age > 18:
            Total_Price = Total_Price*0.95
        else:
            Total_Price = Total_Price
    else:
        Total_Price = Total_Price

    print(Total_Price)
    return Total_Price


calc_price(66,"M")

#Mission 2
def findMinMax (list):
    """
    The function get a list of numbers and get the minimum and maximum value
    :param list:
    :return: Min and Max value
    """
    # Assign first element as a minimum.
    Min_Value = list[0]

    # Assign first element as a maximum.
    Max_Value = list[0]

    for i in range(len(list)):
        # If the other element is min than first element
        if list[i] < Min_Value:
            Min_Value = list[i]  # It will change

    print("The smallest element in the list is ", Min_Value)

    for i in range(len(list)):
        # If the other element is max than first element
        if list[i] > Max_Value:
            Max_Value = list[i]  # It will change

    print("The smallest element in the list is ", Max_Value)
    return(Min_Value, Max_Value)


list1 = [-1, -45, 20, 100]
list2 = [1, 5, 7, 9, 3]
findMinMax(list1)

#Mission 3

def dict2list(dictionary):
    """
    The function get dictionary and return 2 lists. 1- All the keys. 2- All the values
    :param dictionary:
    :return: 2 lists
    """
    Keys, Values = [], [] #Creare two empty lists fir the values and keys
    for key, value in dictionary.items(): #Check all the items in the dictionary
        Keys.append(key) #add key from dictionary to Keys list
        Values.append(value) #add value from dictionary to Values list

    print(" The keys list: ", Keys)
    print(" The values list: ", Values)
    return (Values, Keys)

dictionary = {'jack': 'Abir' , 'sape': 4139}
dict2list(dictionary)

#Mission 4

def list2dict(list_keys, list_values):
    """
    Function to convert 2 lists to dictionary
    :param list_keys:
    :param list_values:
    :return: Dictionary
    """
    Dictionary = {} #Create empty dictionary
    for key in list_keys:
        for value in list_values:
            Dictionary[key] = value
            list_values.remove(value)
            break
    print(Dictionary)
    return (Dictionary)
list_keys = ["Java", "C++", "Python"]
list_values = [3, 12]
list2dict(list_keys,list_values)

#Mission 5

def upper_or_lower(string):
    """
    The Functin get string of Upper and Lower letters and return 2 string seperatly for Upper and Lower
    :param string:
    :return: 2 string, 1 for Upper letters, 1 for Lower letters
    """
    string_Upper = "" #Create empty list for the upper letters
    string_Lower = "" #Create empty list for the lower letters

    for i in range(len(string)):
        if string[i].isupper(): #Check if the letter is Upper
            string_Upper = string_Upper + string[i] #Add to the Upper string
        elif string[i].islower(): #Check if the letter is Lower
            string_Lower = string_Lower + string[i] #Add to the Lower string

    return (string_Upper, string_Lower)

string = "PythOn Is thE Best DevElop LangUAGe"
string_UP, string_LOW = upper_or_lower(string)
print(string_UP, string_LOW)

# Mission 6

def seperate(special_string):
    """

    :param special_string:
    :return: the count of Numbers and Letters
    """
    num_of_letters = 0 # Assign count of letters = 0.
    num_of_numbers = 0 # Assign count of numers = 0.
    for i in range(len(special_string)):
        if special_string[i].isnumeric():
            num_of_numbers += 1 # if the char is numeric add 1 to the counter
        elif special_string[i].isalpha():
            num_of_letters += 1 # if the char is letter add 1 to the counter

    print(num_of_letters)
    print(num_of_numbers)
    return (num_of_letters, num_of_numbers)


special_string = input("Please Enter Str & bank account password : ")
seperate(special_string)

