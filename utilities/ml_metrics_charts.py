from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
from sklearn.preprocessing import normalize


def confusion_matrix_heatmap(y_true, y_pred, index_name="Actual", columns_name="Predicted",
normalized=True, figsize = (10,7), font_scale=1.4, cmap="Blues",annot_kws={"size": 16}):
       
    data = confusion_matrix(y_true, y_pred)
    df_cm = pd.DataFrame(data, columns=np.unique(y_true), index = np.unique(y_true))
    # print(df_cm)    
    df_normalized = df_cm.div(df_cm.sum(axis=1), axis=0)
    # print(df_normalized)
    if normalized: df = df_normalized
    else: df = df_cm
    df_cm.index.name = index_name
    df_cm.columns.name = columns_name
    plt.figure(figsize = figsize)
    sn.set(font_scale=font_scale) 
    sn.heatmap(df, cmap=cmap, annot=True, annot_kws=annot_kws)# font size