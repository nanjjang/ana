#def makeFishShapeBun(taste):
#    print(f"{taste}맛 붕어빵 완성!")
#    print("맛있게 드세요")
    
#makeFishShapeBun("팥")
#makeFishShapeBun("슈크림")
#-----------------------------------------------------------#
#x = 10

#def example():
#    x = 20
#    print(x)

#example()
#print(x)
#-----------------------------------------------------------#
#def for10(text):
#    for i in range(10):
#        print(text)
        
#for10("Hello World")
#-----------------------------------------------------------#
def sort(a,b,c):
    if a > b:
        if b > c:
            print(c,b,a)
        elif b<c:
            print(b,c,a)
    elif b > c:
        if a > c:
            print(c,a,b)
        elif a<c:
            print(a,c,b)
    elif c > a:
        if a > b:
            print(b,a,c)
        elif a<b:
            print(a,b,c)

sort(1,4,3)