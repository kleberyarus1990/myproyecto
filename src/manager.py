import pandas as pd
import numpy as np

class Scenary():
    def resampleData(data,period,timeColumn):
        resampled = data.resample(period,on=timeColumn).mean() #Resample the data for given time period

        resampled['Hora'] = resampled.index.time #Retrieve the hour
        scene01 = resampled.groupby('Hora').mean()  # Create an average values for every time step of any day
        #print(scene01)
        return scene01

    def resampleData1(data,period,timeColumn):
        resampled = data.resample(period,on=timeColumn).mean() #Resample the data for given time period

        resampled['Mes'] = resampled.index.time #Retrieve the hour
        scene01 = resampled.groupby('Mes').mean()  # Create an average values for every time step of any day
        #print(scene01)
        return scene01




    def scene1(data,steps,concentracion): #Build scenary with varaible to be estimated
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long],columns=range(0,steps+1))
        for i in range (0,long-steps):
            temp = data.ix[data.index[i:i + steps+1], concentracion].values
            temp2 = np.transpose(temp)
            scene.ix[scene.index[i]] = temp2
        return scene

    def scene2(data, steps, variable1,variable2):  #Build scenary with two variables
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, 2*steps))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp1=data.ix[data.index[i:i + steps], variable2].values
            temp2 = np.ravel(np.column_stack((temp,temp1)))
            temp3 = np.transpose(temp2)
            scene.ix[scene.index[i]] = temp3
        scene.ix[scene.index[0:long - steps], 2 * steps] = data.ix[data.index[steps:long], variable2]
        return scene

    def scene3(data, steps, variable1, variable2,variable3):  #Build scenary with three variables
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, 3 * steps))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp2 = data.ix[data.index[i:i + steps], variable2].values
            temp3=data.ix[data.index[i:i + steps], variable3].values
            temp4 = np.ravel(np.column_stack((temp,temp2,temp3)))
            temp5 = np.transpose(temp4)
            scene.ix[scene.index[i]] = temp5
        scene.ix[scene.index[0:long - steps], 3 * steps] = data.ix[data.index[steps:long], variable3]
        return scene

    def scene4(data, steps, variable1, variable2, variable3, variable4):  #Build scenary with three variables
        long = len(data.index)
        scene = pd.DataFrame(index=data.index[steps:long], columns=range(0, 4 * steps))
        for i in range(0, long - steps):
            temp = data.ix[data.index[i:i + steps], variable1].values
            temp2 = data.ix[data.index[i:i + steps], variable2].values
            temp3=data.ix[data.index[i:i + steps], variable3].values
            temp4 = data.ix[data.index[i:i + steps], variable4].values
            temp5 = np.ravel(np.column_stack((temp,temp2,temp3,temp4)))
            temp6 = np.transpose(temp5)
            scene.ix[scene.index[i]] = temp6
        scene.ix[scene.index[0:long - steps], 4 * steps] = data.ix[data.index[steps:long], variable4]
        return scene
'''def scene1(data,steps,concentracion): #Build scenary with varaible to be estimated
        long = len(data.index)
        #print(long)
        scene = pd.DataFrame(index=data.index[steps:long],columns=range(0,steps))
        #scene=scene.dropna()
        #scene1=scene[0]
        d={1: (concentracion +' '+'-5'), 2: (concentracion +' '+'-4'), 3: (concentracion +' '+'-3'), 4: (concentracion +' '+'-2'), 5: (concentracion +' '+'-1')}
        scene.rename(columns=d,inplace=True)
        print("aqui")
        #print(scene.rename(index=str, columns={0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "e"}))
        print(list(scene))
        for i in range (0,long-steps):
            temp = data.ix [data.index[i:i + steps], concentracion].values
            #print(temp)
            temp2 = np.transpose(temp)
            #print(temp2)
            scene.ix[scene.index[i]] = temp2
            #print(scene)

        return scene'''