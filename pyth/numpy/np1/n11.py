def a(name,score):
    score.sort()
    print(score)


if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
    a(name,score)