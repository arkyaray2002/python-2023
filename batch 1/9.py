d = {}
for i in range(int(input("Enter the number of entries : \n"))):
    name = input("Enter cricketers name: ")
    runs = int(input("Enter runs: "))
    d[name] = runs

sorted_d = dict(sorted(d.items(), key=lambda item : item[1]))
max_runs_name = [n for (n,r) in d.items() if r == max([x for (y,x) in d.items()])][0]
names = d.keys()
new_player = input("Enter player name: ")
new_runs = int(input("Enter runs: "))
d[new_player] = new_runs
min_runs_name = [n for (n,r) in d.items() if r == min([x for (y,x) in d.items()])][0]
d.pop(min_runs_name)
print(d)
