class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age  = age
        self.pay  = pay
        self.job  = job

    def lastname(self):
        return  self.name.split()[-1]

    def giveraise(self,percent):
        #return self.pay *= (1.0 + percent)
        self.pay *= (1.0 + percent)
        return self.pay