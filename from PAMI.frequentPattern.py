from PAMI.frequentPattern.topk import FAE  as alg

inputFile = 'https://u-aizu.ac.jp/~udayrage/datasets/transactionalDatabases/Transactional_T10I4D100K.csv'

kCount=100  #Users can also specify this constraint between 0 to 1.

seperator='\t'

obj = alg.FAE(iFile=inputFile, k=kCount, sep=seperator)    #initialize
obj.mine()            #Start the mining process

obj.save(outFile='frequentPatternsMinSupCount100.txt')
frequentPatternsDF= obj.getPatternsAsDataFrame()
print('Total No of patterns: ' + str(len(frequentPatternsDF)))
print('Runtime: ' + str(obj.getRuntime()))
print('Memory (RSS): ' + str(obj.getMemoryRSS()))
print('Memory (USS): ' + str(obj.getMemoryUSS()))

# from PAMI.frequentPattern.topk import FAE  as alg
# import pandas as pd
# inputFile = 'https://u-aizu.ac.jp/~udayrage/datasets/transactionalDatabases/Transactional_T10I4D100K.csv'
# seperator='\t'
# minimumSupportCountList = [100, 150, 200, 250, 300]
# #minimumSupport can also specified between 0 to 1. E.g., minSupList = [0.005, 0.006, 0.007, 0.008, 0.009]

# result = pd.DataFrame(columns=['algorithm', 'minSup', 'patterns', 'runtime', 'memory'])
# #initialize a data frame to store the results of FAE algorithm