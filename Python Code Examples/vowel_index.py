def vowel_2_index(string):
    ret = ""
    for i in range(len(string)):
        if string[i] in "aeiıoöuüAEIİOÖUÜ":
            ret=ret+str(i+1)
        else:
            ret=ret+string[i]
    return ret

print(vowel_2_index("batuhan aydın"))