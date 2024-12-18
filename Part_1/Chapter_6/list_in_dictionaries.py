favourite_language = {
    'sai' : ['python','java','javascript'],
    "jishnu" : ['cpp'],
    'hima' : ['cpp','python'],
    'thiru' : ['java']
}

for name,languages in favourite_language.items():
    if(len(languages) == 1):
        print(f"{name.title()}'s favourite language is {languages[0]}\n")
    else:
        print(f"{name.title()}'s favourite languages are:")
        for language in languages:
            print(f"\t{language}")
        print()