Loading
-------
"How 'full' is the hash table?"
0 |-> D -> M -> Q
1 |-> H -> R -> X -> Y
2 |-> A -> I -> 0
3 |-> C -> J -> L -> N -> Z
4 |-> G -> S -> U
5 |-> B -> O -> 1 -> 2
6 |-> E -> K -> P -> W
7 |-> F -> T -> V
load_factor = number_of_items / number_of_slots_in_array
load_factor = 29 / 8 = 3.625
load_factor = 29 / 256 = 0.113
When the load factor > 0.7, it's time to increase the number of slots
When the load factor < 0.2, it's time to decrease the number of slots (down to some minimum)
"Rehashing"
-----------
Make a new array of double the size
Go through all the elements in the old hash table
Insert them into the new array