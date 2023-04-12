notas=[]
# ----------------------------mostrar notas-------------------------
def leernotas():
    while True:
        n=float(input("ingresar notas (0 para salir): "))
        if n== 0:
            print("¡listo!") 
            break
        if n < 1:
            print("nota mal ingresada escriba nuevamente")
            return(n)
        if n > 7:
            print("nota mal ingresada escriba nuevamente")
            return(n)  
        notas.append(n),    
    print("las notas son:",notas)
# ------------mostrar numero de notas y promedio---------------------
def promedio():
    nu= len(notas)
    print("tienes",nu,"notas" )

# ------------mostrar nota mas alta y baja---------------------

def mayor(notas):
    max = notas[0];
    for x in notas:
        if x > max:
            max = x
    return max    
 
def menor(notas):
    min = notas[0];
    for x in notas:
        if x < min:
            min = x
    return min

def main(notas):
    print ("la nota mayor: es ", mayor(notas))
    print ("la nota menor: es ", menor(notas))
leernotas()
promedio()
main(notas)