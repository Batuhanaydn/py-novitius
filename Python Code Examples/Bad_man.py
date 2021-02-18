def get_villain_name(birth): 
    b = birth.split('/')
    first = [ "The Evil","The Vile","The Cruel", "The Trashy","The Despicable", "The Embarrassing", "The Disreputable","The Atrocious", "The Twirling",  "The Orange","The Terrifying", "The Awkward"]
    last = ["Mustache", "Pickle", "Hood Ornament", "Raisin", "Recycling Bin", "Potato", "Tomato", "House Cat", "Teaspoon", "Laundry Basket"]
    for ay, isim in enumerate(first, start=1):         
        if str(ay) == b[1]:
            ilk = isim
    
    for gun, lastit in enumerate(last, start=0):
        if int(b[1]) % 10 == gun:
            son = lastit
    
    return ilk + " " + son    
    
    
            

print(get_villain_name("1/1/2000"))