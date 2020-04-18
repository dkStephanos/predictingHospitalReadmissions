from DriverHelper import DriverHelper
from FileReaderUtil import FileReaderUtil
from DataUtil import DataUtil

if __name__ == '__main__':

    # --- Preprocessing ---
    rawPatientDF = DriverHelper.getRawPatientDF()
    DriverHelper.printRawData(rawPatientDF)
    rawPatientDF = DataUtil.setMissingValuesToNaN(rawPatientDF)
    nanStats = DataUtil.getNaNStats(rawPatientDF)
    rawPatientDF = DataUtil.dropDirtyCols(rawPatientDF, ['weight', 'payer_code', 'medical_specialty', 'max_glu_serum', 'A1Cresult', 'diag_1_desc', 'diag_2_desc', 'diag_3_desc'])
    cleanPatientDF = DataUtil.imputeMissingValues(rawPatientDF, 3)

    print("fuck")