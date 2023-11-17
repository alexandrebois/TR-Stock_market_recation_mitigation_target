import numpy as np
import re
import pandas as pd 
import datetime

# Function to test if an ISIN code is valid
def is_valid_isin(isin):
    """
    Parameters
    -----------
    isin : string

    Returns 
    -----------
    boolean
        returns True only if the string is a valid ISIN sequence
    """
    # Checking the type
    if not isinstance(isin, str):
        return False
    # Checking length
    if len(isin) != 12:
        return False
    # Two first caracters are capital letters
    if not re.match(r'^[A-Z]{2}', isin):
        return False
    # The 9 following are alphanumerical
    if not re.match(r'^[A-Z0-9]{9}', isin[2:11]):
        return False
    # The last one is a number
    last_char = isin[-1]
    if not last_char.isdigit():
        return False
    # Sum of digits
    #digits_sum = sum(int(c, 36) for c in isin[2:11])
    # Modulo 10 check
    #return (digits_sum + int(last_char)) % 10 == 0
    return True

is_valid_isin = np.vectorize(is_valid_isin)

def preprocess_isin(file_path, decimal = '.', sep = ',', encoding = 'utf-8', low_memory = True):
    """
    Parameters
    -----------
    file_path : string, path leading to the worksheet. Worksheet needs a 'ISIN' named column
    decimal : string, default '.', the coma to consider for float numbers
    sep : string, default ',' the csv separator
    encoding : string, default 'utf-8', try 'latin_1' for microsoft excel exported as csv files 
               if errors appears

    Returns 
    -----------
    pd.DataFrame
        returns the dataframe with only valid ISINs, no ISIN duplicates, and no NaN on ISIN column
    """
    extension = file_path.split('.')[1]
    if extension == 'csv' : 
        df = pd.read_csv(file_path, decimal = decimal, sep = sep, encoding = encoding, 
                         low_memory = low_memory)
    elif extension == 'xlsx' :
        df = pd.read_excel(file_path, decimal = decimal)
    else :
        raise Exception('extension de fichier non reconnue')
    df = df[ df['ISIN'].notna() ]
    df = df.drop_duplicates( subset = 'ISIN')
    filter = is_valid_isin(df['ISIN'])
    df = df[filter]
    return df

def to_date(str):
     """
     Parameters
     -----------
     str : string object with '%d/%m/%Y' format

     Returns
     ----------
     date object
          Renvoit l'objet date correspondant à la chaine de caractère
          passé en argument
          
     """
     format = '%d/%m/%Y'
     date = datetime.datetime.strptime(str, format)
     return date

to_date = np.vectorize(to_date)