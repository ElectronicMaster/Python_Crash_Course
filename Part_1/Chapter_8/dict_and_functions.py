

def launch(phons: dict,launchd: list,cnt: int):
    keys = list(phons.keys())
    while keys:
        val = keys.pop()
        launchd.append(val)
        phons[val] = ""
    cnt = 0

count = 10
phones = {"Samsung" : "S24 Ultra", "Apple" : "iPhone 16", "Google" : "Pixel 9", "Nothing" : "Nothing Phone 2"}
launched = []

launch(phones,launched,count)

print(phones)
print(launched)
print(count)