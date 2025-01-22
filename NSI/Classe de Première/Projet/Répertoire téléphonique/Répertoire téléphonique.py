from sympy import mod_inverse

class PseudoRandomNumberGenerator:
    def __init__(self, seed, salt):
        self.salt = salt
        self.seed = seed
        self.modulus = 2**31 - 1  # Un grand nombre premier, souvent utilisé
        self.a = 1103516746  # Un multiplicateur choisi
        self.c = 12345  # Une constante d'incrémentation

    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.modulus
        return self.seed
    
    def salting(self):
        self.salt = [ord(char) for char in self.salt]
        x=1
        for number in self.salt:
            x *= number
        self.salt = x

        return x*self.seed
    
def obfuscate(user_name):
    user_name = [ord(char) for char in user_name]
    x=1
    for number in user_name:
        x *= number
    user_name = x
    user_name = user_name
    
def reverse_lcg(final_result, a, c, m, steps):
    # Find the modular inverse of a
    a_inv = mod_inverse(a, m)
        
    # Start from the final result and reverse steps
    current = final_result
    for _ in range(steps):
        current = (current - c) * a_inv % m
        
    return current

def search(adress):
    name_to_search = input("Veuillez entrer un nom : ")
    with open(adress, "r") as f:
        repertoire = f.read()
    repertoire = repertoire.split("\n")
    repertoire = repertoire[:len(repertoire)-1]
        
    user_founds = []
    for i in range(0, len(repertoire), 2):
        if repertoire[i] == name_to_search:
            phone_number = int(repertoire[i+1])
            salt = [ord(char) for char in repertoire[i]]
            x=1
            for number in salt:
                x *= number
            phone_number //= x
            phone_number = reverse_lcg(phone_number, 1103516746, 12345, 2**31 - 1, 100)
            user_founds.append(f"{repertoire[i]} : {str(phone_number).zfill(10)}")
    
    return user_founds

def ask():
    user_name = input("Veuillez entrer votre nom d'utilisateur : ")
        
    while user_name == "" or any(char.isdigit() for char in user_name):
        user_name = input("Nom d'utilisateur incorrect, veuillez en entrer un nouveau nom: ")
        
    phone_number = input("Veuillez entrer votre numéro de téléphone : ")
    try:
        phone_number = int(phone_number)
    except ValueError:
        pass

    while len(str(phone_number).zfill(10)) != 10 or type(phone_number) != int:
        phone_number = input("Numéro incorrect, veuillez entrer un nouveau numéro: ")
        try:
            phone_number = int(phone_number)
        except ValueError:
            pass

    return user_name, phone_number

while True: 
    print("Tapez 0 si vous voulez quitter\nTapez 1 si vous voulez enregistrer un nouveau numéro\nTapez 2 si vous voulez rechercher un numéro")
    user_input = input(":")

    while user_input not in ["0", "1", "2"]:
        user_input = input("Option non-disponible, veuillez entrer 0, 1 ou 2 : ") 


    if user_input == "0":
        break

    elif user_input == "1":
        user_name, phone_number = ask()
        
        pseudo_random_number_generator = PseudoRandomNumberGenerator(phone_number, user_name)
        for _ in range(100):
            pseudo_random_number_generator.next()
        
        pseudo_random_number = pseudo_random_number_generator.salting()
        
        with open("Répertoire téléphonique/Répertoire.txt", "a") as f:
            f.write(user_name+"\n")
            f.write(str(pseudo_random_number)+"\n")
        
    elif user_input == "2":
        user_founds = search("Répertoire téléphonique/Répertoire.txt")
        
        if len(user_founds) != 0:
            for name in user_founds:
                print(name)
        else:
            print("Personne inconnue")
