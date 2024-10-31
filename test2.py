import pyarrow.parquet as pq
import pandas as pd
import numpy as np
# from typing import List,Dict


parquet_file = pq.ParquetFile('par')

# g = parquet_file.iter_batches(batch_size=400)
# print(g)
# data = next(g)
# print(data.to_pandas())
# data = next(g)
# print(data.to_pandas())
# data = next(g)
# print(data.to_pandas())
# data = next(g)
# print(data.to_pandas())


def getData():
    g = parquet_file.iter_batches(batch_size=400)

    for batch in g:
        yield batch.to_pandas()


# for batch in parquet_file.iter_batches(batch_size=200):
#     batch_df = batch.to_pandas()
#     print(batch_df)

def getBatch(iter):
    try:
        return next(iter)
    except StopIteration:
        pass

def full(iter):
    return [batch for batch in iter]


# iter = getData()
# print(id(iter))
# print(iter)
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
iter = getData()



print(getBatch(iter))
print(getBatch(iter))

print('full')
print(full(iter))
# print(getBatch(iter))
# print(getBatch(iter))