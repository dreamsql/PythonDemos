

class TreeNode(object):

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):

	def __init__(self):
		self.result = 0

	def findTilt(self,root):		
		self.do_find_tilt(root)
		return self.result


	def do_find_tilt(self, root):
		if root == None: 
			return 0
		tl = self.do_find_tilt(root.left)
		tr = self.do_find_tilt(root.right)
		self.result += abs(tl - tr) 
		return tl + tr + root.val



def build_1_2_3_4_5_tree():
	lf4 = TreeNode(4)
	lf5 = TreeNode(5)
	lf2 = TreeNode(2)
	lf2.left = lf4
	lf3 = TreeNode(3)
	lf3.right = lf5
	lf1 = TreeNode(1)
	lf1.left = lf2
	lf1.right = lf3
	return lf1




if __name__ == '__main__':	
	leaf1 = TreeNode(1)
	leaf2 = TreeNode(2)
	leaf3 = TreeNode(3)
	leaf1.left = leaf2
	leaf1.right = leaf3
	sol = Solution()
	print(sol.findTilt(build_1_2_3_4_5_tree()))