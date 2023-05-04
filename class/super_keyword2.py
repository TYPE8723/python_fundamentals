class Animals:
    def __init__(self):
        self.animal = True
        self.legs = True
        self.wings = True
        self.hands = True
        self.plant = False
    def is_bird(self,name):
        if self.wings == True:
            print ('bird name :',name)
            print ('bird fly status :',self.wings)
    def is_animal(self,name,place):#land or water
        if self.legs and self.wings == True:
            print('can wwalk on land :',self.legs)
            print('can swim :',self.wings)
            print(' name :'+name+' place : '+place)
         
    
class living(Animals):
    def __init__(self):
        super().__init__()
    def is_bird(self):
        super().is_bird('crow')
    def is_animal(self):
        super().is_animal('turtle','land_and_water')
obj = living()
obj.is_bird()
obj.is_animal()

    