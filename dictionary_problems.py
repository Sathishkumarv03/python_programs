# -------------------------------
# 1️⃣ Count frequency of characters in a string
# -------------------------------

s = input("Enter a string: ")
dicti = {}

for ch in s:
    if ch in dicti:
        dicti[ch] += 1
    else:
        dicti[ch] = 1

print("Character Frequency:", dicti)


# -------------------------------
# 2️⃣ Merge Two Dictionaries
# -------------------------------

input1 = input("Enter first dictionary (key value pairs): ").split()
d1 = {}

for i in range(0, len(input1), 2):
    k = input1[i]
    v = int(input1[i + 1])
    d1[k] = v

input2 = input("Enter second dictionary (key value pairs): ").split()
d2 = {}

for i in range(0, len(input2), 2):
    k = input2[i]
    v = int(input2[i + 1])
    d2[k] = v

for k in d2:
    d1[k] = d2[k]

print("Merged Dictionary:", d1)


# -------------------------------
# 3️⃣ Sort Dictionary by Values (Descending)
# -------------------------------

dy = input("Enter dictionary to sort (key value pairs): ").split()
d = {}

for i in range(0, len(dy), 2):
    k = dy[i]
    v = int(dy[i + 1])
    d[k] = v

d_sort = sorted(d.items(), key=lambda x: x[1], reverse=True)
d_sorted = dict(d_sort)

print("Sorted Dictionary (by values descending):", d_sorted)


# -------------------------------
# 4️⃣ Create Dictionary From Two Lists
# -------------------------------

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

d = {}

for i in range(len(l1)):
    d[l1[i]] = l2[i]

print("Dictionary from Two Lists:", d)


# -------------------------------
# 5️⃣ Find Key with Maximum Value
# -------------------------------

d = {'a': 1, 'b': 2, 'c': 3, 'd': 3}

max_k = list(d.keys())[0]
max_v = d[max_k]

for k in d:
    if d[k] > max_v:
        max_v = d[k]
        max_k = k

print("Key with Maximum Value:", max_k)