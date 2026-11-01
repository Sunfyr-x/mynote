下面把前面那批「408 经典算法题」对应到 LeetCode（力扣中国 leetcode.cn）题号，按类别整理成表。  
（注：408 大题偏「写伪代码+复杂度」，LeetCode 偏「能跑通代码」，思路完全通用）

## 一、数组 / 字符串

408 经典题 对应 LeetCode 链接

数组循环左移（三次逆置） 189 轮转数组 https://leetcode.cn/problems/rotate-array/

数组去重（双指针） 26 删除有序数组重复项 https://leetcode.cn/problems/remove-duplicates-from-sorted-array/

两有序数组合并 88 合并两个有序数组 https://leetcode.cn/problems/merge-sorted-array/

有序数组找两数之和 1 两数之和 / 167 两数之和II https://leetcode.cn/problems/two-sum/

第 k 大 / topK（快排划分） 215 数组第K大 https://leetcode.cn/problems/kth-largest-element-in-an-array/

螺旋矩阵遍历 54 螺旋矩阵 https://leetcode.cn/problems/spiral-matrix/

矩阵旋转 90° 48 旋转图像 https://leetcode.cn/problems/rotate-image/

二分查找 704 二分查找 https://leetcode.cn/problems/binary-search/
## 二、链表
408 经典题 对应 LeetCode 链接

反转链表 206 反转链表 https://leetcode.cn/problems/reverse-linked-list/

局部反转 92 反转链表II https://leetcode.cn/problems/reverse-linked-list-ii/

K 个一组反转 25 K个一组翻转链表 https://leetcode.cn/problems/reverse-nodes-in-k-group/

删除倒数第 k 个 19 删除链表的倒数第N个节点 https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

判环 141 环形链表 https://leetcode.cn/problems/linked-list-cycle/

找环入口 142 环形链表II https://leetcode.cn/problems/linked-list-cycle-ii/

找中点 876 链表的中间结点 https://leetcode.cn/problems/middle-of-the-linked-list/

回文链表 234 回文链表 https://leetcode.cn/problems/palindrome-linked-list/

合并两有序链表 21 合并两个有序链表 https://leetcode.cn/problems/merge-two-sorted-lists/

合并 K 个有序链表 23 合并K个升序链表 https://leetcode.cn/problems/merge-k-sorted-lists/

相交链表 160 相交链表 https://leetcode.cn/problems/intersection-of-two-linked-lists/

重排链表 143 重排链表 https://leetcode.cn/problems/reorder-list/

循环右移链表 61 旋转链表 https://leetcode.cn/problems/rotate-list/
## 三、树 / 二叉树
408 经典题 对应 LeetCode 链接

先/中/后序遍历 144 / 94 / 145 https://leetcode.cn/problems/binary-tree-inorder-traversal/

层序遍历 102 二叉树的层序遍历 https://leetcode.cn/problems/binary-tree-level-order-traversal/

前序+中序重建 105 从前序与中序构造二叉树 https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

中序+后序重建 106 从中序与后序构造二叉树 https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

验证 BST 98 验证二叉搜索树 https://leetcode.cn/problems/validate-binary-search-tree/

最近公共祖先 236 二叉树的最近公共祖先 https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

最大深度 104 二叉树的最大深度 https://leetcode.cn/problems/maximum-depth-of-binary-tree/
## 四、图 / 408 常考算法
408 经典题 对应 LeetCode 链接

拓扑排序（判环） 207 课程表 https://leetcode.cn/problems/course-schedule/

拓扑排序（输出序列） 210 课程表II https://leetcode.cn/problems/course-schedule-ii/

单源最短路 Dijkstra 743 网络延迟时间 https://leetcode.cn/problems/network-delay-time/

最小生成树 Prim/Kruskal 1584 连接所有点的最小费用 https://leetcode.cn/problems/min-cost-to-connect-all-points/

DFS/BFS 连通块 200 岛屿数量 https://leetcode.cn/problems/number-of-islands/
五、排序 / 综合
408 经典题 对应 LeetCode 链接

手撕快排 912 排序数组 https://leetcode.cn/problems/sort-an-array/

手撕归并 912（同上） 同上

LRU 缓存（哈希+双向链表） 146 LRU缓存 https://leetcode.cn/problems/lru-cache/

用栈实现队列 232 用栈实现队列 https://leetcode.cn/problems/implement-queue-using-stacks/

刷题建议（对接 408）

• 先刷「原子操作」：206、876、234、105、207、189、54

• 再刷「组合题」：143（中点+反转+合并）、234（中点+反转+双指针）

- 408 大题写法：LeetCode 写可运行代码，考场上删细节、留伪代码+边界+复杂度

要不要我按“408 大题出现频率”给你排一个 20 题精简刷题顺序，并标出每题必背的伪代码模板？