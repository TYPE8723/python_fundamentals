class parentA:
    def __init__(self,val):
        print('Alen :'+val)
class parentB(parentA):
    def __init__(self,child_name):
        super().__init__('sebastian')
        print('Alens child :'+child_name)
        print('Called by child')
class parentC(parentB):
    def __init__(self):
        super().__init__('Carlo')
        print('Called by Carlo')
details = parentC()