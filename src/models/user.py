
# Esto es la clase Usuario y devuelve un objeto tipo usuario con sus respectivos parametros
class User :
    def __init__(self, email, name, age) -> None:
            self.email = email
            self.age = age
            self.name = name


nuevo_usuario = User("Alejandro@gmail.com",  "Alejandro", 12)

print(nuevo_usuario.age)