from typing import List


class Solution:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        """滑动窗口 力扣 3.无重复字符串的最长子串"""
        result = 0
        sub_str = ""
        i = 0
        for j in range(len(s)):
            while s[j] in sub_str:
                sub_str = sub_str[1:]
                i += 1
            sub_str += s[j]
            result = max(result, j - i + 1)
        return result

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """数组题 力扣36.有效的数独"""
        row_index = [[0 for i in range(9)] for j in range(9)]
        col_index = [[0 for i in range(9)] for j in range(9)]
        sudoku_index = [[[0 for i in range(9)] for j in range(3)] for k in range(3)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                row_index[row][int(board[row][col]) - 1] += 1
                col_index[col][int(board[row][col]) - 1] += 1
                sudoku_index[int(row / 3)][int(col / 3)][int(board[row][col]) - 1] += 1
                if (row_index[row][int(board[row][col]) - 1] > 1 or col_index[col][int(board[row][col]) - 1] > 1 or
                        sudoku_index[int(row / 3)][int(col / 3)][int(board[row][col]) - 1] > 1):
                    return False

        return True

    def romanToInt(self, s: str) -> int:
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            value = roman_dict[s[i]]
            if i < len(s) - 1 and value < roman_dict[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """贪婪算法 力扣 134.加油站"""
        start_station, i = 0, 0
        num_stations = len(gas)
        while i < num_stations:
            sum_gas, cost_gas = 0, 0
            cnt = 0
            while cnt < num_stations:
                cur_station = (cnt + i) % num_stations
                sum_gas += gas[cur_station]
                cost_gas += cost[cur_station]
                if sum_gas < cost_gas:
                    break
                cnt += 1
            if cnt == num_stations:
                return i
            else:
                i = i + cnt + 1

        return -1

    def maxStrength(self, nums: List[int]) -> int:
        """力扣每日一题 2708.一个小组的最大实力值"""
        ans = 1
        nums.sort()
        num_neg = 0
        if len(nums) == 1:
            return nums[1]
        for i in range(len(nums)):
            if nums[i] < 0:
                num_neg += 1
        if num_neg == 1 and nums[-1] == 0 or num_neg == 0 and nums[-1] == 0:
            return 0
        if num_neg % 2:
            for i in range(num_neg - 1):
                ans *= nums[i]
        else:
            for i in range(num_neg):
                ans *= nums[i]
        for i in range(num_neg, len(nums)):
            if nums[i] == 0:
                continue
            ans *= nums[i]

        return ans


        return ans

    def clearDigits(self, s: str) -> str:
        """力扣每日一题 3174.清除数字"""
        ans = ""
        i = 0
        while i < len(s) - 1:
            if i <= len(s) - 2 and s[i].isalpha() and s[i+1].isnumeric():
                i += 2
                continue
            if s[i].isnumeric():
                ans = ans[:-1]
                i += 1
                continue
            ans += s[i]
            i += 1

        return ans

    def rob(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    s = Solution()
    ans = s.clearDigits("ag3")
    print(ans)
