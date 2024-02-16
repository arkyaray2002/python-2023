def sorted_hyphen(st):
    li = st.split('-')
    li.sort()
    return ('-').join(li)

print(sorted_hyphen("green-red-yellow-black-white"))
