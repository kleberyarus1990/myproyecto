import pandas as pd
from manager import CreateScenary

########################input parameters by user##########################
print("Ingrese el intervalo de tiempo a evaluar")
interval=input()                    #period
interval='5min'                  #period

print("Ingrese el numero de medidas hacia atras")
history=int(input())                #history
#history=5              #history

print("Loading....")

dateindex='TIMESTAMP'                #Column where date is stored
columntime='TIMESTAMP'               #Column Name containing the new resampled Time
##############################################################################

###############################Reading csv file###############################
df=pd.read_csv('../Data/final.csv',sep=';')         #read data from csv file
date_set = pd.to_datetime(df.TIMESTAMP, unit='s')   #convert column timestamp to datatime
#final=df[['WINDING_TEMP_AVE']]
df['TIMESTAMP']=date_set                            #assign to column to dataframe of timestamp converter
final=df[['TIMESTAMP','MPU4_KW','EXH_INL_GAS_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE']]  #select the variables in a new dataframe
dfx=final
#print(dfx.dtypes)
##############################################################################

dfx_train=CreateScenary.GroupingData(dfx,interval,columntime)


##########################Assembly posible scenaries##########################
print("Creating Scenaries....")
################ VARIABLE MPU4_KW ################
data01=CreateScenary.stage1(dfx_train,history,'MPU4_KW')
data01.to_csv('../Scenaries/MPU4_KW/MPU4_KW.csv')

