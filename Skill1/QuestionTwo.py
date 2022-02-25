import math
class Perimeter:
    def rectangle(self,side1,side2):
        self.side1=side1
        self.side2=side2
        Peri=2*(side1+side2)
        Area=side1*side2
        print('Perimeter of the Rectangle : ', Peri)
        print('Area of the Rectangle : ',Area)

    def circle(self,radius):
        self.radius=radius
        Peri=2*math.pi*radius
        Area=math.pi*radius*radius
        print('Perimeter of the Circle : ', Peri)
        print('Area of the Circle : ', Area)

    def triangle(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        Peri=side1+side2+side3
        perimeter=Peri/2
        tri=perimeter*(perimeter-side1)*(perimeter-side2)*(perimeter-side3)
        Area=math.sqrt(tri)
        print('Perimeter of the Circle : ', Peri)
        print('Area of the Circle : ', Area)
p=Perimeter()
print('Enter the sides of the Rectangle')
a,b = map(int, input().split())
p.rectangle(a,b)
print('Enter the radius of the Circle')
r=int(input())
p.circle(r)
print('Enter the sides of the triangle')
m,n,o= map(int, input().split())
p.triangle(m,n,o)