from pandas import DataFrame
from gspread import service_account


def get_file_from_gsheets(file_name: str, sheet_name: str) -> DataFrame:

    sa = service_account()
    sh = sa.open(file_name)

    data = sh.worksheet(sheet_name)

    df = DataFrame(data=data.get_values()[1:], columns=data.get_values()[0])

    return df


if __name__ == "__main__":
    # Testing
    from tabulate import tabulate

    df = get_file_from_gsheets(file_name="input-data", sheet_name="sheet_1")

    print(tabulate(df, tablefmt="psql", headers=df.columns, showindex=False))
