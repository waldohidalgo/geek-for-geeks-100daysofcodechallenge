class Solution:
    def kBitFlips(self, arr, k):
        # code here
        n = len(arr)
        flip = 0
        res = 0
        is_flipped = [0] * n

        for i in range(n):
            if i >= k:
                flip ^= is_flipped[i - k]

            if arr[i] ^ flip == 0:
                if i + k > n:
                    return -1
                flip ^= 1
                is_flipped[i] = 1
                res += 1

        return res