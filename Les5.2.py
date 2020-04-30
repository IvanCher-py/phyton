lines = 0
words = 0
with open("text_2.txt", "r") as cool:
    for i in cool:
        print(i, end=' ')
        i = i.split()
        word = len(i)
        words += int(word)
        print(f"- Количество слов в строке {word}")
        lines += 1
print(f"Всего количество строк в файле: {lines}"
      f"\nВсего количество слов: {words}")
