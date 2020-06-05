import knn

data = [[1, 2], 
    [2, 4],
    [3, 5],
    [2, 8],
    [4, 2]]

y = [0, 1, 1, 0, 0]

def test_knn1():
    new_data = [1, 2.5]
    assert(knn.knn(new_data, data, y, k=1) == 0)

def test_knn2():
    new_data = [1, 2.5]
    assert(knn.knn(new_data, data, y, k=5) == 0)

def test_knn3():
    new_data = [1, 4.5]
    assert(knn.knn(new_data, data, y, k=1) == 1)

def test_knn4():
    new_data = [1, 4.5]
    assert(knn.knn(new_data, data, y, k=5) == 0)
