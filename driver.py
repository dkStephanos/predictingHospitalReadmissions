from DriverHelper import DriverHelper
from FileReaderUtil import FileReaderUtil
from DataUtil import DataUtil
from PatternUtil import PatternUtil

if __name__ == '__main__':

    # --- Preprocessing ---
    #rawPatientDF = DriverHelper.getRawPatientDF()
    #cleanPatientDF = DriverHelper.cleanRawData(rawPatientDF)

    # --- Pattern Mining ---
    cleanPatientDF = DriverHelper.getCleanPatientDF()
    patterns = PatternUtil.getPatterns(cleanPatientDF)

    print("fuck")