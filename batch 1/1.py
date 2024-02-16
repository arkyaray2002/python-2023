def expanding(li):
    diff = [j - i for (i,j) in list(zip(li[:-1], li[1:]))]
    diff_of_diffs = [j - i for (i,j) in list(zip(diff[:-1], diff[1:]))]
    return True if len([x for x in diff_of_diffs if x>=0]) == 0 else False

li = list(map(int, input("Enter the elements: \n").split()))
print(expanding(li))
