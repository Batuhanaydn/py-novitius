def DNA_strand(dna):
    back = ""
    for i in dna:
        if i == "A":
            back = back + "T"
        if i == "T":
            back = back + "A"
        if i == "G":
            back = back + "C"
        if i == "C":
            back = back + "G"
    return back
print(DNA_strand("ATTGC"))