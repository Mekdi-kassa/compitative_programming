class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def inbound(row , col):
            if 0 <= row < len(image) and 0 <= col < len(image[0]):
                return True

        que = deque([])
        que.append((sr,sc))
        seen = set()
        seen.add((sr , sc))
        org = image[sr][sc]
        dir1 = [(1,0),(-1,0),(0,-1),(0,1)]
        while que:
            q_len = len(que)
            for _ in range(q_len): 
                x , y = que.popleft()
                if image[x][y] != color:
                    image[x][y] = color
                for r , c in dir1:
                    newr = r + x
                    newc = c + y
                    if inbound(newr , newc)  and (newr , newc) not in seen and image[newr][newc] == org:
                        seen.add((newr , newc))
                        que.append((newr , newc))
        return image