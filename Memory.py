
class Memory:

    
    mem = [0]*52

    def store(self, ch, value):
        Memory.mem[self.indexof(ch)] = value 

    def indexof(self, ch):
        if not ch.isalpha():
            raise ValueError('invalid identifier argument')
        if ch.islower():
            intch = ord(ch)
            a = 'a'
            inta = ord(a)
            index = intch - inta
        else:
            intbc = ord(ch)
            ba = 'A'
            intba = ord(ba)
            index = 26 + intbc - intba
        return index

    def fetch(self, ch):
        return Memory.mem[self.indexof(ch)]
