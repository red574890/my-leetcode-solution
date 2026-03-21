class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        a = 0   # row
        b = 0   # col
        order = 'r'

        right_bound = col - 1
        left_bound = 0
        up_bound = 0
        down_bound = row - 1

        res = []

        for _ in range(row * col):
            res.append(matrix[a][b])

            if order == 'r':
                if b < right_bound:
                    b += 1
                else:
                    order = 'd'
                    up_bound += 1
                    a += 1

            elif order == 'd':
                if a < down_bound:
                    a += 1
                else:
                    order = 'l'
                    right_bound -= 1
                    b -= 1

            elif order == 'l':
                if b > left_bound:
                    b -= 1
                else:
                    order = 'u'
                    down_bound -= 1
                    a -= 1

            elif order == 'u':
                if a > up_bound:
                    a -= 1
                else:
                    order = 'r'
                    left_bound += 1
                    b += 1

        return res
