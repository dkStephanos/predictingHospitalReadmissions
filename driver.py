from DriverHelper import DriverHelper
from FileReaderUtil import FileReaderUtil
from DataUtil import DataUtil
from PatternUtil import PatternUtil
<<<<<<< HEAD
from SupportVector import SVM
from LogisticRegression import LogReg
=======
>>>>>>> 3665f6d5214dade7d07d7ed93ee2b1c0943e282b

if __name__ == '__main__':

    # --- Preprocessing ---
    #rawPatientDF = DriverHelper.getRawPatientDF()
    #cleanPatientDF = DriverHelper.cleanRawData(rawPatientDF)
<<<<<<< HEAD

    # --- Pattern Mining ---
    #cleanPatientDF = DriverHelper.getCleanPatientDF()
    #patterns = PatternUtil.getPatterns(cleanPatientDF)
    #rules = DriverHelper.getReadmittedRulesFromFile()

    # --- Predictive Modeling ---
    cleanPatientDF = DriverHelper.getCleanPatientDF()
    cleanPatientDF = DataUtil.encodeForModeling(cleanPatientDF)
=======

    # --- Pattern Mining ---
    cleanPatientDF = DriverHelper.getCleanPatientDF()
    patterns = PatternUtil.getPatterns(cleanPatientDF)
>>>>>>> 3665f6d5214dade7d07d7ed93ee2b1c0943e282b

    kernelToUse = 'rbf' #gaussian
    testValuePercent = 20
    chosenC = 35
    chosenS = 1

    #SVM.getLearningCurve(cleanPatientDF, 45, kernelToUse, './Graphs/SVMLearningCurve1.png')
    #average = SVM.testNIterations(cleanPatientDF, chosenC, chosenS, kernelToUse, testValuePercent, 5)
    #print("Average: ", SVM.findAverage(average))

    print('Accuracy:  {0}\n'.format(LogReg.classify(cleanPatientDF)))
    LogReg.getLearningCurve(cleanPatientDF, './Graphs/LogRegLearningCurve.png')