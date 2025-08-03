import pandas as pd
from format_helpers import fix_relationship, fix_tier
from column_extractor import extract_cols, fuzzy_rename_columns
from config import STANDARD_COLUMNS, KEYWORD_MAP
from apply_cond_format import apply_cond_format

# extract_cols("more_complex_census_test2.xlsx", sheet_name="UW Census")


def clean_and_save(file_path, sheet_name= "Cleaned"):
    loaded_file = pd.read_excel(file_path, engine = "openpyxl")

    column_map = fuzzy_rename_columns(loaded_file.columns, KEYWORD_MAP)
    loaded_file = loaded_file.rename(columns=column_map)

    for col in STANDARD_COLUMNS: 
        if col not in loaded_file.columns:
            loaded_file[col] = ""


    loaded_file[["Birth Date", "Hire Date"]] = loaded_file[["Birth Date", "Hire Date"]].apply(
        lambda col: pd.to_datetime(col, errors="coerce").dt.strftime("%m/%d/%Y")
    )

    print("Got the columns")

    loaded_file = fix_relationship(loaded_file)
    loaded_file = fix_tier(loaded_file)


    cleaned_file = loaded_file[STANDARD_COLUMNS]

    with pd.ExcelWriter(file_path, engine = "openpyxl", mode = "a", if_sheet_exists="replace") as writer:
        cleaned_file.to_excel(writer, sheet_name=sheet_name, index=False)
        sheet = writer.book[sheet_name]
        apply_cond_format(sheet, STANDARD_COLUMNS)
        sheet.auto_filter.ref = "A1:J1"

    print(f"Cleaned data written to new sheet: {sheet_name}")
    print("Applied Conditional Colors")


clean_and_save("StarterCensusInfo.xlsx", sheet_name="UW Census")
