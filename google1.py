import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('testIntervention.json', scope) #Change to your downloaded JSON file name 
client = gspread.authorize(creds)

print(client)

# spreadsheets = ['Best Interventions (Responses)']
spreadsheets = ['Experience']

def main(spreadsheets):

	df = pd.DataFrame()

	for spreadsheet in spreadsheets:
		print(spreadsheet)
		#Open the Spreadsheet
		sh = client.open(spreadsheet)

		#Get all values in the first worksheet
		worksheet = sh.get_worksheet(0)
		data = worksheet.get_all_values()

		#Save the data inside the temporary pandas dataframe
		df_temp = pd.DataFrame(columns = [i for i in data[0]])
		for i in range(1,len(data)):
			df_temp.loc[len(df_temp)] = data[i]
		print(df_temp)
		#Convert column names



		df = df_temp.reset_index(drop=True)

		# df.to_csv('survey_data.csv',index=False)
		df.to_csv(spreadsheet+'.csv',index=False)

if __name__ == '__main__':
	print('Scraping Form Data')
	main(spreadsheets)