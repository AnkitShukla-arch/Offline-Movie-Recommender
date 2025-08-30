from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

def load_data(filepath='data/ml-100k/u.data'):
    reader = Reader(line_format='user item rating timestamp', sep='\t')
    return Dataset.load_from_file(filepath, reader=reader)

def train_model(data):
    trainset, testset = train_test_split(data, test_size=0.2)
    algo = SVD()
    algo.fit(trainset)
    predictions = algo.test(testset)
    rmse = accuracy.rmse(predictions)
    return algo, predictions, rmse
