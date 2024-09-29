# Email-Auto-comp
A program for comparing bookings in Teamup against Google sheets


## Prerequisites
### Python packages
```
pip install fuzzywuzzy[speedup]
```

### CSV files
#### Google sheets
Export Google sheets of existing licenses (Recommended: "Alla Licenser" and "Licenser VT24 - Nu"). Separated files are ok, but should all be added into the `google_excel_sheets` folder.

#### Teamup
Export Teamup calender: 
1. Access Teamup as administrator
2. Enter the Settings
3. Enter Exporting events
4. Export as Comma Separated Values (.csv) for selected calenders for a specific dates
5. Exported files should be planced into teamup_bookings
