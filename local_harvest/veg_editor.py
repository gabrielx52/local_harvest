def veg_param_editor(veggies='data/veg_data.txt'):
    with open(veggies, 'r+') as infile:
        vegs = eval(infile.read())
        for veg in vegs:
            for item in vegs[veg]:
                print(veg, ":", item, "=", vegs[veg][item] )
                new_value = input(">")
                if new_value:
                    vegs[veg][item] = new_value






veg_param_editor()