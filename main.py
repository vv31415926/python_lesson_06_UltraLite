'''
1. написать тест для своей функции;
2. запустить тест
'''

def myFun( a,b ):
    r = None
    try:
        r = a / b
    except ZeroDivisionError as e:
        print(  'ошибка:',e)
    else:
        print(   'все ОК')
    finally:
        print( 'Функция завершена.')

    return r

print(   myFun( 2,0 )   )