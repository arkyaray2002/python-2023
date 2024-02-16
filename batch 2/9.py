li = list(map(int, input("Enter elements: \n").split()))
n = int(input("Enter the target value: \n"))


# method 1(hashing):
# time complexity O(n):

def twoSumHashing(li, target):
    hashTable = {}

    for key,value in enumerate(li):
        complement_val = target - value
        if complement_val in hashTable and complement_val in li:
            print(f"( {li.index(complement_val)} , {key} )")
        hashTable[key] = value

twoSumHashing(li,n)

print("------------------------------")


# method 2(brute force):
# time complexity O(n**2):

def twoSum(li, target):
    for i in li[:-1]:
        for j in li[i+1:]:
            if i + j == target:
                print(f"( {li.index(i)} , {li.index(j)} )")

twoSum(li,n)

