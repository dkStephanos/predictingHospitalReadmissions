import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder

class DataUtil(object):

    @staticmethod
    def setMissingValuesToNaN(dataFrame):
        dataFrame = dataFrame.replace('?', np.NaN)
        dataFrame = dataFrame.replace('None', np.NaN)
        dataFrame = dataFrame.replace('Not Available', np.NaN)
        dataFrame = dataFrame.replace('Not Mapped', np.NaN)

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
    def imputeMissingValues(dataFrame, numNeighbors, colsToImpute):
        labelencoder = LabelEncoder()
        imputer = KNNImputer(n_neighbors=numNeighbors)

        for col in colsToImpute:
            # Encodes categorical data
            dataFrame[col] = dataFrame[col].fillna('NaN')
            dataFrame[col] = labelencoder.fit_transform(dataFrame[col])
            imputer.fit(dataFrame[col].values.reshape(-1, 1))
            dataFrame[col] = imputer.transform(dataFrame[col].values.reshape(-1, 1))
        
        return dataFrame

    @staticmethod
    def setNaNValuesOfCol(dataFrame, col, value):
        dataFrame[col] = dataFrame[col].fillna(value)

        return dataFrame