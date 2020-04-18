from FileReaderUtil import FileReaderUtil

class DriverHelper(object):
    
    @staticmethod
    def getRawPatientDF():
        return FileReaderUtil.getRawPatientData('10kPatients.csv')
    
    @staticmethod
    def printRawData(rawData):
        print('\nRaw Patient Data Head:\n {0}'.format(rawData.head()))
        print('\nRaw Patient Data Tail:\n {0}'.format(rawData.tail()))