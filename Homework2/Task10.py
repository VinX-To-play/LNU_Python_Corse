import time_converter

user_ss = int(input("Number of seconds: "))
time = time_converter.sek_to_time(user_ss)

print(f"{user_ss} seconds correspond to {time[0]} hour(s), {time[1]} minute(s) and {time[2]} second(s)\n")

user_hh = int(input("Number of hours: "))
user_mm = int(input("Number of minutes: "))
user_ss = int(input("Number of seconds: "))
print(f"{user_hh} hour(s), {user_mm} minute(s) and {user_ss} second(s) correspond to {time_converter.time_to_sek(user_hh, user_mm, user_ss)} seconds.")
