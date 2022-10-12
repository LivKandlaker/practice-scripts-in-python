from random import randrange


def solution(S, K):
    """
    function that get list of week days name and positive integer number and return the name day after K days
    :param S: list of week days list type(str)
    :param K: positive integer number
    :return: the name day after K days
    """
    S_Array = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    counter = 0
    while K >= 7:
        K = int(K - 7)
    for i in S_Array:
        if i == S:
            if (counter + K) >= 7:
                Res = counter + K - 7
            else:
                Res = counter + K
            return S_Array[Res]
        else:
            counter += 1

S = 'sun'
K = randrange(0,500)
ANS = solution(S,K)
print(ANS)