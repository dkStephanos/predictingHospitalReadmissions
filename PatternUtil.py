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
        # Encode dataFrame
        dataFrame = pd.get_dummies(dataFrame)

        # Collecting the inferred rules in a dataframe 
        freq_items = apriori(dataFrame, min_support=0.6, use_colnames=True, max_len=5, verbose=1)
        print(freq_items.head())

        rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)
        print(rules.head())

        return rules


