n = int(input())
d = {}
for i in range(n):
    team1, s1, team2, s2 = input().split(';')
    diff = int(s1) - int(s2)
    result1 = d.setdefault(team1, [0, 0, 0, 0, 0])
    result2 = d.setdefault(team2, [0, 0, 0, 0, 0])
    result1[0] += 1
    result2[0] += 1
    if diff > 0:
        result1[1] += 1
        result1[4] += 3
        result2[3] += 1
    elif diff < 0:
        result2[1] += 1
        result2[4] += 3
        result1[3] += 1
    else:
        result2[2] += 1
        result2[4] += 1
        result1[2] += 1
        result1[4] += 1
for key, value in d.items():
    print(key + ':' + ' '.join(map(str, value))) # объединение списка в строку
    
    
        
        
        
    