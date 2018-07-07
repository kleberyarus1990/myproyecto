import pandas as pd
import numpy as np

class CreateScenary():
    def GroupingData(data,period,timeColumn):
        resampled = data.resample(period,on=timeColumn).mean()  #data resampled with period

        resampled['Hora'] = resampled.index.time #Retrieve the hour
        stage01 = resampled.groupby('Hora').mean()  # Create an average values for every time step of any day
        #print(stage01)
        return stage01

    def stage1(data, hist, variable):  # Build stage
        long = len(data.index)

        stage = pd.DataFrame(index=data.index[hist:long], columns=range(0, hist+1))
        a=list(stage)
        head=list()
        a.reverse()
        #print(a)
        for x in range(0,len(a)):
            head.insert(0,variable+' -'+str(x))
        stage = pd.DataFrame(index=data.index[hist:long], columns=head)
        for i in range(0, long - hist):
            aux = data.ix[data.index[i:i + hist+1], variable].values
            aux2 = np.transpose(aux)
            stage.ix[stage.index[i]] = aux2

        return stage





    '''def stage1(data,hist,variable): #Build stage with varaible to be estimated
        long = len(data.index)
        stage = pd.DataFrame(index=data.index[hist:long],columns=range(0,hist+1))
        for i in range (0,long-hist):
            aux = data.ix[data.index[i:i + hist+1], variable].values
            aux2 = np.transpose(aux)
            stage.ix[stage.index[i]] = aux2
        return stage'''

    def stage2(data, hist, variable1,variable2):  #Build stage with two variables
        long = len(data.index)
        stage = pd.DataFrame(index=data.index[hist:long], columns=range(0, 2*hist))
        a = list(stage)
        #print(long)
        head = list()
        a.reverse()
        cont = 0
        # print(variable1)
        variables = [variable1, variable2]

        temp = int(len(a) / 2)
        # print(temp)
        x = temp
        x1 = 0
        # x1 = len(variables)

        for i in range(1, temp + 1):
            for j in range(1, len(variables) + 1):
                #   if x1<=len(variables):
                head.insert(cont, variables[x1] + ' -' + str(x))
                cont = cont + 1
                x1 = x1 + 1
                if x1 >= len(variables):
                    x1 = 0
            x = int(x) - 1

        #head.append('a')
        #stage = pd.DataFrame(index=data.index[hist:long], columns=head)

        #stage.set_axis(['a', 'b', 'c'], axis=1, inplace=True)

        print(stage.columns)

        for i in range(0, long - hist):
            aux = data.ix[data.index[i:i + hist], variable1].values
            aux1=data.ix[data.index[i:i + hist], variable2].values
            aux2 = np.ravel(np.column_stack((aux,aux1)))
            aux3 = np.transpose(aux2)
            stage.ix[stage.index[i]] = aux3
        print("una")
        print(stage)
        stage.ix[stage.index[0:long - hist], 2 * hist] = data.ix[data.index[hist:long+1], variable2]
        print("dos")
        print(stage)




        return stage

    '''def stage2(data, hist, variable1,variable2):  #Build stage with two variables
        long = len(data.index)
        stage = pd.DataFrame(index=data.index[hist:long], columns=range(0, 2*hist))
        for i in range(0, long - hist):
            aux = data.ix[data.index[i:i + hist], variable1].values
            aux1=data.ix[data.index[i:i + hist], variable2].values
            aux2 = np.ravel(np.column_stack((aux,aux1)))
            aux3 = np.transpose(aux2)
            stage.ix[stage.index[i]] = aux3
        stage.ix[stage.index[0:long - hist], 2 * hist] = data.ix[data.index[hist:long], variable2]
        return stage'''

    def stage3(data, hist, variable1, variable2,variable3):  #Build stage with three variables
        long = len(data.index)
        stage = pd.DataFrame(index=data.index[hist:long], columns=range(0, 3 * hist))
        a = list(stage)
        # print(a)
        head = list()
        a.reverse()
        cont = 0
        # print(variable1)
        variables = [variable1, variable2,variable3]
        temp = int(len(a) / 3)
        # print(temp)
        x = temp
        x1 = 0
        # x1 = len(variables)

        for i in range(1, temp + 1):
            for j in range(1, len(variables) + 1):
                #   if x1<=len(variables):
                head.insert(cont, variables[x1] + ' -' + str(x))
                cont = cont + 1
                x1 = x1 + 1
                if x1 >= len(variables):
                    x1 = 0

            x = int(x) - 1
        stage = pd.DataFrame(index=data.index[hist:long], columns=head)
        for i in range(0, long - hist):
            aux = data.ix[data.index[i:i + hist], variable1].values
            aux2 = data.ix[data.index[i:i + hist], variable2].values
            aux3=data.ix[data.index[i:i + hist], variable3].values
            aux4 = np.ravel(np.column_stack((aux,aux2,aux3)))
            aux5 = np.transpose(aux4)
            stage.ix[stage.index[i]] = aux5
        #stage.ix[stage.index[0:long - hist], 3 * hist] = data.ix[data.index[hist:long], variable3]
        return stage

    def stage4(data, hist, variable1, variable2, variable3, variable4):  #Build stage with three variables
        long = len(data.index)
        stage = pd.DataFrame(index=data.index[hist:long], columns=range(0, 4 * hist))
        a = list(stage)
        # print(a)
        head = list()
        a.reverse()
        cont = 0
        # print(variable1)
        variables = [variable1, variable2,variable3,variable4]

        temp = int(len(a) / 4)
        # print(temp)
        x = temp
        x1 = 0
        # x1 = len(variables)

        for i in range(1, temp + 1):
            for j in range(1, len(variables) + 1):
                #   if x1<=len(variables):
                head.insert(cont, variables[x1] + ' -' + str(x))
                cont = cont + 1
                x1 = x1 + 1
                if x1 >= len(variables):
                    x1 = 0

            x = int(x) - 1
        stage = pd.DataFrame(index=data.index[hist:long], columns=head)
        for i in range(0, long - hist):
            aux = data.ix[data.index[i:i + hist], variable1].values
            aux2 = data.ix[data.index[i:i + hist], variable2].values
            aux3=data.ix[data.index[i:i + hist], variable3].values
            aux4 = data.ix[data.index[i:i + hist], variable4].values
            aux5 = np.ravel(np.column_stack((aux,aux2,aux3,aux4)))
            aux6 = np.transpose(aux5)
            stage.ix[stage.index[i]] = aux6
        #stage.ix[stage.index[0:long - hist], 4 * hist] = data.ix[data.index[hist:long], variable4]
        return stage

    def GroupingData1(data, period, timeColumn):
        resampled = data.resample(period, on=timeColumn).mean()  # Resample the data for given time period
        resampled['Mes'] = resampled.index.time  # Retrieve the hour
        stage01 = resampled.groupby('Mes').mean()  # Create an average values for every time step of any day
        return stage01
