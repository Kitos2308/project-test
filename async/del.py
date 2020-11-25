





def couroutine(func):
    def inner(*args, **kwargs):
        g= func(*args, **kwargs)
        g.send(None)
        return g
        

    return inner





class BlaBlaException(Exception):
    pass



def subgen():
    while True:
        try:
            message=yield
        except StopIteration:
            #print("KU-KU epta!")
            break
        else:
            print('-------------',message)
        
    return 'Returned from subgen()'


@couroutine
def delegator(g):
    # while True:
    #     try:
    #         data=yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)




