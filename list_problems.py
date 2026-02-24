# square of the given numbers
l = list(map(int, input().split()))
sq = [x**2 for x in l]
print(sq)

# filter the even numbers from the list
num = list(map(int, input().split()))
even = [x for x in num if x % 2 == 0]
print(even)

#find common elements in two lists
li = list(map(int , input().split()))
li2 = list(map(int, input().split()))
common = [x for x in li if x in li2]
print(common)

#remove the duplicates from the list
list_val = list(map(int, input().split()))
uniq = []
for x in list_val:
    if x not in uniq:
        uniq.append(x)
print(uniq)

#reverse the list
lt = list(map(int, input().split()))
rev = []
for i in range(len(lt)-1, -1, -1):
    rev.append(lt[i])
print(rev)


