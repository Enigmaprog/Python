import pickle as p

def create():
    print()
    fName = input('Input file name\'s: ')
    f = open(fName, 'w')
    heads = []
    x = None
    while x != 'x':
        x = input('Введите строку базы данных, x - выход:\n')
        print()
        if x != 'x':
            heads.append(x)
    return fName, heads
        
        

def add(args = []):
    print()
    # args[0] - fName, args[1] - heads

    f = open(args[0], 'ab')
    book = {}
    print('---Ввод значений базы данных---')
    for i in args[1]:
        book[i] = input(i + ': ')
    p.dump(book, f)

def dell(args = []):
    f = open(args[0], 'rb+')
    choose = int(input('Введите № удаляемой записи: '))
    records = []
    while True:
        try:
            records.append(p.load(f))
        except:
            break
    f = open(args[0], 'wb')
    for i in range(len(records)):
        if i+1 != choose:
            p.dump(records[i], f)


def findByField(args = []):
    f = open(args[0], 'rb+')
    while True:
        field = input('Введите поле: ')
        if field in args[1]:
            break
        else:
            print('Такого поля не существует!')

    value = input('Введите значение: ')
    flag = True
    while True:
        try:
            print()
            obj = p.load(f)
            if obj[field] == value:
                for i in obj.items():
                    print(i[0] + ':\t' + i[1] + '\t\t', end = "")
                print()
                flag = False
        except:
            break
    if flag:
        print('Такого поля не существует!')
            
    
def printBase(args = []):
    print()
    f = open(args[0], 'rb')
    while True:
        try:
            obj = p.load(f)
            
            for i in obj.items():
                print(i[0] + ':\t' + i[1] + '\t\t', end = "")
                
            print()
        except:
            break
        
    
c = None
while c != 'x':
    print('-----Menu-----')
    print('1. Создать базу данных')
    print('2. Добавить запись')
    print('3. Удалить запись')
    print('4. Поиск по полю')
    print('5. Вывод базы данных')
    print('x - Exit')
    c = input('Ввод: ')
    
    if c == '1':
        bd = create()
    elif c == '2':
        try:
            add(bd)
        except:
            print('ERROR: Базы данных не существует!')
    elif c == '3':
        try:
            dell(bd)
        except:
            print('ERROR: Базы данных не существует!')
    elif c == '4':
        try:
            findByField(bd)
        except:
            print('ERROR: Базы данных не существует!')
    elif c == '5':
        try:
            printBase(bd)
        except:
            print('ERROR: Базы данных не существует!')
    
       
        
    print()
    




