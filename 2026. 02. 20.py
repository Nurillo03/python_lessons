cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car!='gm': 
#         print(car.title())
#     else: 
#         print(car.upper())
# for i in range(len(cars)):
#     if cars[i]!='gm':
#         cars[i]=cars[i].title()
#     else:
#         cars[i]=cars[i].upper()
# cars=[car.title() if car!='gm' else car.upper() for car in cars]

# ism=input('Iltimos ismingizni kiriting: ')
# if ism.lower()=='admin':
#     print('Xush kelibsiz,',ism.title()+'. Foydalanuvchilar royxatini korishni hohlaysizmi? ')
# else:
#     print(ism.title(),', xush kelibsiz.')

# print('Iltmos ixtiyoriy 2 ta son kiriting.')
# son1=int(input('1-son: '))
# son2=int(input('2-son: '))
# # if son1==son2: print('Sonlar teng.')
# # else: print('Sonlar teng emas.')
# javob='Sonlar teng' if son1==son2 else 'Sonlar teng emas'
# print(javob)

# son=float(input('Istalgan sonni kiriting: '))
# # j='musbat son' if son>0 else ('manfiy son' if son<0 else 'nol')
# j=('katta musbat' if son>100 else
#    'musbat' if son>0 else
#    'manfiy' if son<0 else
#    'nol')
# print(j)

# x=float(input('Brorta son kiriting: '))
# print(f"{x} ni kvadrat ildizi {x**0.5} ga teng" if x>0 else 'Musbat son kiriting.')
# if x>0: print(f"{x} ni kvadrat ildizi {x**0.5} ga teng")
# else: print('Musbat son kiriting.')

# son=float(input('Iltimos juft son kiriting: '))
# if son%2==0:
#     print('rahmat')
# else:
#     print('bu juft son emas.')

# yosh=float(input('Iltimos yoshingizni kiriting: '))
# if yosh<=4: narh=0
# elif yosh>=60: narh=0
# elif yosh>=18: narh=20000
# else: narh=10000
# print(f"chipta narxi {narh} som")

# print('iltimos 2 ta son kiriting: ')
# son1=float(input("1-son: "))
# son2=float(input("2-son: "))
# if son1==son2: print(son1,'va',son2,'teng.')
# elif son1<son2: print(son1,son2,'dan  kichik.')
# else: print(son1,son2,'dan  katta.')

# mahsulotlar=['olma','anor','piyoz','kartoshka','un',
#              'moy','shokolad','tuz','gosht','kalbasa']
# print('dokonimizdan nima sotvolishni hohlaysiz? ')
# buyurtmalar=[]
# borlari=[]
# yoqlari=[]
# for i in range(1,6):
#     buyurtmalar.append(input(f"{i}-mahsulotni kiriting:"))
# print()
# for buyurtma in buyurtmalar:
#     if buyurtma in mahsulotlar: 
#         print(f"{buyurtma} dokonimizda mavjud.") 
#         borlari.append(buyurtma)
    
#     if buyurtma not in mahsulotlar: 
#         print(f"kechirasiz {buyurtma} dokonimizda hozirda mavjud emas") 
#         yoqlari.append(buyurtma)
# print('borlari:',', '.join(borlari))
# print('yoqlari:',', '.join(yoqlari))

# try:
#     son=int(input('butun son kiriting: '))
#     q=[]
#     for i in range(2,11):
#         if son%i==0:
#             q.append(i)
#     if q:
#         print(son,'2 dan 10 gacha bo\'lgan sonlar ichida',' va '.join([str(x) for x in q]),'sonlariga qoldiqsiz bo\'linadi.') 
#     else:
#         print(son,'2 dan 10 gacha bo\'lgan sonlar ichida hech qaysi songa qoldiqsiz b\'linmaydi')
# except ValueError:
#     print("❗ Iltimos, faqat butun son kiriting.")

# son = int(input("Istalgan butun son kiriting: "))

# for n in range(2,11):
#     if not son%n:
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")



















































































