spam = ['apples','bananas','tofu','cats']

def foo(list):
    length = len(list)
    commalist = ''
    print(type(commalist))
    print('length' + str(length))
 
    for el in list:
        print(list.index(el))
        if list.index(el)<length-1:
            commalist += el + ', '
        elif list.index(el)==length-1:
            commalist += 'and ' + el 
    return commalist

expose = foo(spam)
print(expose)
