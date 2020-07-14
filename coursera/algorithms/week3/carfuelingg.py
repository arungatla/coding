# Python 3 program for finding the total 
# number of stops for refilling to reach 
# destination of N km 

# Function that returns the total number of 
# refills made to reach the destination of N km 
def countRefill(N, K, M, compulsory): 
	count = 0
	i = 0
	distCovered = 0

	# While we complete the whole journey. 
	while (distCovered < N): 
		
		# If must visited petrol pump lie 
		# between distCovered and distCovered+K. 
		if (i < M and compulsory[i] <= (distCovered + K)): 
			
			# make last mustVisited as distCovered 
			distCovered = compulsory[i] 

			# increment the index of 
			# compulsory visited. 
			i += 1

		# if no such must visited pump is 
		# there then increment distCovered by K. 
		else: 
			distCovered += K 

		# Counting the number of refill. 
		if (distCovered < N): 
			count += 1

	return count 

# Driver Code 
if __name__ == '__main__': 
	N = 4
	K = 500
	M = 200
	
	# compulsory petrol pumps to refill at 
	compulsory = [6, 7, 8] 

	# function call that returns the 
	# answer to the problem 
	print(countRefill(N, K, M, compulsory)) 
	
# This code is contributed by 
# Sanjit_Prasad 
