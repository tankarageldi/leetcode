class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def findMiddle(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.data
    
def main():
        
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    print(findMiddle(head))
if __name__ == '__main__':
    main()