class cat:
    name = None
    age = None
    poroda = None
    def __init__(self, name = None, age = None, poroda = None):
        self.geti(name, age, poroda)
        self.pri()

    def geti(self, name , age = None, poroda = None):
        self.name = name
        self.age = age
        self.poroda = poroda

    def pri(self):
        print(self.name, 'age:', self.age, 'porodad:', self.poroda)
cat1 = cat('Mari' , 3)

