# better-trader-to-xls
Convertor cfg to csv for Better Trader data

## For get .csv file:
 1. You must have a 'item_defaults.cfg' in folder.
 2. Write in console.
    1. Linux
        ``` 
        python data_to_csv.py
        ```
    2. Windows
          ``` 
          C:\<path to python>\python.exe D:/<path to .py>/data_to_csv.py
          ```
 3. It will created a 'NEW_item_defaults.csv'


## For get .cfg file for game:
 1. You must have a 'Updated_item_defaults.csv.cfg' in folder.
 2. Write in console.
    1. Linux
        ``` 
        python from_csv_to_cfg.py
        ```
    2. Windows
          ``` 
          C:\<path to python>\python.exe D:/<path to .py>/from_csv_to_cfg.py
          ```
 3. It will created a 'CREATED_item_defaults.cfg'