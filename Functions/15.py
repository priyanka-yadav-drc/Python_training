def func():
	items=[n for n in raw_input().split('-')]
	items.sort()
	print('-'.join(items))

func()