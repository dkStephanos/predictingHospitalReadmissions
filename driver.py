from DriverHelper import DriverHelper
from FileReaderUtil import FileReaderUtil

if __name__ == '__main__':
    rawPatientDF = DriverHelper.getRawPatientDF()
    DriverHelper.printRawData(rawPatientDF)