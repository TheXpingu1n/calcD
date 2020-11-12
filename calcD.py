#coded by : Azad Mohammed
import math
import pyfiglet
import termcolor
print(termcolor.colored(pyfiglet.figlet_format('calcD'), color = 'green'))
pi = math.pi
e = math.exp
tan = math.tan
cos = math.cos
sin = math.sin

class Calculate_Areas2D:
   
   def circle_area(self) :
       rad = input('Please insert the value of the radius : ')
       r = int(rad)
       circleA = (pi * (pow(r, 2)))
       print(f'The area is : {circleA} cm²')
   
   def tri_area(self) :
        b = input('Insert a value of the base : ')
        h = input('Insert a value of the height : ')
        bas = int(b)
        hei = int(h)
        triangleA = float(0.5) * bas * hei
        print(f'The area is : {triangleA} cm²')
  
   def squ_area(self) :
        a = input('The length of the side : ')
        side = int(a)
        sqA = pow(side * 2)
        print(f'The area is : {sqA} cm²')
   
   def rect_area(self) :
        l = input('The length please : ')
        w = input('And the width : ')
        leng = int(l)
        wid = int(w)
        rectA = leng * wid
        print(f'The area is {rectA} cm²')
   
   def para_area(self):
        b = input('The base length please : ')
        h = input('And the height legnth : ')
        basee = int(b)
        hei = int(h)
        paralA = basee * hei
        print(f'The area is : {paralA} cm²')
   
   def trap_area(self):
          APa = input('Please enter the first parallel line : ')
          BPa = input('Please enter the second parallel line : ')
          Hei = input('Height : ')
          APara = int(APa)
          BPara = int(BPa)
          H = int(Hei)
          trapizumA = 0.5 * (APara + BPara) * H
          print(f'The area is : {trapizumA} cm²')
  
   def elipise_area(self) :
          a = input('Enter length of major axis : ')
          b = input('Enter length of minor axis : ')
          sideA = int(a) * 0.5
          sideB = int(b) * 0.5
          elipA = pi * sideA * sideB
          print(f'The area : {elipA} cm²')
  
   def Cres_area(self):
          RR = input('Please enter your first radius (biggest) length : ')
          r = input('Please enter your second radius (smallest) length : ')
          rad1 = int(RR)
          rad2 = int(r)
          AofC = (pi*rad1**2)-(pi*rad2**2)
          print(f'The area is : {AofC} cm²')
   
   def rhombus_area(self):
      print('''Choose *By numbers* : \n
        1- Rhombus area by height and side '1' \n
        2- One side one angle '2' \n
        3- Length of diagonals '3' ''')
      ChooseNo = input('Enter the number : ')
      no = int(ChooseNo)
      no1 = 1
      no2 = 2
      no3 = 3
      
      def rhombus_area1(self):
             h = input('Enter the height : ')
             s = input('Enter the side : ')
             Height = int(h)
             Side = int(s)
             area1 = Height * Side
             print(f'The area is : {area1} cm²')
     
      def rhombus_area2(self):
             s = input("Enter length of side : ")
             Mesaure = input('And the measurment of angle : ')
             Side1 = int(s)
             MofAngle = int(Mesaure)
             area2 = pow(Side1 , 2)*sin(MofAngle)
             print(f'The area is : {area2} cm²')
             
      def rhombus_area3(self):
             d = input('Enter the length of the first diameter : ')
             d2 = input('And the second diameter : ')
             di1 = int(d) 
             di2 = int(d2)
             area3 = (di1 * di2) / 2
             print(f'The area is : {area3} cm²')
      if no == no1 :
           rhombus_area1(1)
      elif no == no2 :  
           rhombus_area2(2)
      elif no == no3 :
           rhombus_area3(3)
      else:
           raise ValueError
           Calculate_Areas2D.rhombus_area(0)


class Calculate_Areas3D: 
    
     def Cube_surfarea(self):
          edge = input('Please enter length of edge : ')
          A = int(edge)
          surfAreaC = 6*A**2
          print(f'The area is : {surfAreaC} cm³')
    
     def RecPrism_surArea(self):
         l = input('Enter the length : ') 
         w = input('Enter the width : ')
         h = input('Enter the height : ')
         length = int(l)
         width = int(w)
         height = int(h)
         surfArea = 2 * (width*length) + (height*length) + (height*width)
         print(f'The area is : {surfArea} cm³')
    
     def Cy_surfarea(self):
         radius = input('Enter the length of the radius : ')
         height = input('And the height : ')
         r = int(radius)
         h = int(height)
         area = 2 * pi * r * (r + h)
         print(f'The area is : {area} cm³')
   
     def Cone_surfarea(self):
          radius = input('Enter the length of the radius : ')
          height = input('Enter the length of the slant height : ')
          r = int(radius)
          h = int(height)
          area = pi * r * (r + h)
          print(f'The area is : {area} cm³')
   
     def Sp_surfArea(self):
          radius = input('Enter the length of the radius : ')
          r = int(radius)
          area = 4 * pi * r**2
          print(f'The area is : {area} cm³')
   
     def hemiSp_surfArea(self):
          radius = input('Enter the length of the radius : ')
          r = int(radius)
          area = 3 * pi * pow(r , 2)
          print(f'The area is : {area} cm³')
    
     def pyramid_LSA(self):
          per = input('Enter the perimeter : ')
          height = input('And the slant height : ')
          p = int(per)
          l = int(height)
          area = 0.5 * p * l 
          print(f'The area is : {area} cm³')
    
     def pyramid_TSA(self):
          per = input('Enter the perimeter : ')
          height = input('And the slant height : ')
          Base = input('Input the base too : ')
          p = int(per)
          l = int(height)
          B = int(Base)
          area = 0.5 * p * l + B
          print(f'The area is : {area} cm³')

