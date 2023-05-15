
from queue1 import Queue1

class Animal_Shelter:
    def __init__(self):
        """
        Initializes an instance of the Animal_Shelter class.
        Creates an empty animal shelter using a Queue1 object.
        """
        self.animal_Shelter = Queue1()

    def enqueue(self, animal):
        """
        Enqueues an animal into the animal shelter.

        
        animal (dict): A dictionary representing the animal to be enqueued.
        The dictionary should have a "species" key with the value "dog" or "cat".

        """
        if animal["species"] == "dog" or animal["species"] == "cat":
            self.animal_Shelter.enqueue(animal)
            print("Animal added to the shelter.")
        else:
            return "We only accept dogs or cats."

    def dequeue(self, pref):
        """
        Dequeues an animal from the animal shelter based on preference then returns it 

        
        pref (str): The preferred species of the animal to dequeue.
        should be either "dog" or "cat".

        Returns:
            dict: A dictionary representing the dequeued animal.
                Returns None if no animal of the preferred species is found.
        """
        if pref == "dog" or pref == "cat":
            current = self.animal_Shelter.linkedlist.head

            while current is not None:
                if current.value["species"] == pref:
                    return self.animal_Shelter.linkedlist.delete(current.value)
                else:
                    current = current.next

            return None

           
                
    

    
# dog1 = Animal("dog","rex")
# dog2 = Animal("dog","re")
# dog3 = Animal("dog","rx")

a_s = Animal_Shelter()
a_s.enqueue({"species":"dog","name":"rex"})
a_s.enqueue({"species":"s","name":"rx"})
a_s.enqueue({"species":"cat","name":"rex"})
print(a_s.dequeue("cat"))
print(str(a_s.animal_Shelter))




