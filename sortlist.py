def stuff ():
 lola_list = [9,10,1,2,3,4,5,6,7,8,'a','b','c','d','e']
 lolalist = []
 lolalist1 =[]
 lolalist2=[]
 mydict= dict()
 for i in lola_list:
  if isinstance (i,str):
   lolalist.append(i)     
   mydict['characters']= sorted(lolalist)
  elif isinstance (i,int):      
   if i% 2 == 0:
    lolalist1.append(i)    
    mydict['evens'] = sorted(lolalist1)
   elif i%2==1:
    lolalist2.append(i)
    mydict['odds']= sorted(lolalist2)

    

   else:
    print ("invalid")
 return mydict
print (stuff())