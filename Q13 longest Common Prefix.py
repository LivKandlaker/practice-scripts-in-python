# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    """
    the function get a list of strings and return the common character
    :type strs: List[str]
    :rtype: str
    """
    char_array = [set(i) for i in strs]
    new_char_array = [sorted(j) for j in char_array]
    new_char_array.sort()
    print(new_char_array)
    small_word = new_char_array[len(new_char_array) - 1]
    new_char_array.remove(new_char_array[len(new_char_array) - 1])
    print(small_word)
    print(new_char_array)
    # range(len(new_char_array[len(new_char_array) - 1])
    # current_word = new_char_array[i]
    new_list = []

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
    for i in range(len(new_char_array)):
        for j in range(len(small_word)):
            if small_word[j] == new_char_array[i][j]:
                print("equal")
                break
            #elif small_word[j]


    print(small_word)

    return


strs = ["dogcart", "racecar", "car", "rbce", "bcre"]
answer = longestCommonPrefix(strs)
