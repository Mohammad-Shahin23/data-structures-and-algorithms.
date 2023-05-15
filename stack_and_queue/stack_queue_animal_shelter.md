# Code Challenge Class-12: pseudo

The Animal_Shelter class represents the shelter and provides methods for enqueuing (adding) animals to the shelter and dequeuing (removing)
The Enqueue method: allows the user to add an animal to the shelter by providing a dictionary representation of the animal with a "species" key indicating whether it is a dog or a cat.
The dequeue method: allows the user to remove an animal from the shelter based on their preference for either a dog or a cat.
The code uses a Queue1 object from the queue1 module to implement the underlying data structure for managing the animals in the shelter

# White Bord Class-12: Animal_Shelter

![MarineGEO circle logo](/stack_and_queue/png/Animal_Shelter.png)







## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `enqueue` | O(1)        | O(1)             |
| `denqueue` | O(n)      | O(1)             |

## Solution
    class Animal_Shelter:
    def __init__(self):
        
        self.animal_Shelter = Queue1()

    def enqueue(self, animal):
        
        if animal["species"] == "dog" or animal["species"] == "cat":
            self.animal_Shelter.enqueue(animal)
            print("Animal added to the shelter.")
        else:
            return "We only accept dogs or cats."

    def dequeue(self, pref):
        
        if pref == "dog" or pref == "cat":
            current = self.animal_Shelter.linkedlist.head

            while current is not None:
                if current.value["species"] == pref:
                    return self.animal_Shelter.linkedlist.delete(current.value)
                else:
                    current = current.next

            return None
