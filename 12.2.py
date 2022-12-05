def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node.isupper():
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                    paths.append(newpath)
        else:
            if max( path.count(val) for val in path if val.islower() ) == 1:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)                    
            elif node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
    return paths

if __name__ == "__main__":

    with open('caves.txt') as f:
        lines = [ x.strip().split('-') for x in f.readlines()]

    caves = []

    for a in lines:
            for b in a:
                if b not in caves and b != 'end':
                    caves.append(b)

    grid = {}

    for b in caves:
        gridpaths = []
        for a in lines:
            if b == a[0]:
                if a[1] != 'start':
                    gridpaths.append(a[1])
            elif b == a[1]:
                if a[0] != 'start':
                    gridpaths.append(a[0])
        grid[b] = gridpaths

    all = find_all_paths(grid,'start','end')
    print('len: ', len(all))