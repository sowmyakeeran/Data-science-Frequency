class Univariate():
    
    
    def QuanQual(self,dataset):
        Quan=[]
        Qual=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset[columnName].dtypes=="O"):
                #print("Qual")
                Qual.append(columnName)
            else:
                #print("Quan")
                Quan.append(columnName)
        return Quan,Qual
    def frequencyTable(self,dataset,columnName):
        import pandas as pd
        freq=pd.DataFrame(columns=["Unique_Values","Frequency","Relative_Freq","Cumsum"])
        freq["Unique_Values"]=dataset[columnName].value_counts().sort_index().index
        freq["Frequency"]=dataset[columnName].value_counts().sort_index().values
        freq["Relative_Freq"]=(freq["Frequency"]/len(freq))*100
        freq["Cumsum"]=freq["Relative_Freq"].cumsum()
        return freq