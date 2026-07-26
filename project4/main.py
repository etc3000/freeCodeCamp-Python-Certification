class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        converted_string = [ord(char) for char in string]
        return sum(converted_string)
    
    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            self.collection[hash_key].update({key: value})
        else:
            self.collection[hash_key] = {key: value}
        
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            self.collection[hash_key].pop(key, None)

    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection:
            return self.collection[hash_key].get(key, None)
        return None

