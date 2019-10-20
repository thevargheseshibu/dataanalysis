import pandas as pd
import datetime
import datetime as d
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

#Declaration Section

apdata = pd.read_csv('ApartmentData_March2019.csv')
ans = True

func_list = []
fname = []

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0

function_list = []

LoungeStay = 0
HallStay = 0
kitchenStay = 0
BathroomStay = 0
BedroomStay = 0
tvminutes = 0
lounminutes = 0
LounMMinutes = 0
Entryminutes = 0
hminutes = 0
kitchminutes = 0
kitchMMinutes = 0
bathminutes = 0
BathMMinutes = 0
BathDoorminutes = 0
bedlampminutes = 0
bedminutes = 0
BedMMinutes = 0

BedroomMotion = 0
BathroomMotion = 0
KitchenMotion = 0
LoungeMotion = 0

HotWaterKettleKitchenPower = 0
BedLampPower = 0
TVLoungePower = 0

BathroomIlluminance = 0
LoungeIlluminance = 0
BedroomIlluminance = 0
KitchenIlluminance = 0

Entry1Door = 0
BathroomDoor = 0

tempv = 0
count = 0
tcount = 0
fcount = 0
av = 0
bv = 0
oneweek = 0
twoweek = 0
twenty1days = 0
onemonth = 0
owcount = 0
twcount = 0
t1dcount = 0
omcount = 0

#Declaration Section

for i in range(0, (len(apdata)) - 1):
    fname.append(apdata["function_name"][i])

    def Remove(duplicate):
        for num in duplicate:
            if num not in func_list:
                func_list.append(num)


Remove(fname)

