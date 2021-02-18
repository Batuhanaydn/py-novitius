def convert(s): 
    if(len(s) == 0): 
        return
    s1 = '' 
    s1 += s[0] 
    for i in range(1, len(s)): 
        if (s[i] == '_') or (s[i] == '-'): 
            
            i += 1
        elif(s[i - 1] != '_') or (s[i - 1] != '-'): 
            s1 += s[i]  
    print(s1)      
              
  

def main(): 
    s = "The-Stealth-Warrior"
    convert(s) 
      
if __name__=="__main__": 
    main()  