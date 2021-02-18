# Fenwick Tree Algorithm

Bir dizideki sayıların verimli bir şekilde parçalanabilir bir şekilde toplanabilmesine izin veren bir ağaç biçimidir. Örneğin bir dizi [2, 3, -1, 0, 6] şeklinde verildiğinde ve biz bu dizinin ilk üç öğresini [2, 3, -1] toplamak istediğimizde 2 + 3 + -1 = 4 şeklinde toplarız. Fenwick Tree buna farklı bir bakış açısından bakarak bu istenilen toplamı bit olarak toplar ve bize sonucu böyle verir. 

|Algoritma|		|Ortalama|	    |En kötü durumda|
| ------------- |:-------------:| -----:|
|Uzay|		    |O ( n )|	    |O ( n )|
|Arama|		    |O (log n )|	|O (log n )|
|Ekle|		    |O (log n )	O|  |(log n )|
|Sil|		    |O (log n )	O|  |(|log n )|


*  [Wikipedia](https://en.wikipedia.org/wiki/Fenwick_tree#Updating_and_Querying_the_Tree)
*  [C tutorial](https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/tutorial/)
*  [another tutorial](https://cp-algorithms.com/data_structures/fenwick.html)
 


