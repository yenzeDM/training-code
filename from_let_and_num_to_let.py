with open('dataset_3363_2.txt') as file, open('number.txt', 'w') as word:
    for i in file:
        li_word = i.replace('', ' ').split()
        li_word.append(' ')
        count, flag = -1, True
        while flag:
            count += 1
            if li_word[count].isalpha():
                inter = li_word[count]
            elif li_word[count].isdigit() and li_word[count+1].isdigit():
                inter2 = li_word[count] + li_word[count+1]
                word.write(f'{inter * int(inter2)}')
                count += 1
            elif li_word[count].isdigit():
                inter2 = li_word[count]
                word.write(f'{inter * int(inter2)}')
            else:
                flag = False