
import pandas as pd

# read in the two csv files
normal_df = pd.read_csv('./CSV/Training_Normal.csv')
susp_df = pd.read_csv('./CSV/Training_Susp.csv')

# add 10 to each caller ID in susp_df
susp_df['Caller ID'] = susp_df['Caller ID'] + 10

# add a new column 'type' to both dataframes
normal_df['type'] = 'normal'
susp_df['type'] = 'scammer'

# concatenate the two dataframes
combined_df = pd.concat([normal_df, susp_df], ignore_index=True)

# write the combined dataframe to a new csv file
combined_df.to_csv('./CSV/combined.csv', index=False)
