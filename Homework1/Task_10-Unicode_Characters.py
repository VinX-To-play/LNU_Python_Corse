import random
output = ""
 
print('Random characters from the Runes category:')
 
for i in range(5):
    output = output + ' ' + (chr(random.randint(int(0x16A0),int(0x16FF))))

print(output)