import random

class Coin:
        def __init__(self, rare = False, clean = True, heads = True, **kwargs):

                for key, value in kwargs.items():
                        setattr(self, key, value)
                
                self.is_rare = rare
                self.is_clean = clean
                self.heads = heads

                if self.is_rare:
                        self.value = self.original_value * 1.25
                else:
                        self.value = self.original_value

                if self.is_clean:
                        self.colour = self.clean_colour
                else:
                        self.colour = self.rusty_colour

        def __del__ (self):
                print("Coin spent")

        def __str__ (self):
                if self.original_value >= 1:
                        return "${} coin".format(int(self.original_value))
                else:
                        return "{}p coin".format(int(self.original_value*100))

        def rust(self):
                self.colour = self.rusty_colour

        
        def clean(self):
                self.colour = self.clean_colour

        def flip(self):
                heads_options = [True,False]
                choice = random.choice(heads_options)
                self.heads = choice

        

class One_Pound(Coin):
        def __init__(self):
                data = {
                        "original_value": 1.00,
                        "clean_colour": "gold",
                        "rusty_colour": "greenish",
                        "num_edges": 1,
                        "diameter": 22.5,
                        "thickness": 3.15,
                        "mass": 9.5
                        }
                super().__init__(**data)

class One_Pence(Coin):
        def __init__(self):
                data = {
                        "original_value": 0.01,
                        "clean_colour": "bronze",
                        "rusty_colour": "brownish",
                        "num_edges": 1,
                        "diameter": 20.3,
                        "thickness": 1.52,
                        "mass": 3.56
                        }
                super().__init__(**data)
        
class Five_Pence(Coin):
        def __init__(self):
                data = {
                        "original_value": 0.05,
                        "clean_colour": "silver",
                        "rusty_colour": None,
                        "num_edges": 1,
                        "diameter": 18.0,
                        "thickness": 1.77,
                        "mass": 3.25
                        }
                super().__init__(**data)

                def rust(self):
                        self.colour = self.clean_colour

coins = [One_Pence(), Five_Pence(), One_Pound()]

for coin in coins:
        arguments = [coin, coin.colour, coin.value, coin.diameter, coin. thickness,
                     coin.num_edges, coin.mass]

        string = "{} - Colour: {}, value: {}, diameter(mm): {}, thickness(mm): {}, number of edges: {}, mass(g): {}".format(*arguments)
        print(string)
