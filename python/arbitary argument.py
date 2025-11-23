def find_sun(*numbers):
    result=0
    for num in numbers:
        result=result+num
    print("sum:",result)
find_sum(80,50,100)
find_sum(100,200)
find_sum(200,350,450)


def add(a=10,b=20e,c=30):
    sum=a+b+c
    print("sum",sum)
add(50,100,200)
add(500,700)
add(a=600)
add()
     