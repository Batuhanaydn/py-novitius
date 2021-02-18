class FenwickTree:
    def __init__(self, BOYUT):
        self.boyut = BOYUT
        self.fenT = [0 for i in range(0, BOYUT)]

    def update(self, i, val):
        while i < self.boyut:
            self.fenT[i] += val
            i += i & (i)

    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.fenT[i]
            i -= i & (-i)
        return ret

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    f = FenwickTree(100)

    f.update(6, 20)
    f.update(6, 55)
    f.update(6, 75)
    f.update(1, 1)
    print(f.query(1)) # nasıl çalıştığını daha rahat anlamak ve birikimli toplamanın nasıl çalıştığını anlamak için f.update(1,1) değerinin val değerini bir bir arttırarak ilerleyiniz
