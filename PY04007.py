class Matrix:
    def __init__(self, n, m):
        self.n = n  
        self.m = m  
        self.data = [[0] * m for _ in range(n)]  
    def input_matrix(self):
        for i in range(self.n):
            row = list(map(int, input().split()))
            self.data[i] = row
    
    def transpose(self):
        result = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                result.data[i][j] = self.data[j][i]
        return result
    
    def multiply(self, other):
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                s = 0
                for z in range(self.m):
                    s += self.data[i][z] * other.data[z][j]
                result.data[i][j] = s
        return result
    
    def print_matrix(self):
        for i in range(self.n):
            print(' '.join(map(str, self.data[i])))


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    
    a = Matrix(n, m)
    a.input_matrix()
    
    a_transpose = a.transpose()
    
    result = a.multiply(a_transpose)
    
    result.print_matrix()