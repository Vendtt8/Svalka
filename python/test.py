# объявление функции
def print_perm_time_call(msc_time): #07:30
    msc_time = list(map(int, msc_time.split(':'))) # [7, 30]
    prm_time = msc_time
    if msc_time[0] < 8:
        prm_time[0] = prm_time[0] + 2 # [9, 30]
        print(f'Созвон будет в {'0' + str(prm_time[0])}:{prm_time[1]}')
    else:
        print(f'Созвон будет в {prm_time[0]}:{prm_time[1]}')

# считываем данные
msc_time = input()

# вызываем функцию
print_perm_time_call(msc_time)