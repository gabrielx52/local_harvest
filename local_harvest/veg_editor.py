def veg_editor(file='data/short_veg_data.txt'):
    with open(file,'r') as infile:
        vegs = eval(infile.read())
    for veg in vegs:
        print(veg)

veg_editor()


