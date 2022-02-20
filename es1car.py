nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."
#a)
my_list = []

for i in nums:

    if (i % 8 == 0):
        
        my_list.append(i)

print(my_list)

#a corretto)
a = [num for num in nums if num % 8 == 0]
print(a)

#b

b = [num for num in nums if '6' in str(num)]
print('numeri con 6:')
print(b)

#c

print('spazi nella stringa:')
print (len([char for char in string if char == ' ']))
#oppure
c = [1 for s in string if ' ' in s]
sum(c)
#d
my_str = []
el = string.split()
my_str.append(el)
print(my_str)
d = [i for i in my_str if len(i) < 5]
print(list(d))

#print([i for i in string.split(' ') if len (i) < 5])







