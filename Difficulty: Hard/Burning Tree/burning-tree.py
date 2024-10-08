#User function Template for python3

class Solution:
    def minTime(self, root,target):
        parent={}
        res=[root]
        while res:
            a=res.pop(0)
            if a.left:
                parent[a.left]=a
                res.append(a.left)
            if a.right:
                parent[a.right]=a
                res.append(a.right)
        queue=[]
        def inorder(root):
            if root and root.data==target:
               queue.append([root,0])
            else:
                if root:
                    inorder(root.left)
                    inorder(root.right)
        inorder(root)
        vis={queue[0][0]:1}
        maxi=0
        while queue:
            for i in range((len(queue))):
                a=queue.pop(0)
                node=a[0]
                count=a[1]
                maxi=max(maxi,count)
                if node in parent and parent[node] not in vis:
                    vis[parent[node]]=1
                    queue.append([parent[node],count+1])
                if node.left and node.left not in vis:
                    vis[node.left]=1
                    queue.append([node.left,count+1])
                if node.right and node.right not in vis:
                    vis[node.right]=1
                    queue.append([node.right,count+1])
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends