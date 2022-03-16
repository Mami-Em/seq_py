from cs50 import get_float, get_int

def jereo_rah_geom(zvtr):
    print('voahantso tsara!')

def main():
    val = get_int('how many letters do u have? ')
    
    if val < 3:
        print('tsy mety zao, kely lotra')
        exit()

    tab = []
    for i in range(val):
        tabs = get_float('alefa ary: ')
        tab.append(tabs)

    jereo_rah_geom(tab)

main()
