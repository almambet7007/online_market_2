ten = list(range(1, 11))
evens = list(filter(lambda i: i % 2 == 0, ten))
evens1 = list(map(lambda i: i ** 2, evens))
print(evens1)
def function(lst=ten):
    while True:
        index = input("Введите индекс для вывода объекта из списка:")
        if index == 'q':
            break
        try:
                print(lst[int(index)])
        except:
            print(f'enter index from 0 to {len(lst)-1}')
function()