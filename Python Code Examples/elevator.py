def elevatorDistance(arr: list):
    toplam = 0
    for i in range(len(arr)-1):
        toplam += abs(arr[i] - arr[i+1])
    return toplam
print(elevatorDistance([7,1,7,1]))
