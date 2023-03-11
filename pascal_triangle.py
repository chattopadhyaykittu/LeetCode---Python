class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        ps = [[1]]
        
        for i in range(numRows-1):
            print(ps)
            temp = [0] + ps[-1] + [0]
            print(temp)
            print(ps)
            print(ps[-1])
    
            row = []
            
            for j in range(len(ps[-1])+1):
                row.append(temp[j] + temp[j+1])
            
            ps.append(row)
        
        return ps
