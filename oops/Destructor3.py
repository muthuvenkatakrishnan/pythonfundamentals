class Alpha:

    def __init__(self, beta):
        self.beta = beta

class Beta:

    def __init__(self):
        self.alpha = Alpha(self)
    
    def __del__(self):
        print('Object got deleted')
    
def display():

    beta = Beta()

display()