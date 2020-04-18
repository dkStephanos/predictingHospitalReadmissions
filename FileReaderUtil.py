import pandas as pd

class FileReaderUtil(object):
    pass

@staticmethod
def getRawPatientData(filePath):
    RawPatientData = pd.read_csv(filePath)

    return RawPatientData


