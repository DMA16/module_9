def all_variants(text):
    for i in range(len(text)):
        first = 0
        second = i
        while second < len(text):
            yield text[first:second + 1]
            first, second = first + 1, second + 1



a = all_variants("abcd")
for i in a:
    print(i)