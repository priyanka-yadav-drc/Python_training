from collections import Counter
dictt = {
 'V': 10,
 'VI': 10,
 'VII': 40,
 'VIII': 20,
 'IX': 70,
 'X': 80,
 'XI': 40,
 'XII': 20, 
 }

result=Counter(dictt.values())
print(result)