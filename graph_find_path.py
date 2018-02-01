test = {'a':['b','c','f'],
		'b':['c','d'],
		'c':['b','d','e'],
		'd':['b','c'],
		'e':['c'],
		'f':['a'],
		'g':['a','b','c']
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

def find_all_path(graph, start, end, path = []):
	# backtracking algorithm
	path = path + [start]
	if start == end:
		return [path]
	if start not in graph:
		return None
	paths = []
	for node in graph[start]:
		if node not in path: #no cycles
			#partial solution
			newpaths = find_path(graph,node,end,path)
		if newpaths:
			for newpath in newpaths:
				paths.append(newpaths) 
	return paths

def shortest_path(graph, start, end, path = []):
	# backtracking algorithm
	path = path + [start]
	if start == end:
		return [path]
	if start not in graph:
		return None
	paths = []
	for node in graph[start]:
		if node not in path: #no cycles
			#partial solution
			newpaths = find_path(graph,node,end,path)
		if newpaths:
			for newpath in newpaths:
				paths.append(newpaths) 
	if len(paths)>1:
		len_li = []
		for li in paths:
			len_li.append(len(li))
		return paths[len_li.index(min(len_li))]

	return paths

if __name__ == "__main__":
	print(find_path(test,'a','f'))
	print(find_all_path(test,'a','d'))
	print(shortest_path(test,'a','d'))