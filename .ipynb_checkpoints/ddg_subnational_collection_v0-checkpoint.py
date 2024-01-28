import os
import json
import pandas as pd

# virtual machine and collection names
vm = 'TODO-UPDATE'
collection = 'dgg_subnational'


if __name__ == '__main__':

    # ---- paths ---- #
    master_credentials_path = os.path.join('config', 'private', 'credentials_master.csv')
    specs_template_path = os.path.join('config', 'specs', 'templates')
    out_dir = os.path.join('docker', 'collectors', vm, collection)
    os.makedirs(out_dir, exist_ok=True)

    # ---- credentials ---- #

    # path for output credentials.csv
    credentials_path = os.path.join(out_dir, 'credentials.csv')

    # load master credentials
    master_credentials = pd.read_csv(master_credentials_path)

    # filter vm and collection
    credentials = master_credentials.loc[(master_credentials.vm == vm) &
                                         (master_credentials.collection == collection)]

    # save to csv
    credentials.to_csv(credentials_path,
                       columns=['token', 'app'],
                       header=False,
                       index=False)

    # ---- collection specs ---- #

    # output directory
    specs_dir = os.path.join(out_dir, 'specs')
    os.makedirs(specs_dir, exist_ok=True)

    # cleanup old specs
    for f in os.listdir(specs_dir):
        os.remove(os.path.join(specs_dir, f))


    countries = ['NG', 'ET', 'EG', 'ZA', 'UG', 'DZ', 'MA', 'AO', 'GH',
                 'MZ', 'MG', 'CI', 'CM', 'NE', 'ML', 'MW', 'ZM', 'TD',
                 'SO', 'SN', 'ZW', 'GN', 'RW', 'BJ', 'BI', 'TN', 'SS',
                 'TG', 'SL', 'LY', 'CG', 'LR', 'MR', 'ER', 'GM', 'BW',
                 'GA', 'LS', 'GW', 'GQ', 'MU', 'DJ', 'CV', 'ST', 'SC']
    
    #drop_countries = ['SD']
    countries = [i for i in countries if i not in drop_countries]

    platforms = ['facebook', 'instagram']

    i = 0
    for country in countries:
        for platform in platforms:
            i += 1

            specs_file = os.path.join(specs_template_path, country + '_regions.json')
            if not os.path.exists(specs_file):
                print('Specs template does not exist: ' + specs_file)
                continue

            # template json
            with open(specs_file) as f:
                specs = json.load(f)
            specs['name'] = collection

            # customise specs by platform and country
            specs["publisher_platforms"] = [platform]
            specs['languages'] = [None]

            file_out = os.path.join(specs_dir, '_'.join([str(i).zfill(2), country, platform]) + '.json')
            with open(file_out, "w") as f:
                f.write(json.dumps(specs))