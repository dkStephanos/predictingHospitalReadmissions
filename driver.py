from DriverHelper import DriverHelper
from FileReaderUtil import FileReaderUtil
from DataUtil import DataUtil

if __name__ == '__main__':

    # --- Preprocessing ---
    rawPatientDF = DriverHelper.getRawPatientDF()
    cleanPatienDF = DriverHelper.cleanRawData(rawPatientDF)



    print("fuck")