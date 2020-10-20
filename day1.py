def test1(ab,**a):
    print(ab,a)

def test2():
    m1 = {1:'a', 2:'b'}
    m2 = {3:'c', 4:'d'}
    a = (m1,m2)
    print(a)
    m1={2:'a'}
    a[0]=m1
    print(a)

if __name__ == '__main__':
    test1(2, b=3)
    test2()
