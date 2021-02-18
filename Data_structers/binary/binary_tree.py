"""
Bir binary arama ağacı oluşturalım
"""

class dugum:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent # Burada kullandığımız parent sayesinde ileride ağaç içerisinde daha kolay silme işlemlerimizi gerçekleştireceğiz
        self.left = None
        self.right = None

    def __repr__(self):
        r"""
        Burada kullandığımız __repr__ sınıfı python'da özel bir sınıftır. Bu yöntemi kullanarak 
        sınıf nesnelerimizin kendi dize temsilini tanımlayabiliriz. 
        """
        from pprint import pformat # pprint'ten kısaca bahsetmek gerekirse PrettyPrinter'in kısaltılmasıdır. yazdırdığınız verinin daha düzenli ve okunabilir olmasını sağlar


        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)

class BasicBinarySearchTree:
    def __init__(self, root = None):
        self.root = root

    def __str__(self):
        r"""
        Kullanılan tüm düğümlerin sırasına göre bir dizesini döndürmek için kullancağız
        """
        return str(self.root)
    
    def __yeniden_atama(self, node, new_child):
        if new_child is not None:
            new_child.parent = node.parent
        if node.parent is not None:
            if self.is_right(node):
                node.parent.right = new_child
            else:
                node.parent.left = new_child
        else:
            self.root = new_child

    def is_right(self, node):
        return node == node.parent.right

    def empty(self):
        return self.root is None

    def __ekle(self, value):
        new_node = dugum(value, None) # yeni bir düğüm oluştur
        if self.empty(): # Eğer ağacımız boş ise
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def ekle(self, *values):
        for value in values:
            self.__ekle(value)
        return self

    def arama(self, value):
        if self.empty():
            raise IndexError("Hata: Ağaçta hiçbir şey yok, lütfen başka bir fonksiyon kullanın")
        else:
            node = self.root
            # if str(node).isalpha == True:
            #     raise TypeError("Hata: Lütfen tanımlı bir değer giriniz")

            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            return node

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if not self.empty():
            while node.right is not None:
                node = node.right
        return node

    def get_min(self, node=None):
        if node is None:
            node = self.root
        if not self.empty():
            while node.left is not None:
                node = node.left
        return node

    def sil(self, value):
        node = self.arama(value)
        if node is not None:
            if node.left is None and node.right is None: # türkçeleştirirsek sağın ve solun hiç childı yoksa
                self.__yeniden_atama(node,None) 
            elif node.left is None: # sadece sağ için
                self.__yeniden_atama(node, None)
            elif node.right is None: # sadece sol için
                self.__yeniden_atama(node, None)
            else:
                temp_node = self.get_max(
                    node.left
                )
                self.sil(temp_node.value)
                node.value = (
                    temp_node.value
                )
    
    def preorder_traverse(self, node): # Bunu nasıl anlamlı bir şekilde türkçeleştirebilirim bulamadım
        if node is not None:
            yield node 
            yield from self.preorder_traverse(node.left)
            yield from self.preorder_traverse(node.right)
    

    def traversel_tree(self, traversel_function=None):
        """
        Bu işlev ağaçta gezinmeye yaramakta
        """
        if traversel_function is None:
            return self.preorder_traverse(self.root)
        else:
            return traversel_function(self.root)
    
    def sıra(self, arr: list, node: dugum):
        if node:
            self.sıra(arr, node.left)
            arr.append(node.value)
            self.sıra(arr, node.right)

    def enKucukEleman(self, k: int, node: dugum):
        arr = []
        self.sıra(arr, node)
        return arr[k - 1]

def tasıyıcı(curr_node):
    """
    tasıyıcı(left, right, self)
    """
    node_list = list()
    if curr_node is not None:
        node_list = tasıyıcı(curr_node.left) + tasıyıcı(curr_node.right) + [curr_node]
    return node_list



def binary_search_tree():

    testListe = (8, 15, 1, 35, 46, 85, 14, 0, 78, 21)
    t = BasicBinarySearchTree()
    for i in testListe:
        t.ekle(i)
    
    print(t)

    if t.arama(0) is not None:
        print("0 (sıfır) değeri mevcuttur")
    else:
        print("Aradığınız değer mevcut değildir")

    if t.arama(23) is not None:
        print("23 (yirmiuc) değeri mevcuttur")
    else:
        print("Aradığınız değer mevcut değildir")

    if not t.empty():
        print("Maksimum değer: ", t.get_max().value)
        print("Maksimum değer: ", t.get_min().value)

    # for i in testListe:
    #     t.sil(i)
    #     print(i)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    binary_search_tree()

"""
Bu kodu geliştirirken 
https://github.com/TheAlgorithms, 
https://www.educative.io/edpresso/binary-trees-in-python, 
https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm, 
https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree,
https://www.section.io/engineering-education/binary-tree-data-structure-python/ sitelerinden yararlandım.
Daha ayrıntılı bilgi için inceleyebilirsiniz.
"""