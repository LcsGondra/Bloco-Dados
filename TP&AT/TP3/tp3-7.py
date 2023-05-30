antenas = int(input("numero de antenas: "))
olhos = int(input("numero de olhos: "))

if antenas >= 3 and olhos <= 4:
    print('marciano')
if antenas <= 6 and olhos >= 2:
    print('saturniano')
if antenas <= 2 and olhos <= 3:
    print('mercuriano')