from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # Count total occurrences of each character
        freq = Counter(text)

        # Step 1: Build blocks (char, length)
        blocks = []
        current = text[0]
        length = 1
        for i in range(1, len(text)):
            if text[i] == current:
                length += 1
            else:
                blocks.append((current, length))
                current = text[i]
                length = 1
        blocks.append((current, length))  # append last group

        max_blocks = 0

        # Step 2: Try to extend each block by 1 (if there's extra char elsewhere)
        for i in range(len(blocks)):
            ch, l = blocks[i]
            if freq[ch] > l:
                max_blocks = max(max_blocks, l + 1)
            else:
                max_blocks = max(max_blocks, l)

        # Step 3: Try to merge two blocks separated by 1 different char
        for i in range(1, len(blocks) - 1):
            prev_ch, prev_len = blocks[i - 1]
            mid_ch, mid_len = blocks[i]
            next_ch, next_len = blocks[i + 1]

            if mid_len == 1 and prev_ch == next_ch:
                total = prev_len + next_len
                if freq[prev_ch] > total:
                    total += 1
                max_blocks = max(max_blocks, total)

        return max_blocks
