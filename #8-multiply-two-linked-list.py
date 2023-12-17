MOD = 10**9+7
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def convert(head):
    number = 0
    while head:
        number = number * 10 + head.data
        head = head.next
        
    return number
    
    
def multiplyTwoList(head1, head2):
    number1 = convert(head1)
    number2 = convert(head2)
    
    return (number1 * number2) % MOD
    
