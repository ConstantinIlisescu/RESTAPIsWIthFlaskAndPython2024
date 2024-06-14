l = ["Bob","Rolf","Anne"] # list - can be modified and the order is always as defined 
t = ("Bob","Rolf","Anne") # tuple - this can't be modified
s = {"Bob","Rolf","Anne"} # set - set can't have duplicate elements, the order is random despite the order of items

# list and tuple can be selected with subscript notation
print(l[0])
print(t[1])

l[0] = "Costa" # can assign a different value to list but not to tuple

l.append("Joe") # can add to list but not to tuple
l.remove("Rolf")

s.add("Costa") # can add to the set, it has no order si is just add not append
s.add("Costa") # it will just ignore this add as costa is in the set already

#set exercise 
friends = {"Bob","Rolf","Anne"}
abroad = {"Bob","Anne"}
#will take the first set and remove all the values present in the second set = returns {"Rolf"}
local_friends = friends.difference(abroad)

local = {"Rolf"}
friends = local.union(abroad) # combines both sets

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science) # return the values present in both sets