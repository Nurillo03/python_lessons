# son=1
# while son<=5:
#     print(son,end=' ')
#     son+=1
# print('Dastur tugadi.')

# print('Kritilgan sonning kvadratini qaytaradigan dastur.')
# savol='Istalgan sonni kiriting.'
# savol+="Dastur tugashini hohlasangiz 'exit' deb yozing"
# # qiymat=''
# # while qiymat!='exit':
# #     qiymat=input(savol)
# #     if qiymat!='exit':
# #         print(float(qiymat)**2)
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi.')

# son=0
# while son<10:
#     son+=1
#     if (son%2)!=0:
#         continue
#     else: print(son)
# kitoblar=[]
# while True:
#     kitob=input("O'zingiz yoqtirgan kitob nomini kiriting:(stop so'zini yozishi bilan dasturni to'xtating) ")
#     if kitob=='stop':
#         break
#     else:
#         kitoblar.append(kitob.capitalize())
# print('\nSiz yoqtirgan kitoblar quidagilar: ',end='')
# print(', '.join(kitoblar))



# while True:
#     yosh=input('Yoshingizni kiriting: ')
#     if yosh=='exit':
#         break
#     yosh=int(yosh)
#     if yosh<=7:
#         print('Chipta narxingiz 2000 som. ')
#     elif yosh<=18:
#         print('Chipta narxingiz 3000 som. ')
#     elif yosh<=65:
#         print('Chipta narxingiz 10000 som. ')
#     elif yosh>65:
#         print('Chipta narxingiz tekin. ')
# print("Dastur tugadi.")

# ishora=True
# while ishora:
#     yosh=input('Yoshingizni kiriting: ')
#     if yosh=='exit':
#         ishora=False
#         continue
#     yosh=int(yosh)
#     if yosh<=7:
#         print('Chipta narxingiz 2000 som. ')
#     elif yosh<=18:
#         print('Chipta narxingiz 3000 som. ')
#     elif yosh<=65:
#         print('Chipta narxingiz 10000 som. ')
#     elif yosh>65:
#         print('Chipta narxingiz tekin. ')
# print("Dastur tugadi.")

# ishora=True
# while ishora:
#     yosh=input('Yoshingizni kiriting: ')
#     if yosh=='exit':
#         ishora=False
#     else:
#         yosh=int(yosh)
#         if yosh<=7:
#             print('Chipta narxingiz 2000 som. ')
#         elif yosh<=18:
#             print('Chipta narxingiz 3000 som. ')
#         elif yosh<=65:
#             print('Chipta narxingiz 10000 som. ')
#         elif yosh>65:
#             print('Chipta narxingiz tekin. ')
# print("Dastur tugadi.")

# ishora=True
# while ishora:
#     yosh=input('Yoshingizni kiriting: ')
#     if yosh=='exit':
#         ishora=False
#     else:
#         yosh=int(yosh)
#         if yosh<=7:
#             narh=3000
#         elif yosh<=18:
#             narh=5000
#         elif yosh<=65:
#             narh=10000
#         else:
#             narh=0
#         if narh==0:
#             print('Kirish tekin.')
#         else:
#             print(f"Chipta narhingiz {narh} so'm. ")
# print("Dastur tugadi.")


# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
# print("Dastur tugadi. ")

# mevalar=[]
# n=1
# while True:
#     meva=input(f"{n}-meva nomini kiriting: ")
#     mevalar.append(meva.title())
#     takrorlash=input("Davom etishni hohlaysizmi? (ha/yoq)")
#     n+=1
#     if takrorlash=='yoq':
#         break
# print("Siz quidagi mevalarni kiritdingiz: ",', '.join(mevalar))

# mevalar={}
# n=1
# javob=1
# while javob:
#     meva=input(f"{n}-meva nomini kiriting: ").title()
#     narh=int(input('Narhini kiriting: '))
#     mevalar[meva]=narh
    
#     javob=int(input("yana meva kiritingni hohlyasizmi? ha(1),yoq(0) "))
#     n+=1
# for k,v in mevalar.items():
#     print(f'\n{k}ning narhi {v} so\'m.')

# sonlar=[1,2,3,4,1,1,1,5]
# print(sonlar)
# numbers=set(sonlar)
# print(numbers)
# while 1 in sonlar:
#     sonlar.remove(1)
# print(sonlar)


# talabalar=['ali','vali','hasan','husan']
# baholangan_talabalar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba.title()}ning bahosini kiriting: ")
#     baholangan_talabalar[talaba]=int(baho)
# print('')
# for k,v in baholangan_talabalar.items():
#     print(f"{k.title()}ning bahosi {v}.")


# buyurtmalar=[]
# while True:
#     buyurtma=input('Nima buyurtma qilishni hohlaysiz? ')
#     buyurtmalar.append(buyurtma)
#     javob=input('Yana nimadir buyurtma qilishni hohlaysizmi?'
#                 '(ha/yoq)')
#     if javob=='yoq':
#         break
# print()
# print("Siz quidagilarni buyurtma qildingiz:",', '.join(buyurtmalar)+'.')


# mahsulotlar={}
# ishora=True
# while ishora:
#     mahsulot=input("Mahsulot kiriting: ").title()
#     narh=int(input(f'{mahsulot}ning narhini kiriting: '))
#     mahsulotlar[mahsulot]=narh
    
#     javob=input('Davom ettirasizmi? (ha/yoq)')
#     if javob=='yoq':
#         ishora=False
# print()
# print('Quidagi mahsulotlarni kiritdingiz: ')
# for m,n in mahsulotlar.items():
#     print(f"{m} {n} mln so'm.")

mevalar={'olma':10000,'nok':12000,'banan':5000}
buyurtmalar=['olma','nok','olxo\'ri']

# for buyurtma in buyurtmalar:
#     if buyurtma in mevalar:
#         print(f'{buyurtma.title()}ning narhi {mevalar[buyurtma]} so\'m')
#     else:
#         print(f'Bizda {buyurtma} mavjud emas.')

while buyurtmalar:
    buyurtma=buyurtmalar.pop(0)
    if buyurtma in mevalar.keys():
        print(mevalar[buyurtma])
    else:
        print("Bizda bunday mahsulot ajvud emas.")

































