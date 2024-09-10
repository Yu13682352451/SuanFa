#include <iostream>
#include <vector>
#include <climits>  // INT_MIN、INT_MAX
#include <cctype>  // isdigit、isalpha
#include <algorithm>  // sort

class Solution{
public:
    // 分而治之思想 求和
    int dc_sum(std::vector<int> nums){
        if (nums.empty()) return 0;
        else if (nums.size() == 1) return nums[0];
        else return nums[0] + dc_sum(std::vector<int>(nums.begin() + 1, nums.end()));
    }
    // 分而治之思想 求最大值
    int dc_max(std::vector<int> nums, int index=0, int current_max=INT_MIN){
        if (index == nums.size()) return current_max;
        if (nums[index] > current_max) current_max = nums[index];
        return dc_max(nums, index+1, current_max);
    }
    // 双指针 力扣125.验证回文字符串
    static bool isPalindrome(std::string s){
        bool palindrome = true;
        std::string cs = cleanString(s);
        for (int i = 0; i<cs.size(); i++){
            if (cs[i] != cs[cs.size()-i-1]){
                palindrome = false;
                break;
            }
        }
        return palindrome;
    }
    // 上面实现的辅助函数
    static std::string cleanString(const std::string& s){
        std::string result;
        for (char c : s){
            if(std::isalnum(c)) result += std::tolower(c);
        }
        return result;
    }
    // 滑动窗口，找出数组中满足其总和大于等于 target 的长度最小的子数组，力扣209.长度最小的子数组
    static int minSubArrayLen(int target, std::vector<int>& nums){
        int ans = INT_MAX;
        int sum = 0;
        for(int i=0,j=0; i<nums.size(); i++){
            sum += nums[i];
            while(sum >= target){
                ans = std::min(ans, i-j+1);
                sum -= nums[j++];
            }
        }
        return ans==INT_MAX ? 0 : ans;
    }
    // 动态规划思想 求最长公共子串
    static std::string dp_longestCommomSubstring(const std::string& str1, const std::string& str2){
        size_t len1 = str1.size();
        size_t len2 = str2.size();

        // 创建一个二维数组用于存储动态规划状态
        std::vector<std::vector<int>> dp(len1+1, std::vector<int>(len2+1, 0));

        int maxLength = 0; // 用于存储最长公共子串的长度
        int endIndex = 0; // 用于记录最长公共字串在str1中结束的位置

        // 遍历每个字符对
        for (int i = 1; i < len1; i++){
            for (int j = 1; j < len2; j++){
                if (str1[i-1]==str2[j-1]){
                    dp[i][j] = dp[i-1][j-1] + 1;
                    if (dp[i][j] > maxLength){
                        maxLength = dp[i][j];
                        endIndex = i; // 更新最长公共子串的结束位置
                    }
                }
            }
        }

        return str1.substr(endIndex-maxLength, maxLength);
    }
    // 力扣每日一题 2860.让所有学生保持开心的分组方法数
    static int countWay(std::vector<int>& nums){
        int ans = 0;
        std::sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] >= i + 1) continue;
            if(i < nums.size()-1 && nums[i+1] <= i + 1) continue;
            ans++;
        }
        return ans;
    }


};

int main() {
    Solution s;
    std::vector<int> nums = {6,0,3,3,6,7,2,7};
    std::string str = "A man, a plan, a canal: Panama";
    std::cout << s.countWay(nums) << std::endl;
    return 0;
}
