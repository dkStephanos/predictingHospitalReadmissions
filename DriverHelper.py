from FileReaderUtil import FileReaderUtil

class DriverHelper(object):
    
    @staticmethod
    def getRawPatientDF():
        return FileReaderUtil.getRawPatientData('10kPatients.csv')