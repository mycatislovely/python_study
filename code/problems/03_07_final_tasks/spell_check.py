d = set()
for _ in range(int(input())):
    d.add(input().lower())
errors = set()
for _ in range(int(input())):
    for w in input().lower().split():
        if w not in d:
            errors.add(w)
    for e in errors:
        print(e)       
   
