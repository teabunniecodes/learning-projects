guest_list = ["Michelle Kwan", "Kristi Yamguchi", "Midori Ito"]

for guests in guest_list:
    print(f"Please join me for dinner, {guests}")

guest_list.append("Scott Hamilton")
print(guest_list)

guest_list.insert(1, "Nancy Kerrigan")
print(guest_list)

guest_list.remove("Midori Ito")
print(guest_list)

guest_list.sort()
print("Here is the sorted guest list")
print(guest_list)