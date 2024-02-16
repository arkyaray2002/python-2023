import random
n = int(input("Enter the size of your list: "))
li = []
for i in range(n):
    li.append(round(random.random()))

print(li)
spans = []
for key,value in enumerate(li):
    if value == 0:
        start = key
        end = key
    
        for key2,value2 in enumerate(li[start+1:]):
            if value2 == 0:
                continue
            else:
                end += key2 
                break
    else:
        continue
    spans.append((start,end))

print(spans)
max_span = [abs(x-y) for (x,y) in spans]
required_span = spans[max_span.index(max(max_span))] 
print(f"Longest run of zeroes in \n{li}\nis {max(max_span) + 1}\nspan : {required_span[0]} : {required_span[1]}")
