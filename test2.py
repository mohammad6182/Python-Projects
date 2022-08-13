


myWords = 'is my favorite combination of car and color'

color_list= ['black', 'blue', 'red', 'white']

def car_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name, myWords,i)
        lst.append(msg)
    return lst


def get_name():
    go = True
    while go:
        name = input('what is your name?')
        if name =='':
            print('you need to provide your name')
        elif name == "mohammad":
            print('sallam')
        else:
            go= False
    lst = car_function(name)
    for i in lst:
        print(i)
            
get_name()
