import pandas
from faker import Faker
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.workbook import Workbook


def create_workbook(workbook_name, sheet_names):
    # write_only to not get a default 'Sheet' in the file
    workbook = Workbook(write_only=True)
    # iterate through sheet names
    for sheet_name in sheet_names:
        # create new sheet with given name
        sheet = workbook.create_sheet(sheet_name)
        # create testdata for this sheet and fill it into a dataframe
        data = pandas.DataFrame(create_testdata())
        # fill dataframe into the sheet
        for row in dataframe_to_rows(data, index=False):
            sheet.append(row)

    # save the workbook with given name
    workbook.save(workbook_name)


def create_testdata():
    fake = Faker('de_DE')
    data_list = []
    for num in range(200):
        data_list.append({
            'Name': fake.last_name(),
            'Vorname': fake.first_name(),
            'Telefon': fake.phone_number(),
            'Strasse': fake.street_address(),
            'Postleitzahl': fake.postcode(),
            'Stadt': fake.city(),
            'Bank': fake.iban(),
            'Eintritt': fake.date_between().strftime('%d.%m.%Y')
        })
    return data_list


if __name__ == '__main__':
    create_workbook('daten/Adressen 1.xlsx', ['A', 'B', 'C'])
    create_workbook('daten/Adressen 2.xlsx', ['D'])
    create_workbook('daten/Adressen 3.xlsx', ['E', 'F', 'G'])
