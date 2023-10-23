#your_function_name = lambda inputs : output
a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)

l = [2,4,7,3,14,19]
odd_num= lambda i: print(i%2==1)
for i in l:
    # your code here
    odd_num(i)
    
l = [2,4,7,3,14,19]
for i in l:
    # your code here
    my_lambda = lambda x : print((x % 2) == 1)
    my_lambda(i)