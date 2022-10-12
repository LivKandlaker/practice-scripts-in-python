from functools import reduce
def longestCommonPrefix(strs):
    """
    the function get list of strings and return the common characters
    :type strs: List[str]
    :rtype: str
    """
    char_array = [set(i) for i in strs]
    answer = reduce(lambda a,b: a & b, char_array)
    if answer == set():
        answer = '" "'
    return answer
    
strs = ["dogcar","racecar","car", "race", "acre"]
answer = longestCommonPrefix(strs)
print(answer)



        