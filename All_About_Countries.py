class USA():
    def capital(self):
        print("Washington, D.C. is the capital of the USA.")

    def language(self):
        print("The primary language spoken in the USA is English.")

    def type(self):
        print("The USA is a developed country.")

class Argentina():
    def capital(self):
        print("Buenos Aires is the capital of Argentina.")

    def language(self):
        print("The primary language spoken in Argentina is Spanish.")

    def type(self):
        print("Argentina is a developing country.")

obj_usa = USA()
obj_arg = Argentina()

for country in (obj_usa, obj_arg):
    country.capital()
    country.language()
    country.type()