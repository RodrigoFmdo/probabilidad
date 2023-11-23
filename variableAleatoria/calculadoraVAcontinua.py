# %%
import sympy as sp 

# %%
#input recibimos una funcion de x, e intervalos
def userInput():
    intervals = []
    valores = []
    porpartes = int(input("Es una funcion por partes?"))
    if porpartes == 1:
        nintervalos = int(input("cuantos intervalos tiene")) 
        for i in range(nintervalos):
            intervalstring = input("da intervalo y valor separado por comas")
            tempVector = intervalstring.split(',')
            intervals.append(tempVector[0])
            valores.append(tempVector[1])

        return intervals,valores
        
    else:
        fstring = input("da la funcion")
        return fstring

# %%
#integral 
#vamos a integrar f de -00 a 00
def integral(fstring):
    x = sp.symbols('x')
    f = sp.sympify(fstring)
    fintegral = sp.integrate(f,(x,-sp.oo,sp.oo))

    print(f"la integral de -inf a +inf de f es {fintegral}")

    if (fintegral==1):
        print("tu funcion es una funcion de distribucion de probabilidad")
        strInterval=input("da el intervalo [a,b] en la forma a,b para calcular la probabilidad de que la variable aleatoria tome valores en [a,b]" )
        a,b = strInterval.split(",")
        fintegralab =  sp.integrate(f,(x,a,b))

        print(f"la integral de f(x) en el intervalo [a,b] es {fintegralab}")
    else:
        print("tu funcion no es una distribucion de probabilidad")


# %%
#integral por trozos
def integralTrozos(intervals,valores):
    x= sp.symbols('x')
    sumintegrals=0
    for i in range(len(intervals)):
        intersplitted = intervals[i].split('_')
        fintegral = sp.integrate(valores[i],(x,intersplitted[0],intersplitted[1]))
        sumintegrals = sumintegrals + fintegral
    print(f"la integral de f(x) es {sumintegrals}")
    
    if (sumintegrals==1):
        print("tu funcion es una funcion de distribucion de probabilidad")
        strInterval=input("da el intervalo [a,b] en la forma a,b para calcular la probabilidad de que la variable aleatoria tome valores en [a,b]" )
        a,b = strInterval.split(",")
        for i in range(len(intervals)):
            fintegralab = sp.integrate(valores[i],(a,b))
            sumintegralsab = sumintegralsab + fintegralab
        print(f"La integral de f(x) en el intervalo [a,b] es {sumintegralsab}")
    else:
        print("tu funcion no es una distribucion de probabilidad")

# %%
#main
u = userInput()
if type(u) == str:
    integral(u)
elif (type(u) == tuple):
    integralTrozos(u[0], u[1])




