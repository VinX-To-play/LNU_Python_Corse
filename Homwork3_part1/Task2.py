import random
import matplotlib.pyplot as plt
import numpy as np

dice_sum = [0]*11

print("Frequency table (sum, count) for rolling two dice 10000 times")
for i in range(1000):
    curent_throw = random.randint(1,6) + random.randint(1,6)
    match curent_throw:
        case 2: dice_sum[0] += 1
        case 3: dice_sum[1] += 1
        case 4: dice_sum[2] += 1
        case 5: dice_sum[3] += 1
        case 6: dice_sum[4] += 1
        case 7: dice_sum[5] += 1
        case 8: dice_sum[6] += 1
        case 9: dice_sum[7] += 1
        case 10: dice_sum[8] += 1
        case 11: dice_sum[9] += 1
        case 12: dice_sum[10] += 1
    
for i in range(11):
    print(f"{(2+i):<8} {dice_sum[i]}")

fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dice_sum)  # Plot some data on the Axes.
plt.show()   
    