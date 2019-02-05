def check_power(N, k):
    if N <= 0 or k <= 0:
        raise ValueError("N and k should be greater than 0")
    if k == 1:
        return N == 1

    for i in count(1):
        x = k ** i
        if x == N :
            return True
        elif x > N:
            return False
