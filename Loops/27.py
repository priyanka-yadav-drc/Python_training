result_str="";    
for row in range(0,7):    
    for column in range(0,5):     
        if ((row==0) or (column==2)):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
