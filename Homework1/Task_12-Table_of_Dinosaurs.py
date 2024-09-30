dino1 = 'Tyrannosaurus Rex'
length_dino1 = 12.0
weight_dino1 = 9.000

dino2 = 'Velociraptor'
length_dino2 = 1.8
weight_dino2 = 0.015

dino3 = 'Triceratops'
length_dino3 = 9.0
weight_dino3 = 6.800

dino4 = 'Stegosaurus'
length_dino4 = 9.0
weight_dino4 = 5.500

dino5 = 'Brachiosaurus'
length_dino5 = 30.0
weight_dino5 = 56.000


f_header = f"|{'Dinosaur':<22}|{'Length' :^12}|{'Weight (tones)':^15}|"
f_devider = f'{"-"*52}'
f_dino1 = f"|{dino1:<22}|{length_dino1:^12}|{weight_dino1:>15.3f}|"
f_dino2 = f"|{dino2:<22}|{length_dino2:^12}|{weight_dino2:>15.3f}|"
f_dino3 = f"|{dino3:<22}|{length_dino3:^12}|{weight_dino3:>15.3f}|"
f_dino4 = f"|{dino4:<22}|{length_dino4:^12}|{weight_dino4:>15.3f}|"
f_dino5 = f"|{dino5:<22}|{length_dino5:^12}|{weight_dino5:>15.3f}|"


print(f_header)
print(f_devider)
print(f_dino1)
print(f_dino2)
print(f_dino3)
print(f_dino4)
print(f_dino5)