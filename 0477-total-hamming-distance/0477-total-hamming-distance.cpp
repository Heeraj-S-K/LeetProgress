class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int total_distance = 0;
        int n = nums.size();
        
        // Loop through all 32 possible bit positions for integers
        for (int i = 0; i < 32; ++i) {
            int bit_count = 0;
            
            // Count how many elements have the i-th bit set to 1
            for (int num : nums) {
                if ((num >> i) & 1) {
                    bit_count++;
                }
            }
            
            // Elements with '1' at bit i: bit_count
            // Elements with '0' at bit i: n - bit_count
            total_distance += bit_count * (n - bit_count);
        }
        
        return total_distance;
    }
};
