#clase coordenada

class Coordenada:
    #método constructor
    def __init__(self,x,y):
        # atributos privados
        self.__X=x
        self.__Y=y

    #métodos de lecutra y escritura de atributos
    def getX(self):
        return self.__X
    
    def getY(self):
        return self.__Y
    
    def setX(self,x):
        self.__X=x

    def setY(self,y):
        self.__Y=y

    #método mostrar coordenada
    def mostrarCoordenadas(self):
        print("(", self.__X, "," , self.__Y, ")")


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
        self.__V1.mostrarCoordenadas()
        self.__V2.mostrarCoordenadas()
        self.__V3.mostrarCoordenadas()
        self.__V4.mostrarCoordenadas()

   # métodos privados para mostrar los vertices
    def _mostrarcoordenadasV1(self):
        print("(", self.__V1.getX(), "," , self.__V1getY(), ")")
    
    def _mostrarcoordenadasV2(self):
        print("(", self.__V2.getX(), "," , self.__V2getY(), ")")
    
    def _mostrarcoordenadasV3(self):
        print("(", self.__V3.getX(), "," , self.__V3getY(), ")")

    def _mostrarcoordenadasV4(self):
        print("(", self.__V4.getX(), "," , self.__V4getY(), ")")     


    # método para mostrar los vértices
    def mostrarVertices(self):
        print("el cuadrado está compuesto por los siguientes vertices: " )
        self.__mostrarcoordenadasV1()
        self.__mostrarcoordenadasV2()
        self.__mostrarcoordenadasV3()
        self.__mostrarcoordenadasV4() 

#metodo principal del módulo
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

#qué ocurre si el método getX() lo hacemos privado: __getX()?



if __name__ == "__main__":
    main()