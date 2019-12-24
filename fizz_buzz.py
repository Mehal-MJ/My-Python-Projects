def fizz_buzz(x):
    if x%3==0 and x%5!=0:
        print('Fizz')
    elif x%5==0 and x%3!=0:
        print('Buzz')
    elif x%5==0 and x%3==0:
        print('Fizz Buzz')
    else:
        print(x)

#fixed input
fizz_buzz(16)

x=[1,2,5,3,4,5,6]
print(x.index(x[0]+5))