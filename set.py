#----- Set comprehsion method using and logic buit ------------------------
a = {2,5,6,3,}  # this method is difference.
b = {3,5,7,8} # remove elment present in one set but not in another
print(a.difference(b))
print(b.difference(a))
 
a = {4,8,5,6} # This method is difference_update.
b = {5,2,3,8} # remove element of another set from the current set 
(a.difference_update(b))
print(a)

a = {9,2,5,7} # This method is discard.
a.discard(2) # remove an element from the set if it exits 
print(a)

a = {2,6,4,8} #This method is intersection.
b = {6,8,3,9,2} #return commmon element of two or more set .
print(a.intersection(b))

a = {2,6,7,3}  # This method is isdisjoint.
b = {8,9,1,5,4} # return TRUE if two set have no common element.
print(a.isdisjoint(b)) 

a = {2,8,6,3,4}  # This method is issuperset.
b = {2,6,4,2}  # return TRUE if a set contain all element of another set.
print(a.issuperset(b))

print("-------------------")

# ------------ tuple logic question ----------------






