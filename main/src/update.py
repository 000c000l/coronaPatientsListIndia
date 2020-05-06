import pandas as pd
import os
def csv_update(path):
    """
        To delete unnecessary columns
    """
    print(path)
    data=pd.read_csv(path,delimiter=",")
    newData=data.drop(columns=data.columns[16:])
    path=os.path.join(os.path.dirname(path),"newData.csv")
    newData.to_csv(path)
    """
        To rename the columns of csv file and create a file newData.csv in the very same directory
    """
    data=pd.read_csv(path,delimiter=",",names=["patient_id",
                                                "state_patient_number",
                                                "date_announced",
                                                "estimated_onset_date",
                                                "age_bracket",
                                                "gender",
                                                "detected_city",
                                                "detected_district",
                                                "detected_state",
                                                "state_code",
                                                "current_status",
                                                "notes",
                                                "contracted_from",
                                                "nationality",
                                                "type_of_transmission",
                                                "status_change_date"
                                                ])
    data=data.drop(data.index[0])
    data.to_csv(path,index=False)


