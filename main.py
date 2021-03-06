from pyfiglet import figlet_format
from termcolor2 import colored


# ============= labels =============
name = figlet_format("Tool App")
print(colored(name,"red"))

by = "By: Mohammad Shokouhian"
print(colored(by,"green",attrs=["bold","underline"]))

# ============= if =============

a = 0
while a < 1:
    coloredMagenta = lambda x:colored(x,"magenta")
    print(coloredMagenta("[1] Caculator"))
    print(coloredMagenta("[2] Time tool"))
    print(coloredMagenta("[3] Wikipedia Search"))
    print(coloredMagenta("[4] Rock-Scissor-Paper"))
    print(coloredMagenta("[5] Guess Number"))
    print(coloredMagenta("[6] Text to Speech"))
    print(coloredMagenta("[7] Shut down"))
    print(coloredMagenta("[8] Backgroud Changer"))
    print(coloredMagenta("[0] Quit"))
    firstQ = input(">>> What would you like to do: ")
    
    if firstQ == "1":
        
        while True:
         from math import sqrt,tan
         print(colored("For calculate tangent of x enter "))
         inp = input("Calculator >>>")  
        
         try:
            if inp == "0": break
            if inp == "": continue
         except:
            print(colored("ٍError!","red","on_white",attrs=["bold"]))

    elif firstQ == "2":
        import time 
        from jdatetime import JalaliToGregorian
        import datetime as dt
        # import termcolor2

        print(colored("Time Tool","yellow"))


        todayMiladi = time.localtime()
        year = todayMiladi[0]
        month = todayMiladi[1]
        day = todayMiladi[2]
        hour = todayMiladi[3]
        minute = todayMiladi[4]
        second = todayMiladi[5]
        dayOfWeek = todayMiladi[6]
        dayOfYear = todayMiladi[7]

        # ============= functions(time) =============

        def animalshamsi(year):
            trueYear = year - 7
            animal = {0 : "<Mouse>", 1 : "<Cow>", 2 : "<Tiger>", 3 : "<Rabbit>", 4 : "<Dragon>", 5 : "<Snake>", 6 : "<Hourse>", 7 : "<Goat>", 8 : "<Monkey>", 9;}
            if trueYear % 12 == 0:
                print(colored("your birth year is : <Mouse>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 1:
                print(colored("your birth year is : <Cow>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 2:
                print(colored("your birth year is : <Tiger>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 3:
                print(colored("your birth year is : <Rabbit>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 4:
                print(colored("your birth year is : <Dragon>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 5:
                print(colored("your birth year is : <Snake>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 6:
                print(colored("your birth year is : <Houre>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 7:
                print(colored("your birth year is : <Goat>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 8:
                print(colored("your birth year is : <Monkey>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 9:
                print(colored("your birth year is : <Rooster>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 10:
                print(colored("your birth year is : <Dog>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 11:
                print(colored("your birth year is : <Pig>","green"))
                print(colored("================","red"))

        def animalmiladi(year):
            trueYear = year - 4
            if trueYear % 12 == 0:
                print(colored("your birth year is : <Mouse>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 1:
                print(colored("your birth year is : <Cow>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 2:
                print(colored("your birth year is : <Tiger>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 3:
                print(colored("your birth year is : <Rabbit>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 4:
                print(colored("your birth year is : <Dragon>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 5:
                print(colored("your birth year is : <Snake>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 6:
                print(colored("your birth year is : <Houre>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 7:
                print(colored("your birth year is : <Goat>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 8:
                print(colored("your birth year is : <Monkey>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 9:
                print(colored("your birth year is : <Rooster>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 10:
                print(colored("your birth year is : <Dog>","green"))
                print(colored("================","red"))
            elif trueYear % 12 == 11:
                print(colored("your birth year is : <Pig>","green"))
                print(colored("================","red"))

        def todayMiladifunc():
            print(colored("Gregorian date:","yellow"))
            print(colored(f"{year}/{month}/{day}","green"))
            print(colored(f"{hour} : {minute} : {second}","blue"))
            print(colored(f"{dayOfYear} days from {year}","green"))

        def gLeapYear(y):
            if (y%4==0) and ((y%100!=0) or (y%400==0)):
                return True
            else: 
                return False

        def sLeapYear(y):
            ary = [1, 5, 9, 13, 17, 22, 26, 30]
            result = False
            b = y%33
            if b in ary: 
                result = True
            return result

        def todayShamsifunc(gyear, gmonth, gday):
            _gl = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
            _g  = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            
            deydiffjan = 10
            if gLeapYear(gyear-1):  
                deydiffjan = 11
            if gLeapYear(gyear):  
                gd = _gl[gmonth-1]+gday
            else: 
                gd = _g[gmonth-1]+gday
            
            if gd>79:
                sy = gyear - 621
                gd = gd - 79
                if gd<=186:
                    gmod = gd%31
                    if gmod==0:
                        sd = 31
                        sm = int(gd/31)
                    else:
                        sd = gmod
                        sm = int(gd/31) + 1
                else:
                    gd = gd - 186
                    gmod = gd%30
                    if gmod==0:
                        sd = 30
                        sm = int(gd/30) + 6
                    else:
                        sd = gmod
                        sm = int(gd/30) + 7
            else:
                sy = gyear - 622
                gd = gd+deydiffjan
                gmod = gd%30
                if gmod==0:
                    sd = 30
                    sm = int(gd/30) + 9 
                else:
                    sd = gmod 
                    sm = int(gd/30) + 10 
            # result = [sy, sm, sd]
            # return result
            print(colored("today is:","yellow"))
            if dayOfWeek == 0:
                print(colored("Monday","blue"))
            elif dayOfWeek == 1:
                print(colored("Tuesday","blue"))
            elif dayOfWeek == 2:
                print(colored("Wednesday","blue"))
            elif dayOfWeek == 3:
                print(colored("Thursday","blue"))
            elif dayOfWeek == 4:
                print(colored("Friday","blue"))
            elif dayOfWeek == 5:
                print(colored("Saturday","blue"))
            elif dayOfWeek == 6:
                print(colored("Sunday","blue"))
            print(colored("Shamsi date:","yellow"))
            print(colored(f"{sd}/{sm}/{sy}","green"))

        def miladiToShamsi(gyear, gmonth, gday):
            _gl = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
            _g  = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            
            deydiffjan = 10
            if gLeapYear(gyear-1):  
                deydiffjan = 11
            if gLeapYear(gyear):  
                gd = _gl[gmonth-1]+gday
            else: 
                gd = _g[gmonth-1]+gday
            
            if gd>79:
                sy = gyear - 621
                gd = gd - 79
                if gd<=186:
                    gmod = gd%31
                    if gmod==0:
                        sd = 31
                        sm = int(gd/31)
                    else:
                        sd = gmod
                        sm = int(gd/31) + 1
                else:
                    gd = gd - 186
                    gmod = gd%30
                    if gmod==0:
                        sd = 30
                        sm = int(gd/30) + 6
                    else:
                        sd = gmod
                        sm = int(gd/30) + 7
            else:
                sy = gyear - 622
                gd = gd+deydiffjan
                gmod = gd%30
                if gmod==0:
                    sd = 30
                    sm = int(gd/30) + 9 
                else:
                    sd = gmod
                    sm = int(gd/30) + 10 
            # result = [sy, sm, sd]
            # return result
            print(colored(f"Result:\n{sd}/{sm}/{sy}","green"))

        def shamsiToMiladi(gyear, gmonth, gday):
            gregorian_date_obj = JalaliToGregorian(gyear,gmonth,gday)
            gregorian_date =gregorian_date_obj.getGregorianList()
            d = gregorian_date[0]
            m = gregorian_date[1]
            y = gregorian_date[2]
            print(colored("
Result:","green"))
            print(colored(f"{d}/{m}/{y}","green"))
            print(colored("==============
","red"))


        def daysOfLifeMiladi():
            year2 = int(input("
Year of birth: "))
            month2 = int(input("Month of birth: "))
            day2 = int(input("Day of birth: "))
            year_born =  dt.date(year2,month2,day2)
            input_year = f"{year}.{month}.{day}"
            syear = dt.datetime.strptime(input_year, "%Y.%m.%d")
            days_life = (syear.date()- year_born).days
            if days_life <= 0:
                print('You were not born on this date.')
            else:
                print(colored('
It's been {} days from birthday!
'.format(days_life),"green"))

        def daysOfLifeShamsi(gyear,gmonth,gday):
            _gl = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
            _g  = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            
            deydiffjan = 10
            if gLeapYear(gyear-1):  
                deydiffjan = 11
            if gLeapYear(gyear):  
                gd = _gl[gmonth-1] + gday
            else: 
                gd = _g[gmonth-1] + gday
            
            if gd>79:
                sy = gyear - 621
                gd = gd - 79
                if gd<=186:
                    gmod = gd%31
                    if gmod == 0:
                        sd = 31
                        sm = int(gd/31)
                    else:
                        sd = gmod
                        sm = int(gd/31) + 1
                else:
                    gd = gd - 186
                    gmod = gd%30
                    if gmod==0:
                        sd = 30
                        sm = int(gd/30) + 6
                    else:
                        sd = gmod
                        sm = int(gd/30) + 7
            else:
                sy = gyear - 622
                gd = gd+deydiffjan
                gmod = gd%30
                if gmod==0:
                    sd = 30
                    sm = int(gd/30) + 9 
                else:
                    sd = gmod
                    sm = int(gd/30) + 10
            year2 = int(input("
Year of birth: "))
            month2 = int(input("Month of birth: "))
            day2 = int(input("Day of birth: "))
            year_born =  dt.date(year2,month2,day2)
            input_year = f"{sy}.{sm}.{sd}"
            syear = dt.datetime.strptime(input_year, "%Y.%m.%d")
            days_life = (syear.date()- year_born).days
            if days_life <= 0:
                print('You were not born on this date.')
            else:
                print(colored('
It's been {} days from birthday!'.format(days_life),"green"))
                print(colored("==============
","red"))

        # ============= inputs and texts(time) =============

        print(colored("[1] Animal of birth (Miladi)"))
        print(colored("[2] Animal of birth (Shamsi)"))
        print(colored("[3] Today"))
        print(colored("[4] Miladi to Shamsi"))
        print(colored("[5] Shamsi to Miladi"))
        print(colored("[6] Days of life (Miladi)"))
        print(colored("[7] Days of life (Shamsi)"))
        work = input(">>> what do you want to do? ")

        # ============= if(time) =============

        if work == "1":
            try:
                animalmiladi(int(input("
>>> Enter your year of birth: ")))
            except:
                print("Error!")
        elif work == "2":
            try:
                animalshamsi(int(input("
>>> Enter your year of birth: ")))
            except:
                print("Error!")
        elif work == "3":
            try:
                todayShamsifunc(year,month,day)
                todayMiladifunc()
            except:
                print("Error!")
        elif work == "4":
            try:
                y1 = int(input("
>>> year: "))
                m1 = int(input(">>> month: "))
                d1 = int(input(">>> day: "))
                miladiToShamsi(y1,m1,d1)
            except:
                print("Error!")
        elif work == "5":
            try:
                y2 = int(input("
>>> year: "))
                m2 = int(input(">>> month: "))
                d2 = int(input(">>> day: "))
                shamsiToMiladi(y2,m2,d2)
            except:
                print("Error!")
        elif work == "6":
            try:
                daysOfLifeMiladi()
            except:
                print("Error!")
        elif work == "7":
            try:
                daysOfLifeShamsi(year,month,day)
            except:
                print("Error!")
        else:
            print("You should enter number of each parameter!")
    elif firstQ == "3":
        import wikipedia

        print(colored("
Wikipedia","yellow"))

        # ============= functions =============
        def searchEn():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("en")
            print(wikipedia.summary(searchText))

        def searchFa():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("fa")
            print(wikipedia.summary(searchText))

        def searchAr():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("ar")
            print(wikipedia.summary(searchText))

        def searchFr():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("fr")
            print(wikipedia.summary(searchText))

        def searchGe():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("de")
            print(wikipedia.summary(searchText))

        def searchCh():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("zh")
            print(wikipedia.summary(searchText))
            
        def searchRe():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("ru")
            print(wikipedia.summary(searchText))

        def searchEs():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("es")
            print(wikipedia.summary(searchText))

        # ============= inputs and texts =============

        print("[1] English")
        print("[2] Persian")
        print("[3] Arabic")
        print("[4] French")
        print("[5] German")
        print("[6] Chinese")
        print("[7] Russian")
        print("[8] Spanish")
        searchLang = input(">>> Enter language of your search: ")

        # ============= if =============

        if searchLang == "1":
            try:
                searchEn()
            except:
                print("Error!")
        elif searchLang == "2":
            try:
                searchFa()
            except:
                print("Error!")
        elif searchLang == "3":
            try:
                searchAr()
            except:
                print("Error!")
        elif searchLang == "4":
            try:
                searchFr()
            except:
                print("Error!")
        elif searchLang == "5":
            try:
                searchGe()
            except:
                print("Error!")
        elif searchLang == "6":
            try:
                searchCh()
            except:
                print("Error!")
        elif searchLang == "7":
            try:
                searchRe()
            except:
                print("Error!")
        elif searchLang == "8":
            try:
                searchEs()
            except:
                print("Error!")
    elif firstQ == "4":
        import random

        # ============== first input ==============

        print(colored("

Rock Scissor Paper","yellow"))
        OneTwo = "
[1] Computer 
[2] Player 2
"
        print(colored(OneTwo))
        b = 0
        try:
            while b < 1:
                first_input = input(">>> Choose your player rival: ") 
                if first_input == "2":
                    print(colored("
2 Player","yellow"))

                    player_name1 = input("
>>> Player1! What is your name? ")
                    player_name2 = input("
>>> Player2! What is your name? ")
                    playerScore1 = 0
                    playerScore2 = 0

                    e = 0
                    try:
                        while e < 1:
                            c = 0
                            while c < 1:
                                print(colored("
[1] Rock
[2] Scissor
[3] Paper
[0] Back"))
                                playerMove1 = input(f">>> {player_name1}! Choose: ")
                                if playerMove1 == "1":
                                    playerMove1 = "rock".lower()
                                    c += 1
                                    print(colored("==========
","red","on_white"))
                                elif playerMove1 == "2":
                                    playerMove1 = "scissor".lower()
                                    c += 1
                                    print(colored("==========
","red","on_white"))
                                elif playerMove1 == "3":
                                    playerMove1 = "paper".lower()
                                    c += 1
                                    print(colored("==========
","red","on_white"))
                                elif playerMove1 == "0":
                                    playerMove1 = "0"
                                    c += 1
                                    e += 1
                                else:
                                        print(colored("ٍError!","red","on_white",attrs=["bold"]))
                                        print(colored("==========================
","red","on_white"))
                            f = 0
                            while f < 1:
                                print(colored("
[1] Rock
[2] Scissor
[3] Paper
[0] Back"))
                                playerMove2 = input(f">>> {player_name2}! Choose: ")
                                if playerMove2 == "1":
                                    playerMove2 = "rock".lower()
                                    f += 1
                                    print(colored("==========
","red","on_white"))
                                elif playerMove2 == "2":
                                    playerMove2 = "scissor".lower()
                                    f += 1
                                    print(colored("==========
","red","on_white"))
                                elif playerMove2 == "3":
                                    playerMove2 = "paper".lower()
                                    f += 1
                                    print(colored("==========
","red","on_white"))
                                elif playerMove2 == "0":
                                    playerMove2 = "0"
                                    f += 1
                                    e += 1
                                else:
                                    print(colored("ٍError!","red","on_white",attrs=["bold"]))
                                    print(colored("==========================
","red","on_white"))
                            if playerMove1 == playerMove2:
                                print(colored("Draw!","green"))
                                print(colored("===========","red"))
                                print(colored(f"{player_name1}: {playerScore1}","yellow"))
                                print(colored(f"{player_name2}: {playerScore2}","yellow"))
                                print(colored("==========================
","red","on_white"))
                                c -= 1
                                f -= 1
                            elif playerMove1 == "rock":
                                if playerMove2 == "scissor":
                                    print(colored(f"Winner: {player_name1}","green"))
                                    playerScore1 += 1
                                    print(colored(f"===========","red"))
                                    print(colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(colored("==========================
","red","on_white"))
                                    
                                elif playerMove2 == "paper":
                                    print(colored(f"Winner: {player_name2}","green"))
                                    playerScore2 += 1
                                    print(colored(f"===========","red"))
                                    print(colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(colored("==========================
","red","on_white"))
                                c -= 1
                                f -= 1    
                            elif playerMove1 == "scissor":
                                if playerMove2 == "paper":
                                    print(colored(f"Winner: {player_name1}","green"))
                                    playerScore1 += 1
                                    print(colored("===========","red"))
                                    print(colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(colored("==========================
","red","on_white"))
                    
                                elif playerMove2 == "rock":
                                    print(colored(f"Winner: {player_name2}","green"))
                                    playerScore2 += 1
                                    print(colored("===========","red"))
                                    print(colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(colored("==========================
","red","on_white"))
                                c -= 1
                                f -= 1     
                            elif playerMove1 == "paper":
                                if playerMove2 == "rock":
                                    print(colored(f"Winner: {player_name1}","green"))
                                    playerScore1 += 1
                                    print(colored("===========","red"))
                                    print(colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(colored("==========================
","red","on_white"))
                                    
                                elif playerMove2 == "scissor":
                                    print(colored(f"Winner: {player_name2}","green"))
                                    playerScore2 += 1
                                    print(colored("===========","red"))
                                    print(colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(colored("==========================
","red","on_white"))
                                c -= 1
                                f -= 1    
                    except:
                        print(colored("ٍError!","red","on_white",attrs=["bold"]))
                    b += 1
                elif first_input == "1":
                    b += 1
                else:
                    print(colored("Try again!","red","on_white"))
        except:
            pass

        if first_input == "1":
            player_name = input("
>>> What is your name? ")
            computerScore = 0
            playerScore = 0

            p = 0
            try:
                while p < 1:
                    computerMove = random.randint(1,3)
                    if computerMove == 1:
                        computerMove = "rock"
                    elif computerMove == 2:
                        computerMove = "paper"
                    elif computerMove == 3:
                        computerMove = "scissor"
                    d = 0
                    while d < 1:
                        print(colored("
[1] Rock
[2] Scissor
[3] Paper
[0] Back"))
                        playerMove1 = input(">>> Choose: ")
                        if playerMove1 == "1":
                            playerMove = "rock".lower()
                            d += 1
                        elif playerMove1 == "2":
                            playerMove = "scissor".lower()
                            d += 1
                        elif playerMove1 == "3":
                            playerMove = "paper".lower()
                            d += 1
                        elif playerMove1 == "0":
                            playerMove = "0"
                            d += 1
                        else:
                            print(colored("ٍError!","red","on_white",attrs=["bold"]))
                            print(colored("==========================","red","on_white"))
                            
                    if computerMove == playerMove:
                        print(colored(f"Computer move: {computerMove}","blue"))
                        print(colored("Draw!","green"))
                        print(colored("===========","red"))
                        print(colored(f"Player score: {playerScore}","yellow"))
                        print(colored(f"Computer score: {computerScore}","yellow"))
                        print(colored("==========================","red","on_white"))
                    
                    elif playerMove == "rock":
                        if computerMove == "paper":
                            print(colored(f"Computer move: {computerMove}","blue"))
                            print(colored(f"Winner: Computer","green"))
                            computerScore+=1
                            print(colored("===========","red"))
                            print(colored(f"Player score: {playerScore}","yellow"))
                            print(colored(f"Computer score: {computerScore}","yellow"))
                            print(colored("==========================","red","on_white"))
                        elif computerMove == "scissor":
                            print(colored(f"Computer move: {computerMove}","blue"))
                            print(colored(f"Winner: {player_name}","green"))
                            playerScore+=1
                            print(colored("===========","red"))
                            print(colored(f"Player score: {playerScore}","yellow"))
                            print(colored(f"Computer score: {computerScore}","yellow"))
                            print(colored("==========================","red","on_white"))

                    elif playerMove == "scissor":
                        if computerMove == "paper":
                            print(colored(f"
Computer move: {computerMove}","blue"))
                            print(colored(f"Winner: Computer","green"))
                            playerScore+=1
                            print(colored("===========","red"))
                            print(colored(f"Player score: {playerScore}","yellow"))
                            print(colored(f"Computer score: {computerScore}","yellow"))
                            print(colored("==========================","red","on_white"))
                        elif computerMove == "rock":
                            print(colored(f"Computer move: {computerMove}","blue"))
                            print(colored(f"Winner: {player_name}","green"))
                            computerScore+=1
                            print(colored("===========","red"))
                            print(colored(f"Player score: {playerScore}","yellow"))
                            print(colored(f"Computer score: {computerScore}","yellow"))
                            print(colored("==========================","red","on_white"))

                    elif playerMove == "paper":
                        if computerMove == "rock":
                            print(colored(f"Computer move: {computerMove}","blue"))
                            print(colored(f"Winner: Computer","green"))
                            playerScore+=1
                            print(colored("===========","red"))
                            print(colored(f"Player score: {playerScore}","yellow"))
                            print(colored(f"Computer score: {computerScore}","yellow"))
                            print(colored("==========================","red","on_white"))
                        elif computerMove == "scissor":
                            print(colored(f"Computer move: {computerMove}","blue"))
                            print(colored(f"Winner: {player_name}","green"))
                            computerScore+=1
                            print(colored("===========","red"))
                            print(colored(f"Player score: {playerScore}","yellow"))
                            print(colored(f"Computer score: {computerScore}","yellow"))
                            print(colored("==========================","red","on_white"))
                    elif playerMove == "0":
                        p += 1
                    else:
                        print(colored("ٍError!","red","on_white",attrs=["bold"]))
                        print(colored("==========================","red","on_white"))
            except:
                print(colored("ٍError!","red","on_white",attrs=["bold"]))
    elif firstQ == "5":
        import random

        print(colored("Guess number","yellow"))

        a = 0 
        while a < 1:
            b = 0
            while b < 1:
                try:
                    distanceS = int(input(">>> From what number start: "))
                except:
                    print(colored("Try again!","red","on_white"))
                else:
                    b += 1
            c = 0
            while c < 1:
                try:
                    distanceF = int(input(">>> Till what number finish: "))
                except:
                    print(colored("Try again!","red","on_white"))
                else:
                    c += 1
            if distanceF < distanceS:
                computerNum = random.randint(distanceF,distanceS)
            else:
                computerNum = random.randint(distanceS,distanceF)
            d = 0
            while d < 1:
                try:
                    print(colored("[Start number - 1] Quit","magenta"))
                    guess = int(input(">>> Enter your guess: "))
                except:
                    print(colored("Try again!","red","on_white"))
                else:
                    if guess == computerNum:
                            print(colored(f"Well done! your number was: {computerNum}","green"))
                            print(colored("===============","red"))
                            d += 1
                    elif guess == (distanceS - 1):
                            d += 1
                            a += 1
                    elif guess < computerNum:
                            print(colored(f"It is higher than {guess}","blue"))
                            print(colored("===============","red"))
                    elif guess > computerNum:
                            print(colored(f"It is lower than {guess}","blue"))
                            print(colored("===============","red"))
            if guess != (distanceS - 1):
                f = 0
                while f < 1:
                    exit = input(">>> DO you want to exit?y/n: ")
                    if exit == "y":
                            f += 1
                            a += 1
                    elif exit == "n":
                            f += 1
                    else:
                            print(colored("Try again!","red","on_white"))

        a = 0;b = 0;c = 0;d = 0;f = 0
    elif firstQ == "6":
        from text_to_speech import speak

        print(colored("Text to Speech","yellow"))
        # ============== functions ==============

        def searchEn():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="en", slow=True, save=True, file=r"Desktopilename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="en", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchJa():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="ja", slow=True, save=True, file=r"Desktopilename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="ja", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchAr():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="ar", slow=True, save=True, file=r"Desktopilename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="ar", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchFr():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="fr", slow=True, save=True, file=r"Desktopilename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="fr", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchGe():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="de", slow=True, save=True, file=r"Desktopilename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="de", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchCh():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="zh", slow=True, save=True, file=r"Desktopilename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="zh", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchRe():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="ru", slow=True, save=True, file=r"Desktopilename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="ru", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchEs():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="es", slow=True, save=True, file=r"Desktopilename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="es", slow=True)
                    w += 1
                else:
                    pass

        # ============= inputs and texts =============

        print(colored("[1] English","magenta"))
        print(colored("[2] Japanese","magenta"))
        print(colored("[3] Arabic","magenta"))
        print(colored("[4] French","magenta"))
        print(colored("[5] German","magenta"))
        print(colored("[6] Chinese","magenta"))
        print(colored("[7] Russian","magenta"))
        print(colored("[8] Spanish","magenta"))
        searchLang = input(">>> Enter language of your search: ")

        # ============= if =============

        if searchLang == "1":
            try:
                searchEn()
            except:
                print("Error!")
        elif searchLang == "2":
            try:
                searchJa()
            except:
                print("Error!")
        elif searchLang == "3":
            try:
                searchAr()
            except:
                print("Error!")
        elif searchLang == "4":
            try:
                searchFr()
            except:
                print("Error!")
        elif searchLang == "5":
            try:
                searchGe()
            except:
                print("Error!")
        elif searchLang == "6":
            try:
                searchCh()
            except:
                print("Error!")
        elif searchLang == "7":
            try:
                searchRe()
            except:
                print("Error!")
        elif searchLang == "8":
            try:
                searchEs()
            except:
                print("Error!")
    elif firstQ == "7":
        import os

        print(colored("Shut Down","yellow"))

        try:
            a = 0
            while a < 1:
                b = 0
                print(colored("[1] Shut Down","magenta"))
                print(colored("[2] Restart","magenta"))
                print(colored("[0] Quit","magenta"))
                while b < 1:
                    firstInput = input(">>> Choose: ")
                    if firstInput == "1":
                        os.system('shutdown -s')
                        b += 1
                    elif firstInput == "2":
                        os.system('shutdown -r')
                        b += 1
                    elif firstInput == "0":
                        b += 1
                        a += 1
                    else:
                        print(colored("Try again","red","on_white"))
        except:
            print(colored("Error","red","on_white"))
    elif firstQ == "8":
        import ctypes
        print(colored("

Background Changer","yellow"))
        def change_wallpaper():
            try:
                n = 0
                while n < 1:
                    address = input(">>> Enter address of your image: ")
                    value = ctypes.windll.user32.SystemParametersInfoW(20,0,address)
                    print(colored("Background Changed!","blue"))
                    print(colored("[1] Change again","magenta"))
                    print(colored("[0] Quit","magenta"))
                    m = 0
                    while m < 1:
                        secondInput = input(">>> Choose: ")
                        if secondInput == "1":
                            m += 1
                        elif secondInput == "0":
                            m += 1
                            n += 1
                        else:
                            print(colored("ٍError!","red","on_white",attrs=["bold"]))
                n -= 1
                m -= 1
            except:
                print(colored("ٍError!","red","on_white",attrs=["bold"]))
        change_wallpaper()
    elif firstQ == "0":
        a += 1
