numero = int(input('ingrese Numero: '))

#Fibonacci
fibonacci = (lambda fun: lambda arg: fun(fun,arg)) (lambda f,a:0 if a==0 else (1 if a==1 else f(f,a-1)+f(f,a-2))) (numero)
print(fibonacci)


#Factorial
factorial = (lambda fun: lambda arg: fun(fun,arg)) (lambda f,a: 1 if a ==0 else a*f(f,a-1))(numero)
print(factorial)

