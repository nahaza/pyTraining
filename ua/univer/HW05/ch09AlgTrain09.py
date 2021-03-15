# 9. Assume each of the variables set1 and set2 references a set. Write code that creates
# another set containing the elements that appear in set2 but not in set1, and assigns
# the resulting set to the variable set3.

set1 = set([1, 2, 3, 4, 5, 6])
set2 = set([2, 4, 6, 7, 8, 9])
set3 = set2.difference(set1)


print(set3)
