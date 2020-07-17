 #문제1
""" A, B = map(int, input().split())

if A > B :
    print('>')
elif A < B :
    print('<')
else :
    print('==') """

 #문제2
""" 
A = int(input())
if (A%4 == 0) and (A%100 != 0) or (A%400 == 0 ):
    print(1)
else :
    print(0) """

 #문제3
""" x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)  """

 #문제4
""" H, M = map(int, input().split())
if M > 44 :
    print(H, M-45)
elif M <= 44 and H >= 1:
    print(H-1, M+15)
else:
    print(23, M+15) """

 #문제5
""" print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\__|") """