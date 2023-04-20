def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for x in integers():
            yield x / 2

    def take(n, seq):
        result = []
        for x in range(n):
            result.append(next(seq))
        return result

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))