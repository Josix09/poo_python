# composión
""" una cordenada en 2 dimensiones está compuesta por 2 valores, el valor en el eje de las X y el valor en el eje de las Y, esto podría ser una clase. Un cuadrado está compuesto por 4 coordenadas que son los 4 vértices,esto podría ser una clase que está compuesta por 4 clases del objeto coordenada."""
#clase coordenada

class Coordenada:
    #método constructor
    def __init__(self,x,y):
        self.X=x
        self.Y=y


    #método para mostrr coordenadas
    def mostrarCoordenadas(self):
        print("(", self.X, "," , self.Y, ")")


#clase cuadrado

class Cuadrado:
    def __init__(self,v1,v2,v3,v4):
        self.V1=v1
        self.V2=v2
        self.V3=v3
        self.V4=v4

    #método para mostras los vértices
    def mostrarVertices(self):
        print("El cuadrado está compuesto por los siguientes vértices: ")
        self.V1.mostrarCoordenadas()
        self.V2.mostrarCoordenadas()
        self.V3.mostrarCoordenadas()
        self.V4.mostrarCoordenadas()


#metodo principal
def main():
    #input
    x1=int(input("Digite el valor de X: "))
    x2=int(input("Digite el valor de y: "))


    #processing
    c1=Coordenada(x1,x2)
    c1.mostrarCoordenadas()

    v1=Coordenada(7,8)
    v2=Coordenada(10,8)
    v3=Coordenada(7,5)
    v4=Coordenada(10,5)

    cuadrado1=Cuadrado(v1,v2,v3,v4)
    cuadrado1.mostrarVertices()

if __name__ == "__main__":
    main()