while ans:
    print("""
    1.VIEW THE MOVEMENT PATTERNS FOR THE ELDERLY PERSON 
    2.VIEW THE DURATION OF STAY IN EACH LOCATION
    3.VIEW THE USAGE OF AN APPLIANCE
    4.VIEW THE MOVEMENT INTO EACH ROOM
    5.VIEW THE POWER USAGE OF EACH ROOM
    6.VIEW THE COMPARISON OF LUMINOSITY OF EACH ROOM
    7.VIEW WHICH DOOR HAS BEEN USED THE MOST
    8.VIEW THE COMPARISON OF AIR TEMPERATURE FOR A WEEK,TWO WEEK , THREE WEEK AND A MONTH
    9.EXIT
    """)
    ans = input("What would you like to do? ")

    if ans == "1":
      

        bedlamp = datetime.timedelta()
        hwater = datetime.timedelta()
        bathillum = datetime.timedelta()
        bedillum = datetime.timedelta()
        lounillum = datetime.timedelta()
        kitchillum = datetime.timedelta()
        BedMotion = datetime.timedelta()
        BathMotion = datetime.timedelta()
        KitchMotion = datetime.timedelta()
        LounMotion = datetime.timedelta()
        EntryDoor = datetime.timedelta()
        battery = datetime.timedelta()
        BathDoor = datetime.timedelta()
        temp = datetime.timedelta()
        tv = datetime.timedelta()
        LoungeStay = 0
        HallStay = 0
        kitchenStay = 0
        BathroomStay = 0
        BedroomStay = 0
        tvminutes = 0
        lounminutes = 0
        LounMMinutes = 0
        Entryminutes = 0
        hminutes = 0
        kitchminutes = 0
        kitchMMinutes = 0
        bathminutes = 0
        BathMMinutes = 0
        BathDoorminutes = 0
        bedlampminutes = 0
        bedminutes = 0
        BedMMinutes = 0

        for i in range(0, (len(apdata)) - 1):
            if apdata["function_name"][i] == func_list[0]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                tv = tv + c
                tvminutes = tv.seconds / 60
                count1 = count1 + 1

            elif apdata["function_name"][i] == func_list[1]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                bedlamp = bedlamp + c
                bedlampminutes = bedlamp.seconds / 60
                count2 = count2 + 1

            elif apdata["function_name"][i] == func_list[2]:

                temp = datetime.timedelta()
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []
                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                hwater = hwater + c
                hminutes = hwater.seconds / 60
                count3 = count3 + 1

            elif apdata["function_name"][i] == func_list[3]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                bathillum = bathillum + c
                bathminutes = bathillum.seconds / 60
                count4 = count4 + 1

            elif apdata["function_name"][i] == func_list[4]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                temp = datetime.timedelta()
                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                bedillum = bedillum + c
                bedminutes = bedillum.seconds / 60
                count5 = count5 + 1

            elif apdata["function_name"][i] == func_list[5]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                lounillum = lounillum + c
                lounminutes = lounillum.seconds / 60
                count6 = count6 + 1

            elif apdata["function_name"][i] == func_list[6]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                kitchillum = kitchillum + c
                kitchminutes = kitchillum.seconds / 60
                count7 = count7 + 1

            elif apdata["function_name"][i] == func_list[7]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                BedMotion = BedMotion + c
                BedMMinutes = BedMotion.seconds / 60
                count8 = count8 + 1

            elif apdata["function_name"][i] == func_list[8]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a

                BathMotion = BathMotion + c
                BathMMinutes = BathMotion.seconds / 60
                count9 = count9 + 1

            elif apdata["function_name"][i] == func_list[9]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a

                KitchMotion = KitchMotion + c
                kitchMMinutes = KitchMotion.seconds / 60
                count10 = count10 + 1

            elif apdata["function_name"][i] == func_list[10]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a

                LounMotion = LounMotion + c
                LounMMinutes = LounMotion.seconds / 60
                count11 = count11 + 1

            elif apdata["function_name"][i] == func_list[11]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a

                EntryDoor = EntryDoor + c
                Entryminutes = EntryDoor.seconds / 60
                count12 = count12 + 1

            elif apdata["function_name"][i] == func_list[12]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a

                battery = battery + c
                batteryminutes = battery.seconds / 60
                count13 = count13 + 1

            elif apdata["function_name"][i] == func_list[13]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                BathDoor = BathDoor + c
                BathDoorminutes = BathDoor.seconds / 60
                count14 = count14 + 1

            elif apdata["function_name"][i] == func_list[14]:
                time = 0
                timecalen = []
                timecalennext = []
                h = []
                m = []
                s = []

                timecalen = apdata["timeOfData"][i].split(" ")
                timecalennext = apdata["timeOfData"][i + 1].split(" ")
                timeclok = str(timecalen[1])
                timeclok2 = str(timecalennext[1])
                timedate = str(timecalen[0])
                timedate2 = str(timecalennext[0])
                (a1, b1, c1) = timeclok.split(':')
                (a2, b2, c2) = timeclok2.split(':')
                (a3, b3, c3) = timedate.split('-')
                (a4, b4, c4) = timedate2.split('-')
                #print(timecalen[1])
                # print("b3",b3)
                a = datetime.datetime(int(a3), int(b3), int(float(c3)),
                                      int(a1), int(b1), int(float(c1)))

                b = datetime.datetime(int(a4), int(b4), int(float(c3)),
                                      int(a2), int(b2), int(float(c2)))

                c = b - a
                temp = temp + c
                tempminutes = temp.seconds / 60
                count15 = count15 + 1

        LoungeStay = tvminutes + lounminutes + LounMMinutes
        HallStay = Entryminutes
        kitchenStay = hminutes + kitchminutes + kitchMMinutes
        BathroomStay = bathminutes + BathMMinutes + BathDoorminutes
        BedroomStay = bedlampminutes + bedminutes + BedMMinutes

        #print(count1, count2, count3, count4, count5, count6, count7, count8,count9, count10, count11, count12, count13, count14, count15)
        #print('bedlamp', bedlamp)
        #print(BedMMinutes, BathMMinutes, kitchMMinutes, LounMMinutes,Entryminutes, batteryminutes, BathDoorminutes, tempminutes)

        names = [
            '1', '2', '3', '4', '5', '6', ' 7', '8', '9', '10', '11', '12',
            '13', '14', '15'
        ]

        values = [
            tvminutes, bedlampminutes, hminutes, bathminutes, bedminutes,
            lounminutes, kitchminutes, BedMMinutes, BathMMinutes,
            kitchMMinutes, LounMMinutes, Entryminutes, batteryminutes,
            BathDoorminutes, tempminutes
        ]

        plt.figure(figsize=(60, 260))
        plt.title(" FUNCTIONS USAGE ", bbox={'facecolor': '0.6', 'pad': 7})
        plt.figtext(
            .72, .45,
            "1-TV Lounge Power \n2-Bed Lamp Power \n3- Hot Water Kettle Kitchen Power \n4-Bathroom Illuminance \n5-Bedroom Illuminance \n7-Lounge Illuminance \n8-Kitchen Illuminance \n9-Bedroom Motion \n10-Bathroom Motion \n11-Kitchen Motion \n12-Lounge Motion \n13-Entry Door \n14-battery \n15-Bathroom Door \n16-temp "
        )
        plt.bar(names, values)
        plt.xlabel('Functions Done In A Month',fontsize=12,bbox={'facecolor': '0.8', 'pad': 5})
        plt.ylabel(
            'Total Time taken For The Functions For A Month In Minutes',fontsize=12,bbox={'facecolor': '0.8', 'pad': 5})

        plt.show()

    elif ans == "2":
        #print(LoungeStay)

        if (LoungeStay != 0 and HallStay != 0 and kitchenStay != 0
                and BathroomStay != 0 and BedroomStay != 0):

            #print("\n Room pie")

            LoungeStay = tvminutes + lounminutes + LounMMinutes
            HallStay = Entryminutes
            kitchenStay = hminutes + kitchminutes + kitchMMinutes
            BathroomStay = bathminutes + BathMMinutes + BathDoorminutes
            BedroomStay = bedlampminutes + bedminutes + BedMMinutes

            names = [
                'LOUNGE', 'HALL STAY', 'KITCHEN STAY', 'BATHROOM STAY', 'BEDROOM STAY'
            ]

            values = [
                LoungeStay, HallStay, kitchenStay, BathroomStay, BedroomStay
            ]

            cols = ['c', 'm', 'r', 'y', 'w']
            plt.figure(figsize=(60, 260))
            plt.pie(values,
                    labels=names,
                    colors=cols,
                    startangle=90,
                    shadow=True,
                    autopct='%1.1f%%')

            plt.title(" Total Stay In Each Room Comparison ", bbox={'facecolor': '0.8', 'pad': 5})
            
            plt.show()

        else:

            print("Please Execute Option Number 1 And Then Try Again !")

    elif ans == "3":
        
        plt.figure(figsize=(25, 20))
        #print(func_list[0])

        df = pd.DataFrame({
            'from': [
                "START", func_list[0], func_list[1], func_list[3],
                func_list[4], func_list[5], func_list[6], func_list[7],
                func_list[8], func_list[9], func_list[10], func_list[11],
                func_list[12], func_list[13], func_list[13]
            ],
            'to': [
                func_list[0], func_list[1], func_list[3], func_list[4],
                func_list[5], func_list[6], func_list[7], func_list[8],
                func_list[9], func_list[10], func_list[11], func_list[12],
                func_list[13], func_list[13], "END"
            ]
        })
        plt.title(" MOVEMENT PATH ", bbox={'facecolor': 'cyan', 'pad': 5})

        G = nx.from_pandas_edgelist(df, 'from', 'to')
        plt.figtext(.1, .1, "Flow From Goes From 'Start To 'End'" ,bbox={'facecolor': '0.8', 'pad': 5})
        # Plot it
        nx.draw(G, with_labels=True)

        plt.show()

    elif ans == "4":

        for i in range(0, (len(apdata)) - 1):
            if apdata["function_name"][i] == func_list[7] and apdata[
                    "function_type_name"][i] == "movement" and apdata["value"][
                        i] == 8:
                BedroomMotion = BedroomMotion + 1
            if apdata["function_name"][i] == func_list[8] and apdata[
                    "function_type_name"][i] == "movement" and apdata["value"][
                        i] == 8:
                BathroomMotion = BathroomMotion + 1
            if apdata["function_name"][i] == func_list[9] and apdata[
                    "function_type_name"][i] == "movement" and apdata["value"][
                        i] == 8:
                KitchenMotion = KitchenMotion + 1
            if apdata["function_name"][i] == func_list[10] and apdata[
                    "function_type_name"][i] == "movement" and apdata["value"][
                        i] == 8:
                LoungeMotion = LoungeMotion + 1
        #print(func_list[7], func_list[8], func_list[9], func_list[10])
        #print(BedroomMotion, BathroomMotion, KitchenMotion, LoungeMotion)
        names = [func_list[7], func_list[8], func_list[9], func_list[10]]

        values = [BedroomMotion, BathroomMotion, KitchenMotion, LoungeMotion]

        cols = ['g', 'r', 'm', 'w']
        plt.figure(figsize=(60, 260))
        plt.pie(values,
                labels=names,
                colors=cols,
                startangle=90,
                shadow=True,
                autopct='%1.1f%%')

        plt.title("Average Motion Detected in Each Room Sensor", bbox={'facecolor': 'cyan', 'pad': 5})


        plt.show()

    elif ans == "5":
        for i in range(0, (len(apdata)) - 1):
            fname.append(apdata["function_name"][i])

        for i in range(0, (len(apdata)) - 1):
            if apdata["function_name"][i] == func_list[0] and apdata[
                    "function_type_name"][i] == "power":
                TVLoungePower = TVLoungePower + float(apdata["value"][i])
            if apdata["function_name"][i] == func_list[1] and apdata[
                    "function_type_name"][i] == "power":
                BedLampPower = BedLampPower + float(apdata["value"][i])
            if apdata["function_name"][i] == func_list[2] and apdata[
                    "function_type_name"][i] == "power":
                HotWaterKettleKitchenPower = HotWaterKettleKitchenPower + float(
                    apdata["value"][i])
        #print(func_list[0], func_list[1], func_list[2])
        #print(TVLoungePower, BedLampPower, HotWaterKettleKitchenPower)
        names = [func_list[0], func_list[1], func_list[2]]

        values = [TVLoungePower, BedLampPower, HotWaterKettleKitchenPower]

        cols = ['g', 'r', 'm']
        plt.figure(figsize=(60, 260))
        plt.pie(values,
            labels=names,
            colors=cols,
            startangle=90,
            shadow=True,
            autopct='%1.1f%%')
        

        plt.title("Average Power Usage Comparison", bbox={'facecolor': 'cyan', 'pad': 5})
        
        plt.xlabel('Total Average Power Used By Appliances',fontsize=13,bbox={'facecolor': '0.5', 'pad': 5})

        plt.show()

    elif ans == "6":
        for i in range(0, (len(apdata)) - 1):
            fname.append(apdata["function_name"][i])

        for i in range(0, (len(apdata)) - 1):
            if apdata["function_name"][i] == func_list[3] and apdata[
                    "function_type_name"][i] == "illuminance":
                BathroomIlluminance = BathroomIlluminance + float(
                    apdata["value"][i])
            if apdata["function_name"][i] == func_list[4] and apdata[
                    "function_type_name"][i] == "illuminance":
                BedroomIlluminance = BedroomIlluminance + float(
                    apdata["value"][i])
            if apdata["function_name"][i] == func_list[5] and apdata[
                    "function_type_name"][i] == "illuminance":
                LoungeIlluminance = LoungeIlluminance + float(
                    apdata["value"][i])
            if apdata["function_name"][i] == func_list[6] and apdata[
                    "function_type_name"][i] == "illuminance":
                KitchenIlluminance = KitchenIlluminance + float(
                    apdata["value"][i])
        #print(func_list[3], func_list[4], func_list[5], func_list[6])
        #print(BathroomIlluminance, LoungeIlluminance, BedroomIlluminance,KitchenIlluminance)
        names = [func_list[3], func_list[4], func_list[5], func_list[6]]

        values = [
            BathroomIlluminance, LoungeIlluminance, BedroomIlluminance,
            KitchenIlluminance
        ]

        cols = ['g', 'r', 'm','b']
        plt.figure(figsize=(60, 260))
        plt.pie(values,
                labels=names,
                colors=cols,
                startangle=90,
                shadow=True,
                autopct='%1.1f%%')

        plt.title(" Average Illuminance ", bbox={'facecolor': 'Cyan', 'pad': 5})
        plt.xlabel('Total illuminance Percentage For Each Room', fontsize=12,bbox={'facecolor': '0.5', 'pad': 5})

        plt.show()

    elif ans == "7":

        for i in range(0, (len(apdata)) - 1):
            if apdata["function_name"][i] == func_list[11] and apdata[
                    "function_type_name"][i] == "door" and apdata["value"][
                        i] == 255:
                Entry1Door = Entry1Door + 1
            if apdata["function_name"][i] == func_list[13] and apdata[
                    "function_type_name"][i] == "door" and apdata["value"][
                        i] == 255:
                BathroomDoor = BathroomDoor + 1

        #print(func_list[11], func_list[13])
        #print(Entry1Door, BathroomDoor)

        names = [func_list[11], func_list[13]]

        values = [Entry1Door, BathroomDoor]

        cols = ['g', 'r', 'm', 'w']
        plt.figure(figsize=(60, 260))
        plt.bar(names, values)

        plt.title("DOOR USAGE", bbox={'facecolor': 'cyan', 'pad': 5})
        plt.xlabel('Type of Doors', fontsize=12,bbox={'facecolor': '0.5', 'pad': 5})
        plt.ylabel(
            'Total Number Of Times Used',fontsize=12,bbox={'facecolor': '0.5', 'pad': 5})

        plt.show()

    elif ans == "8":
        for i in range(0, (len(apdata)) - 1):
            if i <= (len(apdata)) - 1:
                timecalen = []
                timecalen = apdata["timeOfData"][i].split(" ")
                timedate = str(timecalen[0])
                (a3, b3, c3) = timedate.split('-')

                if (av == 0):
                    av = int(c3)
                if (av + 1 == int(c3)):
                    av = int(c3)
                    bv = bv + 1

                if apdata["id"][i] == "11202/5/power" and bv <= 30:
                    count = count + 1

                if apdata["function_name"][i] == "temp":
                    tempv = tempv + float(apdata["value"][i])
                    #print(apdata["value"][i])
                    tcount = tcount + 1
                #print(b)
                if (bv == 7):

                    oneweek = tempv
                    owcount = tcount
                if (bv == 14):

                    twoweek = tempv
                    twcount = tcount
                if (bv == 21):

                    twenty1days = tempv
                    t1dcount = tcount
                if (bv == 30):
                    #print("One Month passed")
                    onemonth = tempv
                    omcount = tcount

       # print(oneweek, twoweek, twenty1days, onemonth, owcount, twcount,t1dcount, omcount)
        oneweeka = oneweek / owcount
        twoweeka = twoweek / twcount
        twenty1daysa = twenty1days / t1dcount
        onemontha = onemonth / omcount

        names = ["One week", "Two Week", "Twenty One days", "One Month"]

        values = [oneweeka, twoweeka, twenty1daysa, onemontha]

        cols = ['g', 'r', 'm', 'w']
        plt.figure(figsize=(60, 260))
        plt.bar(names, values)

        plt.title("Air Temperature Average", bbox={'facecolor': 'cyan', 'pad': 5})
        plt.xlabel('Average of Temperature', fontsize=12,bbox={'facecolor': '0.5', 'pad': 5})
        plt.ylabel(
            'Average In Weeks & Month',fontsize=12,bbox={'facecolor': '0.5', 'pad': 5})
        
        plt.show()

        plt.pie(values,
            labels=names,
            colors=cols,
            startangle=90,
            shadow=True,
            autopct='%1.1f%%')
        plt.title("Air Temperature Average In Percent", bbox={'facecolor': 'cyan', 'pad': 5})
        plt.show()

    elif ans == "9":
        print("\n Goodbye. Thank You For Using !")
        ans = False

    elif ans != "":
        print("\n Not Valid Choice Try again")
