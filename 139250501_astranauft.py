# 139250501

def conter_astranafts(N: int, K: int) -> int:
    if N == 0 or K == 0:
        return 0  # Базовый случай.
    if N == 1:
        return 1  # Базовый случай.
    return ((conter_astranafts(N - 1, K) + K - 1) % N) + 1


if __name__ == '__main__':
    N = int(input())  # Количество претендентов.
    K = int(input())  # Количество тактов в считалке.
    print(conter_astranafts(N, K))
