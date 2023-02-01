class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        p1 = 0
        p2 = 0
        cnt = 0
        while p2 < k:
            if blocks[p2] == "W":
                cnt += 1
            p2 += 1
        min_cnt = cnt
        while p2 < len(blocks):
            if blocks[p1] == "W":
                cnt -= 1
            if blocks[p2] == "W":
                cnt += 1
            p1 += 1
            p2 += 1

            min_cnt = min(min_cnt,cnt)
        return min_cnt