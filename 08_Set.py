#### .......SET...............
                                                                #  OUTPUTS
#s  = set()
#print(type(s))                                                 #  <class 'set'>

#l = [1,2,3,4]
#s_from_list = set(l)
#s_from_list = set([1,2,3,4])
#print(s_from_list)                                              #  {1, 2, 3, 4}
#print(type(s_from_list))                                        #  <class 'set'>

s = set()
s.add(1)
s.add(3)
print(s)                                                         #  {1, 3}
s1 = s.union({1,2,3})
print(s1)                                                        #  {1, 2, 3}
s2 = s.intersection({1,2,3,4})
print(s2)                                                        #  {1, 3}

print(max(s2))                                                   #  3

s1 = {4,2}
print(s.isdisjoint(s1))                                          #  True
s1.remove(4)
print(s1)                                                        #  {2}

