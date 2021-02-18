goodPowers = [1,2,3,3,4,10]
evilPowers = [1,2,2,2,3,5,10]

def goodVsEvil(good, evil):
    goodRaces = good.split(" ")
    evilRaces = evil.split(" ")
    
    goodWorth = 0
    evilWorth = 0
    
    for i in range(len(goodRaces)):
      goodWorth = goodWorth + int(goodRaces[i])*goodPowers[i]
      
    for i in range(len(evilRaces)):
      evilWorth = evilWorth + int(evilRaces[i])*evilPowers[i]
      
    if goodWorth > evilWorth:
      return "Battle Result: Good triumphs over Evil"
    elif goodWorth < evilWorth:
      return "Battle Result: Evil eradicates all trace of Good"
    else:
      return "Battle Result: No victor on this battle field"
