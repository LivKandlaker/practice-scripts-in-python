def solution(A):
    A = sorted(set(A))
    current_i_val = 0
    previous_i_val= 0
    print(A)
    for i in A:
        if i > 0:
            current_i_val = i
            if previous_i_val + 1 < current_i_val:
                return previous_i_val + 1
            else:
                previous_i_val = current_i_val
    return current_i_val +1


A = [-1, -4, 80, 29, 15, 7, 4, 1, 2, 13, 5, 5, 7, 11, 3]
Answer = solution(A)
print(Answer)
