class Node:
    def __init__(self) -> None:
        self.key = None
        self.val = None
        self.next = None
class MyHashMap:
    def __init__(self):
        self.lst = [None for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        k = key%1000
        if self.lst[k]==None:
            nd = Node()
            nd.key = key
            nd.val = value
            self.lst[k] = nd
        else:
            temp = self.lst[k]
            while temp.next:
                if temp.key == key:
                    temp.val = value
                    return
                temp = temp.next
                
            if temp.key != key:
                nd = Node()
                nd.key = key
                nd.val = value
                temp.next = nd
            else:
                temp.val = value


    def get(self, key: int) -> int:
        k = key%1000
        if self.lst[k] and (self.lst[k]).key== key:
            return (self.lst[k]).val
        else:
            temp = self.lst[k]
            while temp:
                if temp.key == key:
                    return temp.val
                temp = temp.next
        return -1
        

    def remove(self, key: int) -> None:
        k = key%1000
        if self.lst[k]==None:
            return
        elif self.lst[k].key== key:
            self.lst[k] = (self.lst[k]).next
        else:
            temp = self.lst[k]
            while temp.next:
                tem2 = temp.next
                if tem2.key == key:
                    temp.next = tem2.next
                    break
                temp = temp.next
