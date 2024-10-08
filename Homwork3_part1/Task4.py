import listfunc as lf

og_list = [8, 8, 4, 1, 9, 10, 6, 9, 2, 9]

print("Original list of numbers:", og_list)

filterd = lf.filter_even(og_list)

print("Filterd even numbers:", filterd)
print("Sum of even numbers:", lf.sum_of_list(filterd))

og_names = ['luke', 'leia', 'han', 'chewbacca']

print("Original list of names:", og_names)
print("Capitalized names:", lf.capitalise_names(og_names))

print("Original list is strictly increasing?", lf.is_strictly_increasing(og_list))
incricing_list = [1,2,3,4,5,6,7,8,9,10]
print(f"Incresing list ({incricing_list}) increasing? {lf.is_strictly_increasing(incricing_list)}")
print("Unique numbers in original list:",og_list)