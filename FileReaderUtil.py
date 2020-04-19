import pandas as pd

class FileReaderUtil(object):

    @staticmethod
    def getDataFromPath(filePath):
        dataFrame = pd.read_csv(filePath)

        return dataFrame


