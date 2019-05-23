#
import pandas as pd

spreadsheets = pd.ExcelFile('amazon.xlsx')

#--------------
def fetch_report(df):
	rows = df.shape[0]
	fee_per_asin = {}
	for row in range(rows):
		# print("{} : {}".format(df.loc[i,'asin'], df.loc[i,'expected-fulfillment-fee-per-unit']))
		fee_per_asin[df.loc[row,'asin']] = df.loc[row,'expected-fulfillment-fee-per-unit']
	return fee_per_asin

def fetch_reference(df):
	rows = df.shape[0]
	fee_per_asin = {}
	for row in range(rows):
		# print("{} : {}".format(df.loc[row,'asin'], df.loc[row,'expected-fulfillment-fee-per-unit']))
		fee_per_asin[df.loc[row,'asin']] = df.loc[row,'expected-fulfillment-fee-per-unit']
	return fee_per_asin


# to read all sheets
for sheet_name in spreadsheets.sheet_names:
	if str(sheet_name).startswith('Fee Preview'):
		fee_preview_sheet = pd.read_excel(spreadsheets, sheet_name)
		fees_in_report = fetch_report(fee_preview_sheet)

	if str(sheet_name).startswith('Reference'):
		reference_sheet = pd.read_excel(spreadsheets, sheet_name)
		fees_in_reference = fetch_reference(reference_sheet)

print("Fee Preview Report versus Custom Reference Fees")
for asin in fees_in_report.keys():
	if fees_in_report[asin] == fees_in_reference[asin]:
		print("[+] {} : Fees MATCH".format(asin))
	else:
		print("[ERROR] {} : Fees DO NOT MATCH".format(asin))
