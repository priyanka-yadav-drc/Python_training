nums = [
        ["Red","Maroon","Yellow","Olive"],
        ["#FF0000", "#800000", "#FFFF00", "#808000"],
        ["rgb(255,0,0)","rgb(128,0,0)","rgb(255,255,0)","rgb(128,128,0)"]
       ]
n=1
for x in nums:
	del x[n]

print(nums)