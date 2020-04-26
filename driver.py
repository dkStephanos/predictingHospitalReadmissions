from DriverHelper import DriverHelper
from FileReaderUtil import FileReaderUtil
from DataUtil import DataUtil
from PatternUtil import PatternUtil
from SupportVector import SVM
from LogisticRegression import LogReg
from NeuralNetwork import NeuralNetwork

if __name__ == '__main__':

    # --- Preprocessing ---
    rawPatientDF = DriverHelper.getRawPatientDF()
    cleanPatientDF = DriverHelper.cleanRawData(rawPatientDF)

    # --- Pattern Mining ---
    #cleanPatientDF = DriverHelper.getCleanPatientDF()
    #patterns = PatternUtil.getPatterns(cleanPatientDF)
    #rules = DriverHelper.getReadmittedRulesFromFile()

    # --- Predictive Modeling ---
    #cleanPatientDF = DriverHelper.getCleanPatientDF()
    cleanPatientDF = DataUtil.encodeForModeling(cleanPatientDF)

    kernelToUse = 'rbf' #gaussian
    testValuePercent = 20
    chosenC = 1
    chosenS = .01

    #SVM.classify(cleanPatientDF, chosenC, chosenS, kernelToUse, testValuePercent, True, True)
    #SVM.getValidationCurve(cleanPatientDF, chosenC, kernelToUse, './Graphs/SVMValidationCurve.png')
    #SVM.getLearningCurve(cleanPatientDF, chosenC, chosenS, kernelToUse, './Graphs/SVMLearningCurve.png')
    #average = SVM.testNIterations(cleanPatientDF, chosenC, chosenS, kernelToUse, testValuePercent, 5)
    #print("Average: ", SVM.findAverage(average))

    #print('Accuracy:  {0}\n'.format(LogReg.classify(cleanPatientDF)))
    #LogReg.classify(cleanPatientDF)
    #LogReg.getLearningCurve(cleanPatientDF, './Graphs/LogRegLearningCurve2.png')

    #---- Testing Neural Network --------
    alpha = 0.000001
    layerDimensions =  (100,)
    solver = 'lbfgs'
    testValuePercent = 20
    fixSeed = False
    printOut = True
    print("\nRunning Neural Network")
    NeuralNetwork.classify(cleanPatientDF, alpha, layerDimensions, solver, testValuePercent, fixSeed, printOut)