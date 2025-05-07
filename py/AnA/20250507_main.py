# class Hello:
#     def hello_world(self):
#         print("Hello World!")

# a = Hello()
# a.hello_world()



# class Triangle:
#     def make_triangle(self):
#         for i in range(10):
#             for j in range(i+1):
#                 print("*",end="")
#             print()

# a = Triangle()
# a.make_triangle()



# class Member:
#     def __init__(self, name):
#         self.name = name

#     def member_me(self):
#         print("제 이름은 {} 입니다.".format(self.name))

# a = Member("윤준서")
# a.member_me()


# class Myinfo:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
    
#     def member_me(self):
#         print("제 이름은 {0} 이고, 나이는 {1} 이고, 사는 지역은 {2} 입니다.".format(self.name, self.age, self.address))

# a = Myinfo("윤준서", "17", "서울")
# a.member_me()

a = int(input())
class Bread:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def buy(self):
        if(a == 0):
            print("재고가 없습니다.")

        else:
            print("구매해주셔서 감사합니다.")
            self.stock = -1
    
    def bake(self, stock):
        self.stock += stock
        print(f"{self.name}을/를 {stock}개 만들었습니다.")

class Bun(Bread):
    def __init__(self, name, price, inside):
        super().__init__(name, price)
        self.inside = inside
    
    def buy(self):
        super().buy()

    def bake(self):
        print("만들기 실패!")

x = Bread("붕어빵", 1000, 10)
x.bake(4)
for i in range(15):
    x.buy()

y = Bun("카스테라",1000,"연유")
y.bake(3)
for i in range(10):
    y.buy()

#엄 이거 이상한데요 ...ㅋㅋㅋ