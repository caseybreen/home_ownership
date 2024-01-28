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

            specs['genders'] = [0, 1, 2]
            specs['ages_ranges'] = [{
                                      "min": 13
                                    },
                                    {
                                      "min": 15
                                    },
                                    {
                                      "min": 18
                                    },
                                    {
                                      "min": 15,
                                      "max": 24
                                    },
                                    {
                                      "min": 25,
                                      "max": 59
                                    },
                                    {
                                      "min": 60
                                    },
                                    {
                                      "min": 15,
                                      "max": 49
                                    },
                                    {
                                      "min": 18,
                                      "max": 24
                                    },
                                    {
                                      "min": 18,
                                      "max": 49
                                    }] 
            specs['target_groups'] = ["target_groups": [
                                        {},
                                        {
                                          "user_os": [
                                            {
                                              "name": "Android",
                                              "values": [
                                                "Android"
                                              ]
                                            },
                                            {
                                              "name": "iOS",
                                              "values": [
                                                "iOS"
                                              ]
                                            },
                                            {
                                              "name": "Android_or_iOS",
                                              "values": [
                                                "iOS",
                                                "Android"
                                              ]
                                            }
                                          ]
                                        },
                                        {
                                          "behavior": {
                                            "access_device": [
                                              {
                                                "or": [
                                                  6004384041172
                                                ],
                                                "name": "iOS"
                                              },
                                              {
                                                "or": [
                                                  6004386044572
                                                ],
                                                "name": "Android"
                                              },
                                              {
                                                "not": [
                                                  6004384041172,
                                                  6004386044572
                                                ],
                                                "name": "Not_iOS_or_Android_OS"
                                              },
                                              {
                                                "or": [
                                                  6075237200983,
                                                  6075237226583,
                                                  6106223987983,
                                                  6106224431383,
                                                  6092512462983,
                                                  6092512424583,
                                                  6092512412783
                                                ],
                                                "name": "High_end_galaxy_phone_S8_S8p_S9_S9p_High_end_apple_iphone_X_8_and_8p"
                                              },
                                              {
                                                "or": [
                                                  6015235495383
                                                ],
                                                "name": "Wifi"
                                              },
                                              {
                                                "or": [
                                                  6017253486583
                                                ],
                                                "name": "2G_Network"
                                              },
                                              {
                                                "or": [
                                                  6017253511583
                                                ],
                                                "name": "3G_Network"
                                              },
                                              {
                                                "or": [
                                                  6017253531383
                                                ],
                                                "name": "4G_Network"
                                              },
                                              {
                                                "not": [
                                                  6015235495383,
                                                  6017253486583,
                                                  6017253511583,
                                                  6017253531383
                                                ],
                                                "name": "Not_2G_3G_4G_or_WiFi_network"
                                              },
                                              {
                                                "or": [
                                                  6091658707783,
                                                  6091658708183
                                                ],
                                                "name": "Uses_a_mobile_device_0_to_3_months"
                                              },
                                              {
                                                "or": [
                                                  6091658512983,
                                                  6091658512183,
                                                  6091658540583,
                                                  6091658562383,
                                                  6091658651583
                                                ],
                                                "name": "Uses_a_mobile_device_4_to_24_months"
                                              },
                                              {
                                                "or": [
                                                  6091658683183
                                                ],
                                                "name": "Uses_a_mobile_device_25_months_plus"
                                              },
                                              {
                                                "or": [
                                                  6002714898572
                                                ],
                                                "name": "Small_business_owners"
                                              },
                                              {
                                                "not": [
                                                  6002714898572
                                                ],
                                                "name": "Not_Small_business_owners"
                                              }
                                            ]
                                          }
                                        }
                                    ]
            

            file_out = os.path.join(specs_dir, '_'.join([str(i).zfill(2), country, platform]) + '.json')
            with open(file_out, "w") as f:
                f.write(json.dumps(specs))