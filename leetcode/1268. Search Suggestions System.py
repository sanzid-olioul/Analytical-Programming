class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        lst = []
        products = sorted(products)
        for c in searchWord:
            nslst = []
            for i in range(len(products)):
                if 