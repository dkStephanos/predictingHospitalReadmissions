import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

class PatternUtil(object):
   
    @staticmethod
    def getPatterns(dataFrame):
        le = LabelEncoder()
        categorical_cols = ['race', 'gender', 'age', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id', 
                            'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 'acetohexamide', 
                            'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 
                            'troglitazone', 'tolazamide', 'examide', 'citoglipton', 'insulin', 'glyburide.metformin', 'glipizide.metformin',
                            'glimepiride.pioglitazone', 'metformin.rosiglitazone', 'metformin.pioglitazone', 'change', 'diabetesMed', 'diag_1', 'diag_2', 'diag_3', 'readmitted']

        # Encode dataFrame
        dataFrame = pd.get_dummies(dataFrame[categorical_cols])
        dataFrameSample = dataFrame.sample(frac=.3)
        dataFrame.to_csv('FeatureDummies.csv')

        # Collecting the inferred rules in a dataframe 
        freq_items = apriori(dataFrame, min_support=0.05, use_colnames=True, max_len=5, verbose=1, low_memory=True)
        print(freq_items.head())

        rules = association_rules(freq_items, metric="confidence", min_threshold=0.2)
        print(rules.head())
        rules.to_csv('AssociationRules.csv')

        return rules


    @staticmethod
    def plotAssociationRules(rules):
        plt.scatter(rules['support'], rules['confidence'], alpha=0.5)
        plt.xlabel('support')
        plt.ylabel('confidence')
        plt.title('Support vs Confidence')
        plt.show()