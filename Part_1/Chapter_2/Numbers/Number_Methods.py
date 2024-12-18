universe_age = 14_000_000_000
print(universe_age)

x,y,z = 10,20,30
print(f"x: {x}, y: {y}, z: {z}")

MAX_CONST = 1000
# MAX_CONST = 2000 # Error wont come

print(MAX_CONST)

nums = [0,0,1,1,1,2,2,3,3,4]
k = 0
temp = nums.copy()
nums.clear()
nums.append(temp[0])
for i in range (len(temp)-1):
    if(temp[i] != temp[i+1]):
        nums.append(temp[i+1])
print(len(nums))
print(nums)