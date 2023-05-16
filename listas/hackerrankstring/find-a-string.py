def count_substring(string, sub_string):
    inicio = 0
    fim = len(sub_string)
    counter = 0
    for i in string:
        if string[inicio:fim] == sub_string:
            
            counter +=1
        inicio += 1
        fim += 1
    return counter

string = input('string inicial: ').strip()
sub_string = input('substring: ').strip()

count = count_substring(string, sub_string)
print(count)