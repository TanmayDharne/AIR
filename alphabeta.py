MAX, MIN = 1000, -1000

#Returns optimal value of player
#Initially called for root and maximizer
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
	#Terminating condition that is leaf node is reached
	if depth == 3:
		return values[nodeIndex]
	
	if maximizingPlayer:
		best = MIN
		
		#Recur for left and right children
		for i in range(0,2):
			val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
			best = max(best, val)
			alpha = max(alpha, best)
			
			if beta <= alpha:
				break
		
		return best
	else:
		best = MAX
		
		#Recure for left and right children
		for i in range(0,2):
			val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
			best = min(best, val)
			beta = min(beta, best)
			
			if beta <= alpha:
				break
		return best
		
#Driver Code
if __name__ == "__main__":
	values = []
	n = int(input("Enter the no. of values you wanna enter : ")) 
	for i in range(0,n):
		x = int(input("Enter value : "))
		values.append(x)  
	print('The optimal value is :', minimax(0, 0, True, values, MIN, MAX))  