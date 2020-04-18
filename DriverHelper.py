from FileReaderUtil import FileReaderUtil
from DataUtil import DataUtil

class DriverHelper(object):
    
    @staticmethod
    def getRawPatientDF():
        return FileReaderUtil.getRawPatientData('10kPatients.csv')

    @staticmethod
    def getRawPatientDF():
        return FileReaderUtil.getRawPatientData('cleanPatientDF.csv')
    
    @staticmethod
    def printRawData(rawData):
        print('\nRaw Patient Data Head:\n {0}'.format(rawData.head()))
        print('\nRaw Patient Data Tail:\n {0}'.format(rawData.tail()))

    @staticmethod
    def cleanRawData(rawPatientDF):
        rawPatientDF = DataUtil.convertNumericCols(rawPatientDF)
        rawPatientDF = DataUtil.setMissingValuesToNaN(rawPatientDF)
        rawPatientDF = DataUtil.dropDirtyCols(rawPatientDF, ['weight', 'payer_code', 'medical_specialty', 'max_glu_serum', 'A1Cresult', 'diag_1_desc', 'diag_2_desc', 'diag_3_desc'])
        rawPatientDF = DataUtil.setNaNValuesOfCol(rawPatientDF, 'race', 'Other')
        rawPatientDF = DataUtil.imputeMissingValues(rawPatientDF, 3, ['admission_type_id', 'discharge_disposition_id', 'admission_source_id'])
        cleanPatientDF = DataUtil.trimOutliersBySTD(rawPatientDF, 4)
        
        cleanPatientDF.to_csv('cleanPatientDF.csv')

        return cleanPatientDF