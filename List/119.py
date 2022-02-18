list1=['blue','red','black','pink']
sub_str='nk'
if any(sub_str in s for s in list1):
	print("present")
else:
	print("absent")