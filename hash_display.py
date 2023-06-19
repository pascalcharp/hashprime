import random


class simple_hash_statistics:
    def __init__(self, size):
        self.size = size
        self.buckets = [0] * size


    def generate_buckets_for(self, key_list):
        for key in key_list:
            hash = key % self.size
            self.buckets[hash] += 1

    def count_used_buckets(self):
        count = 0
        for bucket in self.buckets:
            if (bucket != 0):
                count += 1
        return count

    def display_buckets(self, title):
        print(f"Résultats pour {title}:")
        print(f"Taille de la table: {self.size}")
        print(f"Nombre de casiers utilisés: {self.count_used_buckets()}")
        for line in range(self.size):
            print(f"{line}: " + self.buckets[line] * "*")

    def reinitialiser(self):
        self.buckets = [0] * self.size





if __name__ == '__main__':
    n_elem = 50
    n_table = 20
    non_random_list_10 = [10 * i for i in range(n_elem)]
    non_random_list_5 = [5 * i for i in range(n_elem)]
    non_random_list_7 = [7 * i for i in range(n_elem)]

    random.seed()
    random_list = [random.randint(0, 1000) for i in range(n_elem)]


    hacheur = simple_hash_statistics(n_table)

    hacheur.generate_buckets_for(non_random_list_10)
    hacheur.display_buckets("Multiples de 10")
    hacheur.reinitialiser()

    hacheur.generate_buckets_for(non_random_list_5)
    hacheur.display_buckets("Multiples de 5")
    hacheur.reinitialiser()

    hacheur.generate_buckets_for(non_random_list_7)
    hacheur.display_buckets("Multiples de 7")
    hacheur.reinitialiser()

    hacheur.generate_buckets_for(random_list)
    hacheur.display_buckets("Nombres aléatoires")
    hacheur.reinitialiser()



