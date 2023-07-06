from hash_tabel.hashtable import HashTable
from hash_tabel.left_join import left_join

def test_left_join():
    hash_1 = HashTable()
    hash_1.set('fond', 'enamored')
    hash_1.set('wrath', 'anger')
    hash_1.set('diligent', 'employed')
    hash_1.set('outfit', 'garb')
    hash_1.set('guide', 'usher')

    hash_2 = HashTable()
    hash_2.set('fond', 'averse')
    hash_2.set('wrath', 'delight')
    hash_2.set('diligent', 'idle')
    hash_2.set('guide', 'follow')
    hash_2.set('flow', 'jam')

    expected = [['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['outfit', 'garb',None] ,  ['guide', 'usher', 'follow']]
    expected.sort()
    actual = left_join(hash_1, hash_2)
    actual.sort()

    assert actual == expected