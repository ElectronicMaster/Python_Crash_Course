guest_list = []

guest_list.append("jishnu")
guest_list.append("Hima")
guest_list.append("Thiru")

print(f"welcomes you for dinner {guest_list[0]}")
print(f"welcomes you for dinner {guest_list[1]}")
print(f"welcomes you for dinner {guest_list[2]}")

guest_list[1] = "srivatsa"

print(guest_list)

guest_list.insert(0,"Gokul")
guest_list.insert(2,"guruprasad")
guest_list.append("hima")

temp = guest_list.copy()

print(guest_list)

print(f"I am sorry you are rejected {guest_list.pop()}")
print(f"I am sorry you are rejected {guest_list.pop()}")
print(f"I am sorry you are rejected {guest_list.pop()}")
print(f"I am sorry you are rejected {guest_list.pop()}")

print(guest_list)

del guest_list[0]
del guest_list[0]

print(guest_list)

guest_list = temp.copy()
print()
print(sorted(guest_list))
guest_list.reverse()
print(guest_list)
guest_list.reverse()
guest_list.sort()
print(guest_list)
guest_list.sort(reverse=True)
print(guest_list)

print(len(guest_list))