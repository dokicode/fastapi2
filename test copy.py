import pandas as pd
import numpy as np
from typing import List,Dict



class DataFrameReader:
    def __init__(self, df):
        self._df = df
        self._row = None
        self._columns = df.columns.tolist()
        self.reset()
        self.row_index = 0

    def __getattr__(self, key):
        return self.__getitem__(key)

    def read(self) -> bool:
        self._row = next(self._iterator, None)
        self.row_index += 1
        return self._row is not None

    def columns(self):
        return self._columns

    def reset(self) -> None:
        self._iterator = self._df.itertuples()

    def get_index(self):
        return self._row[0]

    def index(self):
        return self._row[0]

    def to_dict(self, columns: List[str] = None):
        return self.row(columns=columns)

    def tolist(self, cols) -> List[object]:
        return [self.__getitem__(c) for c in cols]

    def row(self, columns: List[str] = None) -> Dict[str, object]:
        cols = set(self._columns if columns is None else columns)
        return {c : self.__getitem__(c) for c in self._columns if c in cols}

    def __getitem__(self, key) -> object:
        # the df index of the row is at index 0
        try:
            if type(key) is list:
                ix = [self._columns.index(key) + 1 for k in key]
            else:
                ix = self._columns.index(key) + 1
            return self._row[ix]
        except BaseException as e:
            return None

    def __next__(self) -> 'DataFrameReader':
        if self.read():
            return self
        else:
            raise StopIteration

    def __iter__(self) -> 'DataFrameReader':
        return self


filename = "test.csv"

# df= pd.DataFrame(np.random.randint(1, 100, size=(1000, 4)), columns=list('ABCD'))
# print(df)

# df.to_csv(filename)
# df.to_parquet('par')

df = pd.read_parquet('par')
print(len(df))
# for batch in pd.read_parquet('par', engine="fastparquet"):
# for batch in pd.read_parquet('par'):
#     pass

# print(df)

# for row in df.itertuples():
#     print(row)

# iterrow = DataFrameReader(df)


# print(next(iterrow).to_dict())
# print(next(iterrow).to_dict())
# print(next(iterrow).to_dict())

# print(iterrow.__next__().to_dict())
# print(iterrow.__next__().to_dict())
# print(iterrow.__next__().to_dict())
# print(iterrow.row_index)
# print(iterrow.__next__().to_dict())
# print(iterrow.__next__().to_dict())
# print(iterrow.__next__().to_dict())
# print(iterrow.row_index)

# iter = df.itertuples()
# iter = df.iterrows()
# value = next(iter)
# print(value[1]['A'])
# print(next(iter))
# print(next(iter))
# print(next(df))

class dfIterator:

    def __init__(self) -> None:
        pass
    
    def __iter__(self):
        return  self
    


class dfReader:

    def __init__(self, df, start=0, step=10) -> None:
        self._df = df
        # print(start+step)
        self.iter = df.iloc[start : start+step].itertuples()
        # self.iter = df.iloc[start : start+step].to_dict()
        print(self.iter)
        # self.iter = df.itertuples()
        self.columns = df.columns.tolist()
        self.start = start
        self.step = step


    # def to_dict(self, row):
    #     for col_name in self.columns:
    #         col_index = self.columns.index(col_name) + 1
    #         value = row[col_index]
    #         print(f"{col_name} : {value}")

    def next(self):
        data = []
        for i in self.iter:
            data.append(self.to_dict(i))
        return data

    def to_dict(self, row):
        index = row[0]
        data = {}
        for col_name in self.columns:
            col_index = self.columns.index(col_name) + 1
            value = row[col_index]
            data[col_name] = value
        rowData = {
            index : data
        }
        return rowData


    def __next__(self):
        # data = next(self.iter)
        # print('data', data)
        # print(self.columns.index('C'))
        # ff = pd.DataFrame(data).to_dict(orient='dict')
        # ff = data[self.columns.index('D')+1]
        # print(ff)
        row = next(self.iter)
        # print(self.columns)
        index = row[0]
        data = {}
        for col_name in self.columns:
            col_index = self.columns.index(col_name) + 1
            value = row[col_index]
            data[col_name] = value
        rowData = {
            index : data
        }

        # print(rowData)
            # print(f"{col_name} : {value}")
        # print(row[2])
        return rowData



iter = dfReader(df, start=10)

print(iter.next())
# value = next(iter)
# print(value)
# value = next(iter)
# print(value)
# value = next(iter)
# print(value)



# print(list(iter.columns))
# print(iter.columns.tolist())
# print(iter)
# print(pd.DataFrame((next(iter))).to_dict())