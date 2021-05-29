#Python
- everything in python is an object
- function in python is first class function (you can pass function as a parameter)

# Closure
- access to variables, functions, classes from different(outer) scope
- variables are stored in function object
## Creation
1. Need to have min 2 functions, one outer, one inner
2. Outer function should return declaration of inner function
3. Inner function have to use something from outer function (variable, other function, class), and only this will be recorded

## Use case:
- persistence (trwałość)
pomiędzy wywołaniami funkcji jesteśmy w stanie zapamiętać stan. Np przy połączeniu z bazą danych (?)
  
## Cons:
- if you don't understand you can leak memory (spowolnienie aplikacji) 

