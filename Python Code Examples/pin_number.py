def validate_pin(pin):
        number = ["1","2","3","4","5","6","7","8","9","0"]
        pins = []
        for i in pin:
                pins.append(i)
        for a in range(len(number)+1):
                pass
        for b in range(len(pins)+1):
                
            if number[a-1] == pins[b-1]:
                    return False
            if len(pins) == 4 or len(pins) == 6:
                    return True
       


print(validate_pin("1234"))