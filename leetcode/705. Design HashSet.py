class Node:
    def __init__(self) -> None:
        self.val = 0
        self.next = None
class MyHashSet:
    def __init__(self):
        self.lst = [None for i in range(1000)]
        
    def add(self, key: int) -> None:
        k = key%1000
        if self.lst[k]==None:
            nd = Node()
            nd.val = key
            self.lst[k] = nd
        else:
            nd = Node()
            nd.val = key
            temp = self.lst[k]
            while temp.next:
                temp = temp.next
            if temp.val != key:
                temp.next = nd
            
    def remove(self, key: int) -> None:
        k = key%1000
        if self.lst[k]==None:
            return
        elif self.lst[k].val== key:
            self.lst[k] = (self.lst[k]).next
        else:
            temp = self.lst[k]
            while temp.next:
                tem2 = temp.next
                if tem2.val == key:
                    temp.next = tem2.next
                    break
                temp = temp.next

    def contains(self, key: int) -> bool:
        k = key%1000
        if self.lst[k]== key:
            return True
        else:
            temp = self.lst[k]
            while temp:
                if temp.val == key:
                    return True
                temp = temp.next
        return False
