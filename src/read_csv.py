import pandas as pd
from manager import Scenary

########################Parameters to be set by user##########################
period='10min'      #Period of time to evaluated
historyStep=10       #Number of time steps to go back
#testPercentage=0.9  #Fraction of data to be taken as Teste data
##############################################################################

##################Parameters to set according with available##################
#todelete = '_id'               #Mongodb index name to be deleted
validdate='2017/05/01 00:00:00' #Date when valid date starts
dateindex='TIMESTAMP'                #Column where date is stored
columntime='TIMESTAMP'               #Column Name containing the new resampled Time
##############################################################################

###############################Reading csv file###############################
df=pd.read_csv('../Data/final.csv',sep=';') #read data from csv file
#df=pd.read_csv('../Data/final.csv',encoding='latin-1', low_memory=False) #read data from csv file
date_set = pd.to_datetime(df.TIMESTAMP, unit='s')
#final=df[['WINDING_TEMP_AVE']]
df['TIMESTAMP']=date_set
final=df[['TIMESTAMP','MPU4_KW','EXH_INL_GAS_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE']]
#final.set_index('TIMESTAMP')
#final=df
#dfx=df
dfx=final
#print(dfx.dtypes)
##############################################################################

###########################Processing Data####################################
#Procesisng data to eliminate innecesary data and calculating aditional data
#dfx=Prepare.prepare(df,dateindex,validdate,temperature1,temperature2)
##############################################################################

########################Creating Test and Training Data#######################
#test=dfx.sample(frac=testPercentage,random_state=1)
#train = dfx.drop(test.index)
#dfx_train=Scenary.resampleData(train,period,columntime)
dfx_train=Scenary.resampleData(dfx,period,columntime)
dfx_train1=Scenary.resampleData1(dfx,period,columntime)
#dfx_test=Scenary.resampleData(test,period,columntime)
#print("inicio")
#print(dfx_train)
#print("fin")
##############################################################################

##########################Assembly posible scenaries##########################
# Only concentration
data01=Scenary.scene1(dfx_train,historyStep,'MPU4_KW')
data01.to_csv('../Scenaries/MPU4_KW/MPU4_KW.csv')

#data011=Scenary.scene1(dfx_train1,historyStep,'MPU4_KW')
#data011.to_csv('../Scenaries/Method1/CO/MPU4_KWmes.csv')

