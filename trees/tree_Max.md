# Code Challenge Class-16: Max
we need to create a max method without passing any argument. 
which will then find the maximum number in a non ordered tree and returns its value.
# White Bord Class-15: Max
![MarineGEO circle logo](/trees/png/tree_max.png)







## Approach & Efficiency
| Function | Time Complexity | Space Complexity |
| -------- | -------------- | ---------------- |
| `pre_order` | O(logn)        | O (n)             |
| `Max` | O(n)      | O(n)             |

## Solution
    def Max(self):
        
        list_values = self.pre_order()

        if len(list_values) == 0:
            return None
        
        max=list_values[0]
        
        for value in list_values:
            if value >= max :
                max = value
        return max
    