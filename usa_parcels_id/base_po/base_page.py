import os
from dbfread import DBF
from zipfile import ZipFile


def delete_files(path):
    os.unlink(path)


def read_dbf_file(url):
    table = DBF(url, encoding='utf-8')
    return table


def get_path_to_dbf_file(path_to_zip):
    try:
        with ZipFile(path_to_zip, 'r') as zipObj:
            filename_list = zipObj.namelist()
            for fileName in filename_list:
                if fileName.endswith('TaxList.dbf'):
                    path_to_dbf_file = zipObj.extract(fileName, '../usa_parcels_id/databases')
                    return str(path_to_dbf_file)
    except FileNotFoundError as e:
        print(e.args)


def get_path_to_dbf_file_from_folder(path_to_zip):
    path = '../usa_parcels_id/databases'
    try:
        with ZipFile(path_to_zip, 'r') as zipObj:
            zipObj.extractall(path)
        files = os.listdir(path)
        for file in files:
            if file.endswith('.zip'):
                print()
            else:
                path_folder_with_dbf = path + '/' + file
                files_in_folder = os.listdir(path_folder_with_dbf)
                for f in files_in_folder:
                    if f.endswith('.dbf'):
                        return path_folder_with_dbf + '/' + f
    except FileNotFoundError as e:
        print(e.args)


def write_parcels_to_file(path_to_zip, parcel_id, state, country):
    path_to_dbf_file = get_path_to_dbf_file(path_to_zip)
    table = read_dbf_file(path_to_dbf_file)
    parcels = set()
    for row in table:
        parcels.add(str(row[parcel_id]))
    with open('../usa_parcels_id/states/' + state + '/parcels/' + country + '_parcels.csv', 'w') as file:
        for p in parcels:
            file.write(p + '\n')

    delete_files(path_to_zip)
    delete_files(path_to_dbf_file)


def write_parcels_to_file_2(path_to_zip, parcel_id, state, country):
    path_to_dbf_file = get_path_to_dbf_file_from_folder(path_to_zip)
    table = read_dbf_file(path_to_dbf_file)
    parcels = set()
    for row in table:
        parcels.add(row[parcel_id])
    with open('../usa_parcels_id/states/' + state + '/parcels/' + country + '_parcels.csv', 'w',
              encoding='utf-8') as file:
        for p in parcels:
            file.write(p + '\n')

    delete_files(path_to_zip)
    delete_files(path_to_dbf_file)


def write_parcels_to_file_NY(path_to_zip, swis, print_key, state, country):
    path_to_dbf_file = get_path_to_dbf_file(path_to_zip)
    table = read_dbf_file(path_to_dbf_file)
    parcels = set()
    for row in table:
        parcels.add(str(row[swis]) + ' ' + str(row[print_key]))
    with open('../usa_parcels_id/states/' + state + '/parcels/' + country + '_parcels.csv', 'w') as file:
        for p in parcels:
            file.write(p + '\n')

    delete_files(path_to_zip)
    delete_files(path_to_dbf_file)
