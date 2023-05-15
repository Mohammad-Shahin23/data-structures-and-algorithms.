from stack_queue_animal_shelter import Animal_Shelter

def test_enqueu1():
    # Test case 1: Enqueue a dog and dequeue a dog
    shelter = Animal_Shelter()
    shelter.enqueue({"species": "dog"})
    assert shelter.dequeue("dog") == {"species": "dog"}

def test_enqueu2():
    # Test case 2: Enqueue a cat and dequeue a cat
    shelter = Animal_Shelter()
    shelter.enqueue({"species": "cat"})
    assert shelter.dequeue("cat") == {"species": "cat"}

def test_enqueu3():
    # Test case 3: Enqueue a dog and dequeue a cat
    shelter = Animal_Shelter()
    shelter.enqueue({"species": "dog"})
    assert shelter.dequeue("cat") is None

def test_enqueu4():
    # Test case 4: Enqueue a cat and dequeue a dog
    shelter = Animal_Shelter()
    shelter.enqueue({"species": "cat"})
    assert shelter.dequeue("dog") is None

def test_enqueu5():

    # Test case 5: Enqueue an invalid species
    shelter = Animal_Shelter()
    assert shelter.enqueue({"species": "bird"}) == "We only accept dogs or cats."

def test_dequeue1():
    # Test case 6: Dequeue from an empty shelter
    shelter = Animal_Shelter()
    assert shelter.dequeue("dog") is None

    
