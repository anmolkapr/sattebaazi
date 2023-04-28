
V = 4


INF = 99999




def floydWarshall(graph):


	dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

	
	for k in range(V):

		for i in range(V):

			for j in range(V):

				dist[i][j] = min(dist[i][j],
								dist[i][k] + dist[k][j]
								)
	printSolution(dist)



def printSolution(dist):

	for i in range(V):
		for j in range(V):
			if(dist[i][j] == INF):
				print("%7s" % ("INF"), end=" ")
			else:
				print("%7d\t" % (dist[i][j]), end=' ')
			if j == V-1:
				print()



if __name__ == "__main__":
	graph = [[0, 10, 15, 20],
			[5, 0, 9, 10],
			[6, 13, 0, 12],
			[8, 8, 9, 0]
			]

	floydWarshall(graph)

