def frogJumps(X, A , I):
    if I >= 0 and I < len(A) and X in A[I:]:
        first = A.index(X,I)
        aSum , xSum = sum(list(set(A[0:first+1]))) , (X*(X+1))/2
        return first if aSum == xSum else frogJumps(X, A, I+1)
    else:
        return -1

def solution(X, A):
    # write your code in Python 3.6
    return frogJumps(X,A,0)
print(solution(5, [1, 2, 3, 5, 3, 1]))