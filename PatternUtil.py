from apyori import apriori

class PatternUtil(object):
   
    @staticmethod
    def getPatterns(dataFrame):
        # Collecting the inferred rules in a dataframe 
        association_rules = apriori(dataFrame.values, min_support=0.005, min_confidence=0.8, min_length=2)
        association_results = list(association_rules)

        filteredResults = []
        #Filtering our results to just rules that rhs is survived
        for result in association_results:
            for entry in result.ordered_statistics:
                if entry.items_add == frozenset({'Yes'}):
                    filteredResults.append(entry)

        print("\nNumber of rules: {0}\n".format(len(filteredResults)))

        #Sorting by lift
        sortedResults = sorted(filteredResults, key=lambda x: x.lift, reverse=True)
        for result in sortedResults:
            print(str(result))



