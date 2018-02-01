test = {'a':['b','c'],
		'b':['c','d'],
		'c':['b','d','e'],
		'd':['b','c'],
		'e':['c'],
		'f':['a']
}

def find_path(graph, start, end, path = []):
	# backtracking algorithm
	if start == end:
		return path
	if start not in graph:
		return None
	path = path + [start]
	for node in graph[start]:
		if node not in path: #no cycles
			#partial solution
			newpath = find_path(graph,node,end,path)
			if newpath: return newpath
	return None

if __name__ == "__main__":
	print(find_path(test,'a','f'))