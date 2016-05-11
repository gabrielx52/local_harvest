def veg_editor(file='../data/short_veg_data.txt'):
    with open(file) as infile:
        vegs = eval(infile.read())
    veg_list = sorted([veg for veg in vegs])
    split = int(len(veg_list) / 3)
    l1 = veg_list[0:split]
    l2 = veg_list[split:split * 2]
    l3 = veg_list[split * 2:]
    for row_1, row_2, row_3 in zip(l1, l2, l3):
        print("{0:<20s} {1:<20s} {2}".format(row_1, row_2, row_3))
    vegg = input('\nVeg>> ').title()
    print('\n')
    if vegg in vegs:
        for i in vegs[vegg]:
            print('{} = {}'.format(i, vegs[vegg][i]))
    while True:
        ed_li_qu = input('\n(E)dit/(L)ist/(Q)uit\nE/Q/L>> ').title()
        if ed_li_qu == 'E':
            for i in vegs[vegg]:
                print('{} = {}'.format(i, vegs[vegg][i]))
            param_ed = input('Attr>> ').title()
            new_param = input('New value>> ').title()
            if param_ed in vegs[vegg]:
                vegs[vegg][param_ed] = new_param
                print('\n')
                print(vegg)
                for i in vegs[vegg]:
                    print('{} = {}'.format(i, vegs[vegg][i]))
                with open(file, 'w') as outfile:
                    outfile.write(str(vegs))
        elif ed_li_qu == 'L':
            veg_editor()
        else:
            break


veg_editor()
