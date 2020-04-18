import pandas as pd

class FileReaderUtil(object):

    @staticmethod
    def getRawPatientData(filePath):
        RawPatientData = pd.read_csv(filePath)

        return RawPatientData


