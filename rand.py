mod1 = 2147483563
mod2 = 2147483399
mult1 = 40014
mult2 = 40692
seed1 = 12345
seed2 = 67890


def seed(n):
    global seed1, seed2, mod1, mod2
    if n < 0:
        n = -n
    if n == 0:
        seed1 = 12345
        seed2 = 67890
    else:
        seed1 = (mult1 * n) % mod1
        seed2 = n % mod2


def rand():
    global seed1, seed2, mod1, mod2, mult1, mult2
    result = 0
    seed1 = (seed1 * mult1) % mod1
    seed2 = (seed2 * mult2) % mod2
    result = (seed1 - seed2) / mod1
    if result < 0:
        result = result + 1
    return round(result, 5)


def randInt(min, max, count=None):
    if count is None:
        return min + int((max - min + 1) * rand())
    else:
        result = [randInt(min, max) for _ in range(count)]
        return result


def randIntNoRep(min, max, count=None):
    if count is None:
        result = list(range(min, max + 1))
        count = len(result)
        for i in range(count, 0, -1):
            j = randInt(0, count - 1)
            result[i - 1], result[j] = result[j], result[i - 1]
        return result
    else:
        result = []

        inc = False
        failures = 0
        while len(result) < count:
            num = randInt(min, max)

            if num in result:
                failures += 1
                if failures == 3:
                    inc = not inc
                    while num in result:
                        if inc:
                            num += 1
                            if num > max:
                                num = min
                        else:
                            num -= 1
                            if num < min:
                                num = max
                    failures = 0
                    result.append(num)
            else:
                failures = 0
                result.append(num)
        return result
