def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

n = 6

# cek valid
if n<= 0:
   print("Input bilangan positif")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(fibo(i))

