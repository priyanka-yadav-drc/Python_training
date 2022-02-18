nums=[3,11,5,4,6,7,2]

first_even = next((el for el in nums if el%2==0),-1)
first_odd = next((el for el in nums if el%2!=0),-1)
print(first_odd)
print(first_even)