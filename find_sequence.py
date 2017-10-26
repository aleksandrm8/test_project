def find_sequence(A): # ищем число которое входит в нашу последовательность и смещение последовательности относительно его
    int_sequence=int(A)
    if int_sequence==0: # проверяем вариант ввода последовательности нулей
        return [10**len(A), 1]
    int_sequence=10**len(A)-1 # задаем максимально возможное значение
    shift=0 # shift - смещение последовательности относительно искомого числа
    for i in range(0, len(A)): # проверяем числа которые целиком попадают в последовательность
        if A[i]=='0':
            continue # пропускаем числа начинающиеся с нуля
        for j in range(i, min(i+len(str(int_sequence)), len(A))):
            int_number=int(A[i:j+1]) # int_number - проверяемое число
            ok = 1
            if i>0: # если число начинается не с первой позиции сравниваем его с предыдущим числом
                str_do=str(int_number-1) # str_do - предыдущее число
                if len(A[:i])>=len(str_do): # если перед числом цифр больше чем его длина, то число слишком далеко
                    ok=0
                else:
                    i_str_do=len(str_do)-1
                    for x in range(len(A[:i])-1,-1,-1): # сравниваем все предыдущие цифры
                        if A[x]!=str_do[i_str_do]:
                            ok=0
                            break
                        i_str_do-=1
            if not(ok):
                continue
            number=int_number # сравниваем число с последующими числами
            i_end=len(str(number))+i # i_end - индекс конца числа
            while True:
                str_number=str(number+1)
                for x in range(0, min(len(str_number),len(A)-i_end)):
                    if str_number[x]!=A[i_end+x]:
                        ok=0
                        break
                if i_end>=len(A) or not(ok):
                    break
                number+=1
                i_end+=len(str_number)
            if ok: # если найдено подходящее число
                if int_number<int_sequence: # и если оно меньше найденых до этого, то запоминаем его
                    int_sequence=int_number
                    if i>0:
                        shift=-1*len(A[:i])
                    else:
                        shift=0
                break
        if i!=0: # проверяем числа не вошедшие в последовательность целиком
            for add in range(1, len(str(int_sequence))-len(A[i:])+1): # add - все возможные длины добавляемого хвоста 
                if len(A[:i])>=len(A[i:])+add:
                    continue
                str_add = A[i:]+A[i-add:i] # добавляем хвост из начала последовательности, получается предыдущее число
                int_add_next = int(str_add)+1 # при прибавлении 1 возможно увеличение старшего разряда
                str_add_next = str(int_add_next)
                str_number = A[i:]+str_add_next[len(str_add_next)-add:] # берем начало числа из последовательности, а конец из найденого числа
                int_number = int(str_number) # получаем искомое число без возможного увеличения саршего разряда
                str_add = str(int_number-1) # получаем правильное предыдущее число
                if A[:i]!= str_add[len(str_add)-len(A[:i]):]: # сравниваем полученный хвост
                    continue
                if int_number<=int_sequence:
                    int_sequence=int_number
                    shift=min(shift, -1*len(A[:i]))
    return [int_sequence, shift]
while True:
    A=str(input())
    try:
        int_sequence=int(A) # проверяем нет ли лишних символов
    except ValueError:
        print("Nepravilniy vvod")
        break
    [int_sequence, shift] = find_sequence(A) # ищем число которое входит в нашу последовательность и смещение последовательности относительно его 
    str_sequence=str(int_sequence)
    index=0
    for i in range(1, len(str_sequence)): # подсчитываем сколько символов перед найденым числом
        index+=9*(10**(i-1))*i
    index+=1
    index+=(int_sequence-(10**(len(str_sequence)-1)))*len(str_sequence)
    print(index+shift)
