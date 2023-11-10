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

# read in the Normal.csv file
test_df = pd.read_csv('./CSV/Normal.csv')

# modify the Caller ID column to be 21
test_df['Caller ID'] = 21

# add a new column 'type' to the test dataframe
test_df['type'] = 'test'

# concatenate the test dataframe with the combined dataframe
combined_df = pd.concat([combined_df, test_df], ignore_index=True)

# group the dataframe by Caller ID and apply a function to each group
combined_df = combined_df.groupby('Caller ID').apply(lambda x: x.sample(frac=0.5))

# reset the index of the dataframe
combined_df = combined_df.reset_index(drop=True)

# write the combined dataframe to a new csv file
combined_df.to_csv('./CSV/combined.csv', index=False)