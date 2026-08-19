from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # prep to helo w boundary checks later
        num_rows = len(image)
        num_cols = len(image[0])
        # helper func to find adjacent pixels
        def get_neighbors(coord, prev):
            row, col = coord #iterable unpacking of coord argument
            # move down, move right, move up, move left
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0<= neighbor_col < num_cols:
                    if image[neighbor_row][neighbor_col] == prev:
                        yield (neighbor_row, neighbor_col) 
                        # yield gives you all the neighboring coords, return would have stopped after one coord

        # func to actually change pixel colors
        def bfs(root):
            # initilizing queue
            queue = deque([root]) 
            # create a visited grid same size as the image to remove duplicate visits, grids can loop back
            visited = [[False for c in range(num_cols)] for r in range(num_rows)]
            sr, sc = root #iterable unpacking: assigns sr and sc to the coords of root
            prev = image[sr][sc] #saves previous color to find neighbors
            image[sr][sc] = color #changes root color to kick off flood fill
            #BFS LOOP STARTS HERE
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in get_neighbors(node, prev): #able to do this becuase we used yield
                    r, c = neighbor
                    if visited[r][c]:
                        continue
                    image[r][c] = color
                    queue.append(neighbor) #adds neighboring pixels to queue so it can get their neghbors in the BFS LOOP
                    visited[r][c] = True

        bfs((sr, sc))
        return image



        
            
        