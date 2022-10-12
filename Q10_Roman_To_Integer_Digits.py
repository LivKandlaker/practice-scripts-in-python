#Runtime: 58 ms, faster than 42.75% of Python online submissions for Roman to Integer.
#Memory Usage: 13.6 MB, less than 9.50% of Python online submissions for Roman to Integer.
def romanToInt(s):
    """
    function that calc the number from roman_digit to ineger_digit
    :type s: str
    :rtype: int
    """
    list = [] #create empty list with the roman digits (char)
    list[:0]=s
    list.append("    ") #Append space to the end of the list (To not ask for value that is not exsist in the list)
    sum = 0 #create a varaible that sum all the digits
    for i in range(len(s)):
        if list[i] =='I':
            if list[i + 1] == 'V':
                sum += 4
            elif list[i + 1] == 'X':
                sum += 9
            else:
                sum += 1
        elif list[i] == 'V' and list[i - 1] != 'I':
            sum += 5
        elif list[i] == 'X' and list[i - 1] != 'I':
            if list[i + 1] == 'L':
                sum += 40
            elif list[i + 1] == 'C':
                sum += 90
            else:
                sum += 10
        elif list[i] == 'L' and list[i - 1] != 'X':
            sum += 50
        elif list[i] == 'C' and list[i - 1] != 'X':
            if list[i + 1] == 'D':
                sum += 400
            elif list[i + 1] == 'M':
                sum += 900
            else:
                sum += 100
        elif list[i] == 'D' and list[i - 1] != 'C':
            sum += 500
        elif list[i] == 'M' and list[i - 1] != 'C':
            sum += 1000
    
    return sum

answer = romanToInt("XVI")
print(answer)