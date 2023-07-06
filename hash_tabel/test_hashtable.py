from hash_tabel.hashtable import HashTable
from hash_tabel.hashmap_repeated_word import repeated_word

def test_hash_table():
    tabel1 = HashTable()
    tabel1.set('name', 'Ahmad')
    tabel1.set('age', 25)
    tabel1.set('country', 'Jordan')
    

    assert tabel1.get('name') == 'Ahmad'
    assert tabel1.get('age') == 25
    assert tabel1.get('country') == 'Jordan'


def test_hash_table_keys():
    
    tabel1 = HashTable()
    tabel1.set('name', 'Ahmad')
    tabel1.set('country', 'Jordan')
    tabel1.set('age', 25)
    
    keys = tabel1.keys()
    keys.sort()
    excepted = ['name', 'country', 'age']
    excepted.sort()
    assert keys == excepted

    

def test_hash_table_collision():
    tabel1 = HashTable(2)
    tabel1.set('name', 'Ahmad')
    tabel1.set('country', 'Jordan')
    tabel1.set('age', 25)
    keys = tabel1.keys()
    keys.sort()
    excepted = ['name', 'country', 'age']
    excepted.sort()
    assert keys == excepted

def test_hash_table_has():
    tabel1 = HashTable()
    tabel1.set('name', 'Ahmad')
    tabel1.set('country', 'Jordan')
    tabel1.set('age', 25)
    
    assert tabel1.has('name') == True
    assert tabel1.has('country') == True
    assert tabel1.has('age') == True
    assert tabel1.has('not_found') == False

def test_hash_table_repeated_word():
    string = "Once upon a time, there was a brave princess who..."
    assert repeated_word(string) == 'a'

def test_hash_table_repeated_word2():
    string2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert repeated_word(string2) == 'it'

def test_hash_table_repeated_word3():
    string3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    assert repeated_word(string3) == 'summer'
    