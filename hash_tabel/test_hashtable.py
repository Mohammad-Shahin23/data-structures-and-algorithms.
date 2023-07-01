from hashtable import HashTable

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