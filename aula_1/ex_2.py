class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return str({
            'name': self.name,
            'email': self.email,
            'password': self.password
        })    

    def vender(self):
        pass

    def ver_vendas(self):
        pass
        
if __name__ == "__main__":
    
    name = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    password = input('Digite seu senha: ')

    u = User(name, email, password)
    
    u_serialized = str(u)

    with open('tmp.json', 'a') as f:
        f.write(str(u))
