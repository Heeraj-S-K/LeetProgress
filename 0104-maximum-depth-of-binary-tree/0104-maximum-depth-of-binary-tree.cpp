class Solution {
public:
    int maxDepth(TreeNode* root) {
        // Base case: If the node is empty, depth is 0
        if (root == nullptr) {
            return 0;
        }
        
        // Recursively find the depth of left and right subtrees
        int leftDepth = maxDepth(root->left);
        int rightDepth = maxDepth(root->right);
        
        // The depth of the current node is 1 + the max of its children
        return 1 + std::max(leftDepth, rightDepth);
    }
};
