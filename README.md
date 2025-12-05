# Codedex-classes

import math 

print ( '==================\nArea Calculator 📐\n==================')



print( ' 1) Triangle\n 2) Rectangle\n 3) Square\n 4) Circle\n 5) Quit\n')




shape = int(input('Which shape: '))
if shape == 4: 
  radius = int(input('Radius: '))
elif shape== 5:
  print('Quit')
else:
  base = int(input('Base: '))
  height = int(input('Height: '))



if shape == 4:
  area_4 = math.pi * radius 
  print('The area of the circle is', area_4)
elif shape == 3:
  area_3 = base * height 
  print('The area of the square is', area_3) 
elif shape == 2:
  area_2 = base * height 
  print('The area of the rectangle is', area_2 ) 
elif shape == 1:
  area_1 = (base * height)/2 
  print('The area of the rectangle is', area_1)
