import pandas as pd
from openpyxl import load_workbook
from config import STANDARD_COLUMNS, KEYWORD_MAP



def extract_cols(file_path, sheet_name = "UW Census"):

    loaded_file = pd.read_excel(file_path, engine = "openpyxl")
    # loaded_file.columns = [COLUMN_MAP.get(col.strip()) for col in loaded_file.columns]

    # print(loaded_file.head())


    #renaming known columns 
    column_map = fuzzy_rename_columns(loaded_file.columns, KEYWORD_MAP)
    loaded_file = loaded_file.rename(columns=column_map)
    
    # loaded_file = loaded_file.rename(columns=lambda col: COLUMN_MAP.get(col.strip().lower(), col.strip()))
    
    for col in STANDARD_COLUMNS: 
        if col not in loaded_file.columns:
            loaded_file[col] = ""

    # if ("Birth Date", "Hire Date") in loaded_file.columns:
    #     loaded_file["Birth Date"] = pd.to_datetime(loaded_file["Birth Date"], errors="coerce").dt.strftime("%m/%d/%Y")

    loaded_file[["Birth Date", "Hire Date"]] = loaded_file[["Birth Date", "Hire Date"]].apply(
        lambda col: pd.to_datetime(col, errors="coerce").dt.strftime("%m/%d/%Y")
    )

    #reordering to right order
    cleaned_file = loaded_file[STANDARD_COLUMNS]

    with pd.ExcelWriter(file_path, engine = "openpyxl", mode = "a", if_sheet_exists="replace") as writer:
        cleaned_file.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Cleaned data written to new sheet: {sheet_name}")



def fuzzy_rename_columns(columns, keyword_map):
    renamed = {}
    for col in columns: 
        clean_col = col.strip().lower()
        mapped = None

        for keyword, standard in keyword_map.items():
            if keyword in clean_col:
                mapped = standard
                break
        
        renamed[col] = mapped if mapped else col.strip()

    return renamed







