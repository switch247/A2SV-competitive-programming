class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
            matrix = [[0] * n for _ in range(m)]
            # mark guards and walls
            for guard in guards: matrix[guard[0]][guard[1]] = "G"
            for wall in walls: matrix[wall[0]][wall[1]] = "W"

            # mark all spots guards see
            for i in range(m):
                seen_guard = False
                # -> search right
                for j in range(n):
                    if matrix[i][j] == "G":
                        seen_guard = True
                    elif matrix[i][j] == "W":
                        seen_guard = False
                    elif seen_guard:
                        matrix[i][j] = "x"

                seen_guard = False
                # <- search left
                for j in range(n - 1, -1, -1):
                    if matrix[i][j] == "G":
                        seen_guard = True
                    elif matrix[i][j] == "W":
                        seen_guard = False
                    elif seen_guard:
                        matrix[i][j] = "x"

            for i in range(n):
                seen_guard = False
                # search down
                for j in range(m):
                    if matrix[j][i] == "G":
                        seen_guard = True
                    elif matrix[j][i] == "W":
                        seen_guard = False
                    elif seen_guard:
                        matrix[j][i] = "x"

                seen_guard = False
                # ^ search up 
                for j in range(m - 1, -1, -1):
                    if matrix[j][i] == "G":
                        seen_guard = True
                    elif matrix[j][i] == "W":
                        seen_guard = False
                    elif seen_guard:
                        matrix[j][i] = "x"

            count = 0
            # 0's are available spots
            for i in range(m):
                count += matrix[i].count(0)
                
            return count