# Runtime: 113 ms, faster than 18.05% of Python online submissions for Palindrome Number.
#Memory Usage: 13.6 MB, less than 12.96% of Python online submissions for Palindrome Number.
def isPalindrome(x):
    """
    isPalindrome checks if number is Palindrome and return boolean answer
    :type x: int
    :rtype: bool
    """
    i = 0
    List = [] #create empty list
    if x < 0:
        return False
    while i < x:
       y = x % 10
       List.append(y) #Append the modulo to list 
       x = int(x / 10) #"delete " the last digit
    j = 0 #The first value
    k = len(List) - 1 #The last value
    
    while j < k :
        if List[j] == List[k]:
            j += 1
            k -= 1
        elif List[j] != List[k]:
            return False
        
    return True

bool_res = isPalindrome(98765432123456789)
print(bool_res)