text = ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"]
print("\nOriginal list:")
print(text)
ch='c'
result=[i for i in text if i.startswith(ch)]
print(result)