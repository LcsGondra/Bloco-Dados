sample_input='1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'
rooms = sample_input.split()

repeat_set = set()
unique_set = set()

for r in rooms:
    if r not in unique_set:
        unique_set.add(r)
    else:
        repeat_set.add(r)
        


cap_room = unique_set - repeat_set
print( list(cap_room)[0])