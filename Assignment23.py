def fun(a,b=6,c=8):
    print(a,b,c)

fun(1,2)


def fun(a,b,c=5):
    print(a,b,c)

fun(1,c=3,b=2)

def fun(a,**kargs):

    print(a,kargs)


fun(a=1,c=3,b=2)


def fun(a,b,c=8,d=5):
    print(a,b,c,d)

fun(1,*(5,6))


def func(a,b,c):
    a =2;
    b[0]="x";
    c["a"]="y";
    l = 1;
    m =[l];
    n={"a":0}

func(l,m,n)


def func(a,b,c):
    a=2
    b[0]="x"
    c["a"] = "y"
    i =1
    m=[i]
    n={"a":0}
func(i,m,n)




    
    
    
      



