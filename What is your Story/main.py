

def story():
    place = input('Where does the story take place?\n>>>')
    character = input('What is your character\'s name?\n>>>')
    hair_color = input('What is your character\'s hair color\n>>>')
    job = input('What is your character\'s job?\n>>>')
    tasıt = input("Nasıl bir araç kullanıyor?\n>>>")
    a = character + "sabah erkenden kalktı." + "Banyoya doğru ilerleyip "+ hair_color + " saçlarını taradı. Her sabah yaptığı gibi sabah duşunu aldı. \nİşe gitmek için hazırlandı. O bir "+job+"'-du/-di. Fakat o bir insan mıydı?"

    Is_it_human = input('Is your character human?\n>>>')

    if Is_it_human == "Yes":
        a += " evet o bir insandı. O yüzden "+tasıt+" atladı ve işe gitmek için uzaklaştı. Bu hikaye"+ place +" geçmiştir."
        return a
    elif Is_it_human == "No":
        a += " Tabi ki insan değildi bu yüzden garajına doğru ilerledi ve insan mekanoidlerin çektiği "+tasıt+" atladı. Ve "+job+ " işine doğru yola koyuldu. Bu hikaye "+ place + " Geçmektedir."
        return a

print(story())

# İts fucking bad