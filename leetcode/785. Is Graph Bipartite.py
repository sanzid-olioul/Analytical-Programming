from  queue import Queue
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        qu = Queue()
        dct = {}
        for i in range(len(graph)):
            if len(graph[i])>0:
                if i not in dct.keys():
                    qu.put(i)
                    dct[i]= True
            while not qu.empty():
                vl = qu.get()
                for dt in graph[vl]:
                    if dt in dct.keys():
                        if dct[dt] == dct[vl]:
                            return False
                    else:
                        if dct[vl]:
                            dct[dt] = False
                        else:
                            dct[dt] = True
                        qu.put(dt)
        return True           