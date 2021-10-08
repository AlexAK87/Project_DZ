
def get_ASCII_table(left, right):
    list_table = []
    count = 0
    for i in range(left, right+1):
        list_table.append('{} - "{}"'.format(i, chr(i)))
        count += 1
        if count == 10 or i == right:
            print(', '.join(list_table))
            list_table.clear()
            count = 0


get_ASCII_table(32, 127)



