alien_0 = {}

alien_0["color"] = "green"
alien_0["points"] = 5
alien_0["x_position"] = 0

key_name = "y_position"
alien_0[key_name] = 25

print(alien_0)

val = alien_0.get("ID","No ID is specified")
print(val)

val = alien_0.get("ID")
print(val)