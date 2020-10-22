from database import *
import numpy as np

def showplot():
    records={}
    flag,result=fetchPlotData()
    new_recs = []
    if flag:
        result_records=result.split("\n")[:5]
        for i in result_records:
            new_i = i.replace("|", " ")
            new_recs.append([new_i[0:-2], new_i[-1]])
        records=dict(new_recs)
        table_names=list(records.keys())
        record_count=np.array(list(records.values()),dtype="int8")
        return table_names,record_count
    else:
        print(result) 

if __name__ == "__main__":
    showplot()
    # pass
