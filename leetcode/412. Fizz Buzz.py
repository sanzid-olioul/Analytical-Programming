class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        i = 1
        while (i <= n):
            if i % 3 == 0 and i % 5 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))
            i += 1
        return result