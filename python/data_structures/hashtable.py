class Hashtable:
    """
    Put docstring here
    """
    def __init__(self, size=11):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash_function(self, key, size):
        if type(key) == int:
            return key % size
        elif type(key) == str:
            return sum([ord(c) for c in key]) % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def set(self, key, value):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = value  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else:
                    self.data[next_slot] = value  # replace

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                if self.position == start_slot:
                    stop = True
        return data

    def has(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return found

    def keys(self):
        keys_collection = []
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                keys_collection.append(self.slots[i])
        return keys_collection

    def hash(self, key):
        return self.hash_function(key, len(self.slots))
