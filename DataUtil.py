import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder

class DataUtil(object):

    @staticmethod
    def setMissingValuesToNaN(dataFrame):
        dataFrame = dataFrame.replace('?', np.NaN)
        dataFrame = dataFrame.replace('None', np.NaN)
        dataFrame = dataFrame.replace('Not Available', np.NaN)
        dataFrame = dataFrame.replace('Not Mapped', np.NaN)

        return dataFrame

    @staticmethod
    def getNaNStats(dataFrame):
        print("\nTotal NaN count for each column:")
        isNaNperCol = dataFrame.isna().sum()
        print(isNaNperCol.to_string())

        print("\nPercentage of NaN values:")
        percentageNaN = isNaNperCol.sum()/(len(dataFrame)*len(dataFrame.columns))
        print(percentageNaN)

        return [isNaNperCol, percentageNaN]

    @staticmethod
    def dropDirtyCols(dataFrame, colsToDrop):
        dataFrame = dataFrame.drop(colsToDrop, axis=1)

        return dataFrame

    @staticmethod
    def convertNumericCols(dataFrame):
        numeric_cols = ['time_in_hospital', 'num_lab_procedures', 'num_medications', 'number_outpatient', 'number_emergency', 
                        'number_inpatient', 'number_diagnoses']
        dataFrame[numeric_cols] = dataFrame[numeric_cols].apply(pd.to_numeric)

        return dataFrame

    @staticmethod
    def encodeCategoricalCols(dataFrame):

        categorical_cols = ['race', 'gender', 'age', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id', 
                            'metaformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'acetohexamide', 
                            'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 
                            'troglitazone', 'tolazamide', 'examide', 'citoglipton', 'insulin', 'glyburide.metformin', 'glipizide.metformin',
                            'glimepiride.pioglitazone', 'metformin.rosiglitazone', 'metformin.pioglitazone', 'change', 'diabetesMed', 'diag_1', 'diag_2', 'diag_3']
        le = LabelEncoder()
        # apply le on categorical feature columns
        dataFrame[categorical_cols] = dataFrame[categorical_cols].apply(lambda col: le.fit_transform(col))

        return dataFrame

    @staticmethod
    def imputeMissingValues(dataFrame, numNeighbors, colsToImpute):
        imputer = KNNImputer(n_neighbors=numNeighbors)

        for col in colsToImpute:
            dataFrame[col] = imputer.transform(dataFrame[col].values.reshape(-1, 1))
        
        return dataFrame

    @staticmethod
    def setNaNValuesOfCol(dataFrame, col, value):
        dataFrame[col] = dataFrame[col].fillna(value)

        return dataFrame

    @staticmethod
    def trimOutliersBySTD(dataFrame, factor):
        for col in dataFrame.iloc[:,1:]:
            upper_lim = dataFrame[col].mean () + dataFrame[col].std () * factor
            lower_lim = dataFrame[col].mean () - dataFrame[col].std () * factor
            dataFrame = dataFrame[(dataFrame[col] < upper_lim) & (dataFrame[col] > lower_lim)]

        return dataFrame