import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

class DataUtil(object):

    @staticmethod
    def setMissingValuesToNaN(dataFrame):
        dataFrame = dataFrame.replace('?', np.NaN)
        dataFrame = dataFrame.replace('None', np.NaN)

        return dataFrame

    @staticmethod
    def getNaNStats(dataFrame):
        print("\nTotal NaN count for each column:")
        isNaNperCol = dataFrame.isna().sum()
        print(isNaNperCol.to_string())

        print("\nPercentage of NaN values:")
        percentageNaN = isNaNperCol.sum()/(len(dataFrame)*len(dataFrame.columns))
        print(percentageNaN)

        return [isNaNperCol, percentageNaN]

    @staticmethod
    def dropDirtyCols(dataFrame, colsToDrop):
        dataFrame = dataFrame.drop(colsToDrop, axis=1)

        return dataFrame

    @staticmethod
    def imputeMissingValues(dataFrame, numNeighbors):
        imputer = KNNImputer(n_neighbors=numNeighbors)

        dataFrameFilled = imputer.fit_transform(dataFrame)
        
        return dataFrame

    @staticmethod
    def setNaNValuesOfCol(dataFrame, col, value):
        dataFrame = dataFrame[col].fillna(value)

        return dataFrame