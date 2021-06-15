#  .....Multilevel Inheritance......

class Dad :
    basketball = 1
class Son(Dad) :
    dance = 1
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"
class Grandson(Son) :
    dance = 6
    def isdance(self):
        return f"Jakson yeah!" \
           f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
sambhu = Grandson()
print(sambhu.isdance())             # Jakson yeah!Yes I dance very awesomely 6 no of times
print(sambhu.basketball)            # 1