# Concentration and one variable
data02=Scenary.scene2(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','MPU4_KW')
data02.to_csv('../Scenaries/MPU4_KW/EXH_CYL_GAS_TEMP_AVE VS MPU4_KW.csv')

data02=Scenary.scene2(dfx_train,historyStep,'WINDING_TEMP_AVE','MPU4_KW')
data02.to_csv('../Scenaries/MPU4_KW/WINDING_TEMP_AVE VS MPU4_KW.csv')

data02=Scenary.scene2(dfx_train,historyStep,'EXH_INL_GAS_TEMP_AVE','MPU4_KW')
data02.to_csv('../Scenaries/MPU4_KW/EXH_INL_GAS_TEMP_AVE VS MPU4_KW.csv')


#Concentration and two variables
data03=Scenary.scene3(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE','MPU4_KW')
data03.to_csv('../Scenaries/MPU4_KW/EXH_CYL_GAS_TEMP_AVE WINDING_TEMP_AVE VS MPU4_KW.csv')

data03=Scenary.scene3(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','EXH_INL_GAS_TEMP_AVE','MPU4_KW')
data03.to_csv('../Scenaries/MPU4_KW/EXH_CYL_GAS_TEMP_AVE EXH_INL_GAS_TEMP_AVE VS MPU4_KW.csv')

#data03=Scenary.scene3(dfx_train,historyStep,'WINDING_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE','MPU4_KW')
#data03.to_csv('../Scenaries/Method1/CO/Escenario31.csv')

#Concentration and three varaibles
data04=Scenary.scene4(dfx_train,historyStep,'EXH_INL_GAS_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE','MPU4_KW')
data04.to_csv('../Scenaries/MPU4_KW/EXH_INL_GAS_TEMP_AVE EXH_CYL_GAS_TEMP_AVE WINDING_TEMP_AVE VS MPU4_KW.csv')


data01=Scenary.scene1(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE')
data01.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE.csv')

# Concentration and one variable
data02=Scenary.scene2(dfx_train,historyStep,'MPU4_KW','EXH_CYL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/MPU4_KW VS EXH_CYL_GAS_TEMP_AVE.csv')

data02=Scenary.scene2(dfx_train,historyStep,'WINDING_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/WINDING_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')

data02=Scenary.scene2(dfx_train,historyStep,'EXH_INL_GAS_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/EXH_INL_GAS_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')


#Concentration and two variables
data03=Scenary.scene3(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE WINDING_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')

data03=Scenary.scene3(dfx_train,historyStep,'MPU4_KW','EXH_INL_GAS_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/MPU4_KW EXH_INL_GAS_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')

#Concentration and three varaibles
data04=Scenary.scene4(dfx_train,historyStep,'EXH_INL_GAS_TEMP_AVE','MPU4_KW','WINDING_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data04.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/EXH_INL_GAS_TEMP_AVE MPU4_KW WINDING_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')





data01=Scenary.scene1(dfx_train,historyStep,'WINDING_TEMP_AVE')
data01.to_csv('../Scenaries/WINDING_TEMP_AVE/WINDING_TEMP_AVE.csv')

# Concentration and one variable
data02=Scenary.scene2(dfx_train,historyStep,'MPU4_KW','WINDING_TEMP_AVE')
data02.to_csv('../Scenaries/WINDING_TEMP_AVE/MPU4_KW VS WINDING_TEMP_AVE.csv')

data02=Scenary.scene2(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE')
data02.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE VS WINDING_TEMP_AVE.csv')

data02=Scenary.scene2(dfx_train,historyStep,'EXH_INL_GAS_TEMP_AVE','WINDING_TEMP_AVE')
data02.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_INL_GAS_TEMP_AVE VS WINDING_TEMP_AVE.csv')


#Concentration and two variables
data03=Scenary.scene3(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','MPU4_KW','WINDING_TEMP_AVE')
data03.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE MPU4_KW VS WINDING_TEMP_AVE.csv')

data03=Scenary.scene3(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','EXH_INL_GAS_TEMP_AVE','WINDING_TEMP_AVE')
data03.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE EXH_INL_GAS_TEMP_AVE VS WINDING_TEMP_AVE.csv')

#Concentration and three varaibles
data04=Scenary.scene4(dfx_train,historyStep,'EXH_INL_GAS_TEMP_AVE','MPU4_KW','EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE')
data04.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_INL_GAS_TEMP_AVE MPU4_KW EXH_CYL_GAS_TEMP_AVE VS WINDING_TEMP_AVE.csv')


data01=Scenary.scene1(dfx_train,historyStep,'EXH_INL_GAS_TEMP_AVE')
data01.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/EXH_INL_GAS_TEMP_AVE.csv')

# Concentration and one variable
data02=Scenary.scene2(dfx_train,historyStep,'MPU4_KW','EXH_INL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/MPU4_KW VS EXH_INL_GAS_TEMP_AVE.csv')

data02=Scenary.scene2(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','EXH_INL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE VS EXH_INL_GAS_TEMP_AVE.csv')

data02=Scenary.scene2(dfx_train,historyStep,'WINDING_TEMP_AVE','EXH_INL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/WINDING_TEMP_AVE VS EXH_INL_GAS_TEMP_AVE.csv')


#Concentration and two variables
data03=Scenary.scene3(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','MPU4_KW','EXH_INL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE MPU4_KW VS EXH_INL_GAS_TEMP_AVE.csv')

data03=Scenary.scene3(dfx_train,historyStep,'EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE','EXH_INL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE WINDING_TEMP_AVE VS EXH_INL_GAS_TEMP_AVE.csv')

#Concentration and three varaibles
data04=Scenary.scene4(dfx_train,historyStep,'WINDING_TEMP_AVE','MPU4_KW','EXH_CYL_GAS_TEMP_AVE','EXH_INL_GAS_TEMP_AVE')
data04.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/WINDING_TEMP_AVE MPU4_KW EXH_CYL_GAS_TEMP_AVE VS EXH_INL_GAS_TEMP_AVE.csv')



print('Successfully Generated')
##############################################################################