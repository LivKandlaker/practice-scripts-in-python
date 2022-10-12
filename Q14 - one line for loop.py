letter_list = []
for letter in "hellow world":
    letter_list.append(letter)

print(letter_list)

letter_list_2 = []
[letter_list_2.append(letter) for letter in "hellow world"]
print(letter_list_2)
print("-----------------------------------")

num_list = []
for num in "12345":
    if int(num)%2 == 0:
        num_list.append(num)
print(num_list)

num_list_2 = []
[num_list_2.append(num) for num in "12345" if int(num)%2 == 0]
print(num_list_2)