# ONE VARIABLE VS MPU4_KW
data02=CreateScenary.stage2(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE','MPU4_KW')
data02.to_csv('../Scenaries/MPU4_KW/EXH_CYL_GAS_TEMP_AVE VS MPU4_KW.csv')

data02=CreateScenary.stage2(dfx_train,history,'WINDING_TEMP_AVE','MPU4_KW')
data02.to_csv('../Scenaries/MPU4_KW/WINDING_TEMP_AVE VS MPU4_KW.csv')

data02=CreateScenary.stage2(dfx_train,history,'EXH_INL_GAS_TEMP_AVE','MPU4_KW')
data02.to_csv('../Scenaries/MPU4_KW/EXH_INL_GAS_TEMP_AVE VS MPU4_KW.csv')

# TWO VARIABLES VS MPU4_KW
data03=CreateScenary.stage3(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE','MPU4_KW')
data03.to_csv('../Scenaries/MPU4_KW/EXH_CYL_GAS_TEMP_AVE WINDING_TEMP_AVE VS MPU4_KW.csv')

data03=CreateScenary.stage3(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE','EXH_INL_GAS_TEMP_AVE','MPU4_KW')
data03.to_csv('../Scenaries/MPU4_KW/EXH_CYL_GAS_TEMP_AVE EXH_INL_GAS_TEMP_AVE VS MPU4_KW.csv')

data03=CreateScenary.stage3(dfx_train,history,'WINDING_TEMP_AVE','EXH_INL_GAS_TEMP_AVE','MPU4_KW')
data03.to_csv('../Scenaries/MPU4_KW/WINDING_TEMP_AVE EXH_INL_GAS_TEMP_AVE VS MPU4_KW.csv')

# THREE VARIABLES VS MPU4_KW
data04=CreateScenary.stage4(dfx_train,history,'EXH_INL_GAS_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE','MPU4_KW')
data04.to_csv('../Scenaries/MPU4_KW/EXH_INL_GAS_TEMP_AVE EXH_CYL_GAS_TEMP_AVE WINDING_TEMP_AVE VS MPU4_KW.csv')

#EXH_CYL_GAS_TEMP_AVE
data01=CreateScenary.stage1(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE')
data01.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE.csv')


data02=CreateScenary.stage2(dfx_train,history,'MPU4_KW','EXH_CYL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/MPU4_KW VS EXH_CYL_GAS_TEMP_AVE.csv')

data02=CreateScenary.stage2(dfx_train,history,'WINDING_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/WINDING_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')

data02=CreateScenary.stage2(dfx_train,history,'EXH_INL_GAS_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/EXH_INL_GAS_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')

data03=CreateScenary.stage3(dfx_train,history,'EXH_INL_GAS_TEMP_AVE','WINDING_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE WINDING_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')

data03=CreateScenary.stage3(dfx_train,history,'MPU4_KW','EXH_INL_GAS_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/MPU4_KW EXH_INL_GAS_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')

data03=CreateScenary.stage3(dfx_train,history,'MPU4_KW','WINDING_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/MPU4_KW WINDING_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')

data04=CreateScenary.stage4(dfx_train,history,'EXH_INL_GAS_TEMP_AVE','MPU4_KW','WINDING_TEMP_AVE','EXH_CYL_GAS_TEMP_AVE')
data04.to_csv('../Scenaries/EXH_CYL_GAS_TEMP_AVE/EXH_INL_GAS_TEMP_AVE MPU4_KW WINDING_TEMP_AVE VS EXH_CYL_GAS_TEMP_AVE.csv')



#WINDING_TEMP_AVE

data01=CreateScenary.stage1(dfx_train,history,'WINDING_TEMP_AVE')
data01.to_csv('../Scenaries/WINDING_TEMP_AVE/WINDING_TEMP_AVE.csv')


data02=CreateScenary.stage2(dfx_train,history,'MPU4_KW','WINDING_TEMP_AVE')
data02.to_csv('../Scenaries/WINDING_TEMP_AVE/MPU4_KW VS WINDING_TEMP_AVE.csv')

data02=CreateScenary.stage2(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE')
data02.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE VS WINDING_TEMP_AVE.csv')

data02=CreateScenary.stage2(dfx_train,history,'EXH_INL_GAS_TEMP_AVE','WINDING_TEMP_AVE')
data02.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_INL_GAS_TEMP_AVE VS WINDING_TEMP_AVE.csv')



data03=CreateScenary.stage3(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE','MPU4_KW','WINDING_TEMP_AVE')
data03.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE MPU4_KW VS WINDING_TEMP_AVE.csv')

data03=CreateScenary.stage3(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE','EXH_INL_GAS_TEMP_AVE','WINDING_TEMP_AVE')
data03.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE EXH_INL_GAS_TEMP_AVE VS WINDING_TEMP_AVE.csv')

data03=CreateScenary.stage3(dfx_train,history,'MPU4_KW','EXH_INL_GAS_TEMP_AVE','WINDING_TEMP_AVE')
data03.to_csv('../Scenaries/WINDING_TEMP_AVE/MPU4_KW EXH_INL_GAS_TEMP_AVE VS WINDING_TEMP_AVE.csv')

data04=CreateScenary.stage4(dfx_train,history,'EXH_INL_GAS_TEMP_AVE','MPU4_KW','EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE')
data04.to_csv('../Scenaries/WINDING_TEMP_AVE/EXH_INL_GAS_TEMP_AVE MPU4_KW EXH_CYL_GAS_TEMP_AVE VS WINDING_TEMP_AVE.csv')


data01=CreateScenary.stage1(dfx_train,history,'EXH_INL_GAS_TEMP_AVE')
data01.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/EXH_INL_GAS_TEMP_AVE.csv')

data02=CreateScenary.stage2(dfx_train,history,'MPU4_KW','EXH_INL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/MPU4_KW VS EXH_INL_GAS_TEMP_AVE.csv')

data02=CreateScenary.stage2(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE','EXH_INL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE VS EXH_INL_GAS_TEMP_AVE.csv')

data02=CreateScenary.stage2(dfx_train,history,'WINDING_TEMP_AVE','EXH_INL_GAS_TEMP_AVE')
data02.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/WINDING_TEMP_AVE VS EXH_INL_GAS_TEMP_AVE.csv')


data03=CreateScenary.stage3(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE','MPU4_KW','EXH_INL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE MPU4_KW VS EXH_INL_GAS_TEMP_AVE.csv')

data03=CreateScenary.stage3(dfx_train,history,'EXH_CYL_GAS_TEMP_AVE','WINDING_TEMP_AVE','EXH_INL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/EXH_CYL_GAS_TEMP_AVE WINDING_TEMP_AVE VS EXH_INL_GAS_TEMP_AVE.csv')

data03=CreateScenary.stage3(dfx_train,history,'MPU4_KW','WINDING_TEMP_AVE','EXH_INL_GAS_TEMP_AVE')
data03.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/MPU4_KW WINDING_TEMP_AVE VS EXH_INL_GAS_TEMP_AVE.csv')

data04=CreateScenary.stage4(dfx_train,history,'WINDING_TEMP_AVE','MPU4_KW','EXH_CYL_GAS_TEMP_AVE','EXH_INL_GAS_TEMP_AVE')
data04.to_csv('../Scenaries/EXH_INL_GAS_TEMP_AVE/WINDING_TEMP_AVE MPU4_KW EXH_CYL_GAS_TEMP_AVE VS EXH_INL_GAS_TEMP_AVE.csv')



print('Generated Successfully :)')
##############################################################################