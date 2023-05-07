import random
print("                   Добро пожаловать в крестики-нолики")
gamealreade = True
gamealreade1 = False
print("""
                        ИНСТРУКЦИЯ К ИГРЕ
                Чтобы поставить крести, нужно слитно
          написать две цифры, первая будет отвечать за строчку,
                    вторая будет отвечать за столбик""")
while gamealreade == True:
    try:
        z = int(input("Введите цифру 1 чтобы начать игру первым, 2 если хотите ходить вторым, 3 чтобы закрыть игру "))
    except ValueError:
        print("Введите хотя бы цифру, видите же какие цифры для чего нужно ввести")
        continue
    if z == 3:
        gamealreade = False
    if z == 1:
        gamealreade1 = True
        compstat = ['00','01','02','10','11','12','20','21','22',]
        a = [['-' for x in range(3)] for y in range(3)]
        while gamealreade1 == True:
            print('  0','1','2')
            print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
            print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
            print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
            player = str(input())
            try: 
                compstat.remove(str(player))
            except ValueError:
                print("Недопустимое значение(")
                continue
            a[int(player)//10][int(player)%10] = "x"
            if str(a[0][0]) + str(a[0][1]) + str(a[0][2]) == 'xxx' or\
            str(a[1][0]) + str(a[1][1]) + str(a[1][2]) == 'xxx' or\
            str(a[2][0]) + str(a[2][1]) + str(a[2][2]) == 'xxx' or\
            str(a[0][0]) + str(a[1][0]) + str(a[2][0]) == 'xxx' or\
            str(a[0][1]) + str(a[1][1]) + str(a[2][1]) == 'xxx' or\
            str(a[0][2]) + str(a[1][2]) + str(a[2][2]) == 'xxx' or\
            str(a[0][0]) + str(a[1][1]) + str(a[2][2]) == 'xxx' or\
            str(a[2][0]) + str(a[1][1]) + str(a[0][2]) == 'xxx':
                print('  0','1','2')
                print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
                print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
                print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
                print('Вы победили!')
                print("""УРА!!!
        ⠄⠄⠄⠄⠄⠄⠄⣀⣤⣤⣄⡀⢀⣠⣤⣤⣀⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⢀⣾⢫⣵⠶⠉⢿⡟⠉⠄⠈⠙⣧⡀⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⢸⡇⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⣹⡇⠄⠄⠄⠄⠄
        ⢠⡾⢛⡛⢷⡾⣷⡙⠁⠄⠄⠄⠄⠄⠄⠄⢀⡿⢷⡾⢛⡛⢷⡄
        ⣿⢰⡟⠁⠄⠁⠘⢿⣄⡀⠄⠄⠄⠄⢀⣴⡟⠁⠈⠄⠈⢻⡆⣿
        ⢹⣦⠁⠄⠄⠄⠄⠄⣹⡿⣦⣄⣠⡴⢿⣅⠄⠄⠄⠄⠄⠈⣴⡏
        ⠄⠙⢷⣤⡀⠄⣠⣶⠟⠁⢰⣿⣿⡄⠈⠻⣶⣄⠄⢀⣤⡾⠋⠄
        ⠄⠄⠄⢉⣿⣿⣏⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⣹⣿⣿⡉⠄⠄⠄
        ⠄⠄⠄⠈⠉⡏⠉⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⠉⢹⠉⠁⠄⠄⠄
        ⠄⠄⠄⠄⠄⣿⠄⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⠄⣿⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠹⣧⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⣼⠏⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠙⠃⠄⠄⠄⠘⠃⠄⠄⠄⠘⠋⠄⠄⠄⠄⠄⠄""")
                gamealreade1 = False
                break
            try:
                comp = str(random.choice(compstat))
                compstat.remove(str(comp))
                a[int(comp)//10][int(comp)%10] = "o"
                if str(a[0][0]) + str(a[0][1]) + str(a[0][2]) == 'ooo' or\
                str(a[1][0]) + str(a[1][1]) + str(a[1][2]) == 'ooo' or\
                str(a[2][0]) + str(a[2][1]) + str(a[2][2]) == 'ooo' or\
                str(a[0][0]) + str(a[1][0]) + str(a[2][0]) == 'ooo' or\
                str(a[0][1]) + str(a[1][1]) + str(a[2][1]) == 'ooo' or\
                str(a[0][2]) + str(a[1][2]) + str(a[2][2]) == 'ooo' or\
                str(a[0][0]) + str(a[1][1]) + str(a[2][2]) == 'ooo' or\
                str(a[2][0]) + str(a[1][1]) + str(a[0][2]) == 'ooo':
                    print('  0','1','2')
                    print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
                    print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
                    print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
                    print("Вы проиграли(")
                    print("""
        ⣿⡇⣰⣶⣶⣭⠻⣏⠁⠄⠄⣠⠟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⡇⣿⡀⠄⢹⣧⣿⠄⠄⣴⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠟⢿⣝⠷⣶⡾⣿⡟⢀⡾⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣀⡀⠉⠛⠶⢟⣫⡴⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠛⠛⠛⠛⠛⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⠆⠄⠄⠄⠄⠄⠄⠄⠄
        ⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⡀⠄⠄⠄⠈⠻⠿⠇⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣧⠄⠄⠄⠄⠄⣴⠾⠛⢻⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⠄⠄⠄⠄⣠⣴⣶⠿⠗⠒⠄⠄⠄⠄⠄
        ⣿⣿⣿⣾⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣷⣿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣿⣿⣷⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣿⣿⣿⣝⣶⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
""")
                    gamealreade1 = False
                    break
            except IndexError:
                print('  0','1','2')
                print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
                print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
                print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
                print('Ничья!')
                gamealreade1 = False                
    if z == 2:
        gamealreade1 = True
        compstat = ['00','01','02','10','11','12','20','21','22',]
        a = [['-' for x in range(3)] for y in range(3)]
        comp = str(random.choice(compstat))
        compstat.remove(str(comp))
        a[int(comp)//10][int(comp)%10] = "o"
        while gamealreade1 == True:
            if compstat == []:
                print('  0','1','2')
                print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
                print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
                print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
                print('Ничья(')
                gamealreade1 = False
                break
                
            print('  0','1','2')
            print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
            print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
            print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
            try:
                if str(a[0][0]) + str(a[0][1]) + str(a[0][2]) == 'ooo' or\
                str(a[1][0]) + str(a[1][1]) + str(a[1][2]) == 'ooo' or\
                str(a[2][0]) + str(a[2][1]) + str(a[2][2]) == 'ooo' or\
                str(a[0][0]) + str(a[1][0]) + str(a[2][0]) == 'ooo' or\
                str(a[0][1]) + str(a[1][1]) + str(a[2][1]) == 'ooo' or\
                str(a[0][2]) + str(a[1][2]) + str(a[2][2]) == 'ooo' or\
                str(a[0][0]) + str(a[1][1]) + str(a[2][2]) == 'ooo' or\
                str(a[2][0]) + str(a[1][1]) + str(a[0][2]) == 'ooo':
                    print("Вы проиграли(")
                    print("""
        ⣿⡇⣰⣶⣶⣭⠻⣏⠁⠄⠄⣠⠟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⡇⣿⡀⠄⢹⣧⣿⠄⠄⣴⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠟⢿⣝⠷⣶⡾⣿⡟⢀⡾⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣀⡀⠉⠛⠶⢟⣫⡴⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠛⠛⠛⠛⠛⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⠆⠄⠄⠄⠄⠄⠄⠄⠄
        ⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⡀⠄⠄⠄⠈⠻⠿⠇⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣧⠄⠄⠄⠄⠄⣴⠾⠛⢻⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⠄⠄⠄⠄⣠⣴⣶⠿⠗⠒⠄⠄⠄⠄⠄
        ⣿⣿⣿⣾⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣷⣿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣿⣿⣷⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣿⣿⣿⣝⣶⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
""")
                    gamealreade1 = False
                    break
            except IndexError:
                print('  0','1','2')
                print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
                print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
                print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
                print('Ничья!')
                gamealreade1 = False
            player = str(input())
            try: 
                compstat.remove(str(player))
            except ValueError:
                print("Недопустимое значение(")
                continue
            a[int(player)//10][int(player)%10] = "x"
            if str(a[0][0]) + str(a[0][1]) + str(a[0][2]) == 'xxx' or\
            str(a[1][0]) + str(a[1][1]) + str(a[1][2]) == 'xxx' or\
            str(a[2][0]) + str(a[2][1]) + str(a[2][2]) == 'xxx' or\
            str(a[0][0]) + str(a[1][0]) + str(a[2][0]) == 'xxx' or\
            str(a[0][1]) + str(a[1][1]) + str(a[2][1]) == 'xxx' or\
            str(a[0][2]) + str(a[1][2]) + str(a[2][2]) == 'xxx' or\
            str(a[0][0]) + str(a[1][1]) + str(a[2][2]) == 'xxx' or\
            str(a[2][0]) + str(a[1][1]) + str(a[0][2]) == 'xxx':
                print('  0','1','2')
                print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
                print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
                print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
                print('Вы победили!')
                print("""УРА!!!
        ⠄⠄⠄⠄⠄⠄⠄⣀⣤⣤⣄⡀⢀⣠⣤⣤⣀⠄⠄⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⢀⣾⢫⣵⠶⠉⢿⡟⠉⠄⠈⠙⣧⡀⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⢸⡇⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⣹⡇⠄⠄⠄⠄⠄
        ⢠⡾⢛⡛⢷⡾⣷⡙⠁⠄⠄⠄⠄⠄⠄⠄⢀⡿⢷⡾⢛⡛⢷⡄
        ⣿⢰⡟⠁⠄⠁⠘⢿⣄⡀⠄⠄⠄⠄⢀⣴⡟⠁⠈⠄⠈⢻⡆⣿
        ⢹⣦⠁⠄⠄⠄⠄⠄⣹⡿⣦⣄⣠⡴⢿⣅⠄⠄⠄⠄⠄⠈⣴⡏
        ⠄⠙⢷⣤⡀⠄⣠⣶⠟⠁⢰⣿⣿⡄⠈⠻⣶⣄⠄⢀⣤⡾⠋⠄
        ⠄⠄⠄⢉⣿⣿⣏⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⣹⣿⣿⡉⠄⠄⠄
        ⠄⠄⠄⠈⠉⡏⠉⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⠉⢹⠉⠁⠄⠄⠄
        ⠄⠄⠄⠄⠄⣿⠄⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⠄⣿⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠹⣧⠄⠄⠄⠄⢸⡇⠄⠄⠄⠄⣼⠏⠄⠄⠄⠄⠄
        ⠄⠄⠄⠄⠄⠄⠙⠃⠄⠄⠄⠘⠃⠄⠄⠄⠘⠋⠄⠄⠄⠄⠄⠄""")
                gamealreade1 = False
                break
            try:
                comp = str(random.choice(compstat))
                compstat.remove(str(comp))
                a[int(comp)//10][int(comp)%10] = "o"
                if str(a[0][0]) + str(a[0][1]) + str(a[0][2]) == 'ooo' or\
                str(a[1][0]) + str(a[1][1]) + str(a[1][2]) == 'ooo' or\
                str(a[2][0]) + str(a[2][1]) + str(a[2][2]) == 'ooo' or\
                str(a[0][0]) + str(a[1][0]) + str(a[2][0]) == 'ooo' or\
                str(a[0][1]) + str(a[1][1]) + str(a[2][1]) == 'ooo' or\
                str(a[0][2]) + str(a[1][2]) + str(a[2][2]) == 'ooo' or\
                str(a[0][0]) + str(a[1][1]) + str(a[2][2]) == 'ooo' or\
                str(a[2][0]) + str(a[1][1]) + str(a[0][2]) == 'ooo':
                    print('  0','1','2')
                    print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
                    print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
                    print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
                    print("Вы проиграли(")
                    print("""
        ⣿⡇⣰⣶⣶⣭⠻⣏⠁⠄⠄⣠⠟⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⡇⣿⡀⠄⢹⣧⣿⠄⠄⣴⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠟⢿⣝⠷⣶⡾⣿⡟⢀⡾⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣀⡀⠉⠛⠶⢟⣫⡴⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⠛⠛⠛⠛⠛⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣴⠆⠄⠄⠄⠄⠄⠄⠄⠄
        ⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⡀⠄⠄⠄⠈⠻⠿⠇⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣧⠄⠄⠄⠄⠄⣴⠾⠛⢻⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣧⠄⠄⠄⠄⠄⠄⠄⠄⠻⣿⣿⠄⠄⠄⠄⣠⣴⣶⠿⠗⠒⠄⠄⠄⠄⠄
        ⣿⣿⣿⣾⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣷⣿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣿⣿⣷⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
        ⣿⣿⣿⣿⣿⣿⣝⣶⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
""")
                    gamealreade1 = False
                    break
            except IndexError:
                print('  0','1','2')
                print('0 ' + str(a[0][0]), str(a[0][1]), str(a[0][2]))
                print('1 ' + str(a[1][0]), str(a[1][1]), str(a[1][2]))
                print("2 " + str(a[2][0]), str(a[2][1]), str(a[2][2]))
                print('Ничья!')
                gamealreade1 = False
    
                
        
