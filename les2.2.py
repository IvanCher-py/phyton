s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, len(s), 2):
    s[i - 1], s[i] = s[i], s[i - 1]
    print(s)
