def distance(a, b):
    return sum([(ai-bi)**2 for ai, bi in zip(a,b)])**.5


def knn_dump(new_data, data, y):
    return y[0]

def knn_verbose(new_data, data, y, k=1):
    dists = [distance(new_data, p) for p in data]
    print(dists)
    idx = sorted(range(len(data)), key=lambda x: distance(new_data, data[x]))
    print(idx)
    for i in idx[:k]:
        print(i, dists[i], y[i], data[i])
    votes = [y[i] for i in idx[:k]]
    print(votes[0], votes.count(votes[0]))
    result = max(votes, key=votes.count)
    print(result)
    return result

def knn(new_data, data, y, k=1):
    idx = sorted(range(len(data)), key=lambda x: distance(new_data, data[x]))
    votes = [y[i] for i in idx[:k]]
    return max(votes, key=votes.count)

if __name__=='__main__':
    data = [[1, 2], 
        [2, 4],
        [3, 5],
        [2, 8],
        [4, 2]]
    
    y = [0, 1, 1, 0, 0]
    
    new_data = [1, 2.5]
    assert(knn(new_data, data, y, k=1) == 0)
    assert(knn(new_data, data, y, k=5) == 0)

    new_data = [1, 4.5]
    assert(knn(new_data, data, y, k=1) == 1)
    assert(knn(new_data, data, y, k=5) == 0)