# Задание 1

 #from math import sqrt
# day = int(input('Input the number of the day :'))
# while day < 1 or day > 7:
#     day= int (input('Error! THERE IS ONLY 7 DAYS IN A WEEK! PLEASE TRY AGAIN!!'))
# if day == 6 or day == 7:
#         print('is WEEKEND')
# else:
#             print('is NOT WEEKEND')

# Задание 2
# x = int(input(' Enter X :'))
# y = int(input('Enter Y :'))
# z = int(input('Enter Z :'))
# if not (x or y or z) == (not x) and (not y) and (not z):
#     print('True')
# else:
#     print('False')

# Задание 5

# from math import sqrt


# xA = float(input('Enter the X  coordinate for point A: '))
# yA = float(input('Enter the Y  coordinate for point A: '))
# xB = float(input('Enter the X  coordinate for point B: '))
# yB = float(input('Enter the Y  coordinate for point B: '))

# result = sqrt (((xB-xA)**2 + (yB-yA)**2))
# print(round(result, 3))

# задание 3

# X = float(input('Input X coordinates: '))
# Y = float(input('Input Y coordinates: '))
# while X==0 and Y==0:
#     print('Error! Coordinate must be bigger than 0')
#     X = float(input('Input X coordinates: '))
#     Y = float(input('Input Y coordinates: '))
# if X > 0 and Y > 0:
#     print('first quarter')
# elif X < 0 and Y>0:
#     print('second quarter')
# elif X<0 and Y<0:
#     print('third quarter')
# else:
#     print('fourth quarter')

# Задание 4 

qrtar= int(input('Input quarter: '))
while qrtar < 1 or qrtar > 4:
    qrtar= int(input('Error!! Input correct quarter: '))
if qrtar == 1:
    print('X > 0 - (+∞); Y > 0 - (+∞)')
elif qrtar == 2:
    print('X < 0 - (-∞); Y > 0 - (+∞)')
elif qrtar == 3:
    print('X < 0 - (-∞); Y < 0 - (-∞)')
else:
    print (('X>0 -(+∞); Y < 0 - (-∞)'))

