import pandas as pd
import numpy as np

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