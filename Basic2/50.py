print("Input a text with two words 'Python' and 'Java'")
text = raw_input().split()
for i in range(len(text)):
    if "Python" in text[i]: 
    	n = text[i].index("Python");text[i] = text[i][:n] + "Java" + text[i][n + 6:]
    elif "Java" in text[i]:
    	n = text[i].index("Java");text[i] = text[i][:n] + "Python" + text[i][n + 4:]
print(' '.join(text))
