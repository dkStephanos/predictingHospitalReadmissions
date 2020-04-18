from DriverHelper import DriverHelper
from FileReaderUtil import FileReaderUtil
from DataUtil import DataUtil

if __name__ == '__main__':

    # --- Preprocessing ---
    rawPatientDF = DriverHelper.getRawPatientDF()
    rawPatientDF = DataUtil.convertNumericCols(rawPatientDF)
    rawPatientDF = DataUtil.setMissingValuesToNaN(rawPatientDF)
    rawPatientDF = DataUtil.dropDirtyCols(rawPatientDF, ['weight', 'payer_code', 'medical_specialty', 'max_glu_serum', 'A1Cresult', 'diag_1_desc', 'diag_2_desc', 'diag_3_desc'])
    rawPatientDF = DataUtil.setNaNValuesOfCol(rawPatientDF, 'race', 'Other')
    DataUtil.getNaNStats(rawPatientDF)
    rawPatientDF = DataUtil.encodeCategoricalCols(rawPatientDF)
    rawPatientDF = DataUtil.imputeMissingValues(rawPatientDF, 3, ['admission_type_id', 'discharge_disposition_id', 'admission_source_id'])
    rawPatientDF.to_csv('rawPatientDF.csv')
    cleanPatientDF = DataUtil.trimOutliersBySTD(rawPatientDF, 4)
    nanStats = DataUtil.getNaNStats(cleanPatientDF)
    print('Shape of clean dataframe: {0}'.format(cleanPatientDF.shape))

    print("fuck")