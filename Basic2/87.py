def func(code):
	if len(code)==8 or len(code)==12:
		print "valid"
	else:
		print "invalid"

func('12345678')
func('uytrewdfghjk')
func('1234567')
