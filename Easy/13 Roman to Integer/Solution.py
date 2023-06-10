class Solution:
    def romanToInt(self, s: str) -> int:
        # Define digit mapping:
        roman_list = [('M', 1000),
                      ('CM', 900),
                      ('D', 500),
                      ('CD', 400),
                      ('C', 100),
                      ('XC', 90),
                      ('L', 50),
                      ('XL', 40),
                      ('X', 10),
                      ('IX', 9),
                      ('V', 5),
                      ('IV', 4),
                      ('I', 1)
                      ]
        # Special case:
        if s == 'N':
            return 0

        result = 0
        index = 0
        for i, integer in roman_list:
            while s[index:index + len(i)] == i:
                result += integer
                index += len(i)
                
        return result
