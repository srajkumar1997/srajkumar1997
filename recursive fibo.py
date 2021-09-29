
def recur_fibo(num):
   if num <= 1:
       return num
   else:
       return(recur_fibo(num-1) + recur_fibo(num-2))
nterms = 20
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
