from typing import Union, Optional, Any
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

class DateTimeFeatures(BaseEstimator, TransformerMixin):
    """
    DateTimeFeatures extracts date and time features from datetime variables, 
    adding new columns to dataset. DatetimeFeatures can extract datetime 
    information from existing datetime variables or from the dataframe index.
    """

    def __init__(self, variables: Union[None, str] = None) -> None:
        self.variables = variables
        
    def fit(self, X: pd.DataFrame, y: Optional[pd.Series]=None) -> Any:
        """
        This transformer does not learn any parameter.
        """
        if self.variables==None and not np.issubdtype(X.index.dtype, np.datetime64):
            raise TypeError("Index should have datetime type")
        if self.variables!=None and not np.issubdtype(df[self.variables].dtype, np.datetime64):
            raise TypeError("Column should have datetime type")
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Extract the date and time features and add them to the dataframe.
        """
        if self.variables==None:
            date_series = X.index.to_series()
        else:
            date_series = X[self.variables]
        X = X.assign(         
            day = date_series.dt.day,
            month = date_series.dt.month,
            #year = date_series.dt.year,
            day_of_year = date_series.dt.day_of_year,
            sin_day_of_year = np.sin(np.pi*date_series.dt.day_of_year/183),
            cos_day_of_year = np.cos(np.pi*date_series.dt.day_of_year/183),
            sin_month = np.sin(np.pi*date_series.dt.month/6),
            cos_month = np.cos(np.pi*date_series.dt.month/6),  
        )
        return X
