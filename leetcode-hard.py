# 3614. Process String with Special Operations II

class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        length = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                length += 1
            elif ch == '*':
                if length:
                    length -= 1
            elif ch == '#':
                length *= 2
            elif ch == '%':
                pass

            lengths.append(length)

        if k >= length:
            return "."

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            cur_len = lengths[i]

            if ch == '%':
                k = cur_len - 1 - k

            elif ch == '#':
                prev_len = cur_len // 2
                if k >= prev_len:
                    k -= prev_len

            elif ch == '*':
                pass

            else:  
                prev_len = lengths[i - 1] if i > 0 else 0
                if k == prev_len:
                    return ch

        return "."