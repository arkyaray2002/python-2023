def rev_string(st):
    return (' ').join(st.split()[::-1])

def count_el(li, el):
    return li.count(el)

print(rev_string("I love apples"))
print(count_el([1,2,2,2,2,3,4,5], 2))
