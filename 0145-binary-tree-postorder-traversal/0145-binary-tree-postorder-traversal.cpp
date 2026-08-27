#include <vector>
#include <algorithm>

class Solution {
public:
    // Helper function to handle recursion
    void traverse(TreeNode* node, std::vector<int>& result) {
        if (node == nullptr) return;
        
        traverse(node->left, result);   // 1. Visit Left
        traverse(node->right, result);  // 2. Visit Right
        result.push_back(node->val);    // 3. Visit Root
    }

    std::vector<int> postorderTraversal(TreeNode* root) {
        std::vector<int> result;
        traverse(root, result);
        return result;
    }
};
