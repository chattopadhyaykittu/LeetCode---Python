class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        length = 0
        curr = head

    # Calculate the length of the linked list
        while curr:
            length += 1
            curr = curr.next

    # Check if the number of rows and columns is valid
        if m * n < length:
            return None

    # Create an empty matrix with the desired number of rows and columns
        matrix = [[-1] * n for _ in range(m)]

    # Fill the matrix with the elements of the linked list
        cur = head
        x1, x2, y1, y2 = 0, m-1, 0, n-1

        while cur:
        # Fill the top row
            for i in range(y1, y2+1):
                if cur is None:
                    break
                matrix[x1][i] = cur.val
                cur = cur.next

        # Fill the right column
            for j in range(x1+1, x2+1):
                if cur is None:
                    break
                matrix[j][y2] = cur.val
                cur = cur.next

            if x1 < x2 and y1 < y2:
            # Fill the bottom row
                for i in range(y2-1, y1-1, -1):
                    if cur is None:
                        break
                    matrix[x2][i] = cur.val
                    cur = cur.next

            # Fill the left column
                for j in range(x2-1, x1, -1):
                    if cur is None:
                        break
                    matrix[j][y1] = cur.val
                    cur = cur.next

        # Update the indices
            x1 += 1
            x2 -= 1
            y1 += 1
            y2 -= 1

        return matrix
