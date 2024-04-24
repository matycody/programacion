class Punto():
    
    def eje_x(self):
        return self.eje_x
    
    def eje_y(self):
        return self.eje_y
    
    def __init__(self, x,y):
        self.x =x
        self.y =y 
    
    def imprimir(self):
        return f"({self.x}, {self.y})"
        
    def opuesto(self):
        
        return Punto(-self.x, -self.y)
        # return Punto(self.eje_x()*-1,self.eje_y()*-1)
    
p= Punto(2,3)
q=p.opuesto()
print(type(q))
print(p.imprimir())
print(q.imprimir())
