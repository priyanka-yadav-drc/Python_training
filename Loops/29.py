result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (((column==0 or column==4) and (row!=2 and row!=3 and row!=4)) or ((column==1 or column==3) and (row==2 or row==4)) or (row==3 and column==2)):    
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
