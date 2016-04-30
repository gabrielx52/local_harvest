def veg_param_editor(veggies='data/veg_data.txt'):
    with open(veggies, 'r+') as infile:
        vegs = eval(infile.read())
        for veg in vegs:
            edit = input('Edit: {}? Y/N '.format(veg))
            if edit.lower() == 'y':
                for attr in vegs[veg]:
                    attr_edit = input('{} = {}, Edit? Y/N '.format(attr, vegs[veg][attr]))
                    if attr_edit.lower() == 'y':
                        new_attr = input('New value for {} {}: '.format(veg, attr))
                        vegs[veg][attr] = new_attr
                        print(veg, attr, '= ', vegs[veg][attr])

                    else:
                        pass
            else:
                pass
        with open('data/veg_data_edit.txt', 'w') as f:
            f.write(str(vegs))

veg_param_editor()
