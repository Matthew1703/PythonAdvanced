dct = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'],
       6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

english_words = ['hello', 'good', 'cats', 'dogs', 'query', 'dirty']
def my_t9(strin: str):
    count = 0
    new_str = ''
    for i in range(len(strin)-1):
        symbol = int(strin[i])
        if symbol == 7 or symbol == 9:
            delit = 4
        else:
            delit = 3
        if strin[i] == strin[i+1]:
            count += 1
        else:
            new_str += dct[symbol][count % delit]
            count = 0
    new_str += dct[int(strin[-1])][count % delit]

    lst = []
    for word in english_words:
        if word[0] == new_str[0] and word[-1] == new_str[-1] \
                and len(word) - 3 < len(word) < len(new_str) + 3:
            lst.append(word)
    print('Изначальная строка из цифр:', strin)
    print('Конвертированная строка из цифр:', new_str)
    print('Слова, которые могут получиться:', ''.join(lst))

my_t9("22244228687777")

