# BY CHATGPT
# CONVERTIDO DE UMA SOLUÇÃO EM C++ ENCONTRADA NA INTERNET
# NÃO TESTADA

def calcula(a, b, coratual, pos, resatual):
    if pos > n:
        return resatual
    if lista[pos] == coratual:
        resatual += 1
        coratual = b if coratual == a else a
    if pos == n:
        return resatual
    return calcula(a, b, coratual, pos + 1, resatual)


if __name__ == "__main__":
    n = int(input())
    lista = [0] * (n + 1)
    p = [-1] * (n + 1)

    for i in range(1, n + 1):
        a = int(input())
        lista[i] = a
        if p[a] == -1:
            p[a] = i

    res = 1
    for i in range(1, n + 1):
        if p[i] != -1:
            for j in range(i + 1, n + 1):
                if p[j] != -1:
                    res1 = calcula(i, j, i, p[i], 0)
                    res2 = calcula(j, i, j, p[j], 0)
                    resatual = max(res1, res2)
                    if resatual > res:
                        res = resatual

    print(res)