String=str(input("Enter a sentence:"))
def lower_upper(String):
 pass
 return lower_upper
lower=0
count=1
upper=0
count1=1
for i in String:
      if i in String:
         if(i.islower()):
            lower=lower+count
         else:
            if(i.isupper()):
             upper=upper+count1
print("The number of  Uppercase characters are:",upper)
print("The number of Lowercase characters are:",lower)
lower_upper(String)