class Calculate_Areas_Plat5:

     def Tetrahedron(self):
          def Tetrahedron_1(self):
               side = input('Enter the length of the side : ')
               a = int(side)
               area = 3 * (math.sqrt(3))/4 * a ** 2
               print(f'The area is : {area} cm³')
          def Tetrahedron_2(self):
               side = input('Enter the length of the side : ')
               a = int(side)
               area = 4 * (math.sqrt(3))/4 * a ** 2
               print(f'The area is : {area} cm³')
          choose = input('What do you want? Area of the slant surface to the tetrahedron ->> SA \n Area of whole surface of tetrahadron ->> WA \n >>> ').capitalize().strip()
          if choose == 'SA' : 
               Tetrahedron_1(0)
          elif choose == 'WA' : 
               Tetrahedron_2(0)
          else : 
                raise ValueError

     def hexahedron(self):
          print('it is just a cube, go and call the cube calc function.')

     def Octahedron(self):
          edge = input('Enter The length of the edge : ')
          a = int(edge)
          area = 2 * pow(a , 2) * math.sqrt(3)
          print(f'The area is : {area} cm³')

     def Dodecahedron(self):
          length = input('Enter the edge length : ')
          a = int(length)
          surfarea = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * a ** 2
          print(f'The area is : {surfarea} cm³')

     def Icosahedron(self):
          length = input('Enter the length of the side : ')
          a = int(length)
          area = 5 * math.sqrt(3) * a ** 2
          print(f'The area is : {area} cm³')


def open_pro():     
 print(''' Welcome \n For 2D shape area calculator enter : "T" \n For 3D shape area calculator enter : "A" \n For platonic solid area claculator enter "P" \n To quit enter 'Q' ''')
 answer = input('>> ').capitalize().strip()
 if answer == 'T' : 
      print('''Hello \n 
      - For Circle area calculator ->> 'C' \n
      - For Triangle area calculator ->> 'T' \n
      - For Square area calculator ->> 'S' \n
      - For Rectangle area calculator ->> 'R' \n
      - For Parallelogram area calculator ->> 'P' \n
      - For Trapizum area calculator ->> 'U' \n
      - For Ellipse area calculator ->> 'E' \n
      - For Cresent area calculator ->> 'N' \n
      - For Rhombus area calculator ->> 'H' \n
      ''')
      answer2 = input('>> ').capitalize().strip()
      if answer2 == 'C': 
                               Calculate_Areas2D.circle_area(0)
      elif answer2 == 'T':
                               Calculate_Areas2D.tri_area(0)
      elif answer2 == 'S':
                               Calculate_Areas2D.squ_area(0)
      elif answer2 == 'R':
                               Calculate_Areas2D.rect_area(0)
      elif answer2 == 'P':
                               Calculate_Areas2D.para_area(0)
      elif answer2 == 'U':
                               Calculate_Areas2D.trap_area(0)
      elif answer2 == 'E': 
                               Calculate_Areas2D.elipise_area(0)
      elif answer2 == 'N':
                               Calculate_Areas2D.Cres_area(0)
      elif answer2 == 'H': 
                               Calculate_Areas2D.rhombus_area(0)
      else :
           raise ValueError    
 elif answer == 'A':
      print('''Hello \n 
      - For Cube surface area calculator ->> 'C' \n
      - For Rectangular prism surface area calculator ->> 'R' \n
      - For Cylinder surface area calculator ->> 'Y' \n
      - For Cone surface area calculator ->> 'O' \n
      - For Sphere surface area calculator ->> 'S' \n
      - For Hemisphere surface area calculator ->> 'H' \n
      - For Pyramid Literal surface area calculator ->> 'L' \n
      - For Pyramid Total surface area calculator ->> 'T' \n
      ''')
      answer3 = input('>> ').capitalize().strip()
      if answer3 == 'C': 
                            Calculate_Areas3D.Cube_surfarea(0)
      elif answer3 == 'R': 
                            Calculate_Areas3D.RecPrism_surArea(0)
      elif answer3 == 'Y':
                            Calculate_Areas3D.Cy_surfarea(0)
      elif answer3 == 'O':
                            Calculate_Areas3D.Cone_surfarea(0)
      elif answer3 == 'S':
                            Calculate_Areas3D.Sp_surfArea(0)
      elif answer3 == 'H':
                            Calculate_Areas3D.hemiSp_surfArea(0)
      elif answer3 == 'L': 
                            Calculate_Areas3D.pyramid_LSA(0)
      elif answer3 == 'T':
                            Calculate_Areas3D.pyramid_TSA(0)
      else :
           raise ValueError
 elif answer == 'P':
      print('''Hello \n 
      - For Tetrahedron area calculator ->> 'T' \n
      - For Hexahedron area calculator ->> 'H' \n
      - For Octahedron area calculator ->> 'O' \n
      - For Dodecahedron area calculator ->> 'D' \n
      - For Icosahedron area calculator ->> 'I' \n
      ''')
      answer4 = input('>> ').capitalize().strip()
      if answer4 == 'T': 
                          Calculate_Areas_Plat5.Tetrahedron(0)
      elif answer4 == 'H': 
                          Calculate_Areas_Plat5.hexahedron(0)
      elif answer4 == 'O':
                          Calculate_Areas_Plat5.Octahedron(0)
      elif answer4 == 'D':
                          Calculate_Areas_Plat5.Dodecahedron(0)
      elif answer4 == 'I':
                          Calculate_Areas_Plat5.Icosahedron(0)
      else :
            print('Error occured , try to enter a valid option')
 elif answer == 'Q':
      print('Closing...')
 else:
     raise ValueError


open_pro()

#Calculate_Areas2D.Cres_area(0,1)
