import numpy as np

def solution(A):
    N = dict()

    for i in range(len(A)):
        N[A[i]] = i


    for i in range(len(A)):
        if i not in N.keys():
            return i
        else:
            i+1


    return




A = [-1, 5, 3, 6, 5, 1, 123, -12345, 1, 0, 2, 3, 4, 5, 6]

Answer = solution(A)
print(Answer)