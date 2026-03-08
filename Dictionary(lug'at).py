cars={'model':'nexia','rang':'qizil'}
# print(cars['model'])
# print(cars['rang'])

mevalar={'olma':10000,'nok':12000,'banan':5000}
# print(f"Bananning narxi {mevalar['banan']} so'm.")

talaba_0={'ism':'murod','yosh':22,'t_yil':2003}
talaba_0['kurs']=4
talaba_0['fakultet']='ingliz tili'
talaba_0['ism']='ali'
# print(talaba_0)

eng_uz={}
eng_uz['apple']='olma'
eng_uz['school']='maktab'
eng_uz['book']='kitob'
# print(eng_uz)
del eng_uz['apple']
# print(eng_uz)

kinolar={
    'qorqinchli':'IT',
    'sarguzasht':'Karib dengizi qaroqchilari',
    'tarixiy':'Troya'}
# print(kinolar)

telefonlar={}
telefonlar['anvar']='redmi'
telefonlar['husniddin']='iphone'
# print(telefon)
phone_1=telefonlar['anvar']
phone_0=telefonlar.get('akrom','Bunday telefon mavjud emas.')
# print(phone_1)
# print(phone_0)

dostim={
        'ism':'abbos',
        'yosh':22,
        't_yil':2003}
# print(f"Do'stimning ismi {dostim['ism'].title()}, yoshi {dostim['yosh']} da,"
      # f" {dostim['t_yil']}-yilda tug'ilgan.")

sevimli_taomlar={'onam':'manti',
                 'ukam':'somsa',
                 'singlim':'shorva',
                 'enam':'chuchvara',
                 'ozim':'lagmon'}
# print(f"Onamning sevimli taomi {sevimli_taomlar['onam']}.")
# print(f"Ukamning sevimli taomi {sevimli_taomlar['ukam']}.")
# print(f"Singlimning sevimli taomi {sevimli_taomlar['singlim']}.")

python={'integer':'butun son',
        'string':'matn',
        'float':'onli son',
        'list':'royxat',
        'tuple':'ozgarmas royxat',
        'dictionary':'lugat',
        'set':'oxshash qiymatlarni takrorlamaydigan royxat'}
# for k,q in sorted(python.items()):
    # print(f"{k}-{q}.")

sonlar1=[1,2,3,2]
sonlar2={1,2,3,2}
sonlar1.append(4)
sonlar2.add(4)
sonlar2.update([5,6,7,4])

# print(sonlar1)
# print(sonlar2)

shaxs1={'ism':'Alisher Navoiy',
        't_yil':'1441-yil',
        'tugilgan joyi':'Hirot(hozirgi Afgoniston)',
        'asarlar soni':'30 ta'}
shaxs2={'ism':'Abdulla Qodiriy',
        't_yil':'1894-yil',
        'tugilgan joyi':'Toshkent shahri',
        'asarlar soni':'3 ta'}
shaxs3={'ism':'Tomas Harris',
        't_yil':'1940-yil',
        'tugilgan joyi':'AQSH)',
        'asarlar soni':'6 ta'}
shaxs4={'ism':'Agata Kristi',
        't_yil':'1890-yil',
        'tugilgan joyi':'Angliya',
        'asarlar soni':'100 dan ortiq'}
shaxslar=[shaxs1,shaxs2,shaxs3,shaxs4]

# for s in shaxslar:
#     for k,q in s.items():
#         if k=='asarlar soni':
#             print(k.title()+':',q,'\n')
#         else:
#             print(k.title()+':',q) 


shaxs1['vafot etgan yili']='1501-yil'
shaxs2['vafot etgan yili']='1938-yil'
shaxs3['vafot etgan yili']='hali tirik'
shaxs4['vafot etgan yili']='1976-yil'            

# for sh in shaxslar:
#     print(f"{sh['ism']} {sh['vafot etgan yili']}da vafot etgan.")


sevimli_kinolar={'Abbos':['gerakl','troya'],
                 'Nodir':['LOTR','Hobbit'],
                 'Abror':['Cannibal','Breaking Bad']}
# for ka,qi in sevimli_kinolar.items():
#     print(ka+':',', '.join([kino.title() for kino in qi]))

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

# davlat=input('Qaysi davlat haqida malumot olishni hohlaysiz?\n>>> ').lower()
# if davlat in davlatlar:
#     info=davlatlar[davlat]
#     print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}.\n"
#           f"Maydoni {info['maydon']} km kvadrat.\n"
#           f"Aholisi {info['aholi']} kishi.\n"
#           f"Pul birligi {info['pul birligi']}.")
# else:
#     print('Kechirasiz, bu davlat haqida malumot mavjud emas.')



n='   men n hafrini yozdim  '.strip('   m')
print(n)
print(len(n))









































































