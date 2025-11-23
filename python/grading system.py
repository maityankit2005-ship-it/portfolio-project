maths=int(input("enter marks of maths"))
science=int(input("enter marks of science"))
english=int(input("enter marks of english"))

totalmarks = maths+science+english
print(totalmarks)
z=(totalmarks/300)*100
print(z)

if (z<=100)and(z<=90):
    print("A grade")
elif(z<=89)and(z<=75):
    print("B grade")
elif (z<=74)and(z<=60):
    print("C grade")
elif(z<=59)and(z<=40):
    print("D grade")
else:
    print("fail")
