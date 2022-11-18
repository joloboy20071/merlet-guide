choise = ['snelheid', 'newton']
snelheid_ms = ['s = v x t', 'v = s X t', 't = v/s']
Newton = ['F = m x a', 'a = F/m', 'm = a/F']
listam =[]


dic = {
    's': 'm',
    'v': 'm/s',
    't': 's',
    'F': 'N',
    'a': 'm/s_2',
    'm': 'kg'
}

dic_2 ={
    'meter': 'de afstand in meter: \n',
    'tijd': 'de tijd in secondes: \n',
    'snelheid': 'de snelheid in meter per seconde: \n',
    'massa': 'de massa in kg: \n',
    'versnelling': 'de versnelling in m/s_2: \n ',
    'newton': 'kracht in newton: \n'
}

def devide(a, b, var1, var2):
    c = a/b
    d = '{}{} / {}{}'.format(a, var1, b ,var2)
    return c, d

def times(a, b, var1, var2):
    c = a*b
    d = '{}{} X {}{}'.format(a, var1, b ,var2)
    return c, d

h =1
for i in choise:
    print('{}:{}'.format(h, i))
    listam.append(str(h))
    h += 1


while True:
    g = 1
    selc = input('maak je reken keuze: \n')
    if selc in listam:
        num = int(selc)
        print('you selected: {}'.format(choise[num -1]))
        if choise[num -1] == 'snelheid':
            print('u heeft de keuze uit')
            for i in snelheid_ms:
                print('{}: {}'.format(g, snelheid_ms[g-1]))
                g +=1
            choise_2 = input('kies een van de bereken methodes:\n') 
            if choise_2 == '1':
                a = float(input(dic_2['meter'])) 
                b = float(input(dic_2['tijd']))
                c, d = times(a, b, dic['s'], dic['t'])
                print(d)
                print('= {} {}'.format(c,dic['v']))
            if choise_2 == '2':
                a = float(input(dic_2['snelheid'])) 
                b = float(input(dic_2['tijd']))
                c, d = devide(a, b ,dic['v'], dic['t'])
                print(d)
                print('= {} {}'.format(c,dic['v']))
            if choise_2 == '3':
                a = float(input(dic_2['meter'])) 
                b = float(input(dic_2['snelheid']))
                c, d = devide(a, b ,dic['s'], dic['v'])
                print(d)
                print('= {} {}'.format(c,dic['t']))
        if choise[num-1] == 'newton':
            print('u heeft de keuze uit')
            for i in Newton:
                print('{}: {}'.format(g, Newton[g-1]))
                g +=1
            choise_2 = input('kies een van de bereken methodes:\n')
            if choise_2 == '1':
                a = float(input(dic_2['massa'])) 
                b = float(input(dic_2['versnelling']))
                c, d = times(a, b, dic['m'], dic['a'])
                print(d)
                print('= {} {}'.format(c,dic['F']))
            if choise_2 == '2':
                a = float(input(dic_2['newton'])) 
                b = float(input(dic_2['massa']))
                c, d = devide(a, b ,dic['F'], dic['m'])
                print(d)
                print('= {} {}'.format(c,dic['a']))
            if choise_2 == '3':
                a = float(input(dic_2['versnelling'])) 
                b = float(input(dic_2['newton']))
                c, d = devide(a, b ,dic['a'], dic['F'])
                print(d)
                print('= {} {}'.format(c,dic['m']))
    else:
        print('not valid')