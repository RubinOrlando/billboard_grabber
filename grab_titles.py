import pandas as pd

url = 'https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_'

def get_data(url):
    """TODO: Specify function
    
    Arguments:
        url {str} -- String containing the address from where you want to obtain the data
    
    Returns:
        pandas.DataFrame -- Data set containing tables of the sent urls
    """
    data = pd.read_html(url, header=0)
    # Take the first table that has the form n x 3.

    for table in data:
        if table.shape[1] == 3:
            data = table
            break
    data = data.drop(columns=data.columns[0])
    return data

year_data = []

for i in range(1959, 2018):
    new_url = "{}{}".format(url, i)
    my_df = get_data(new_url)

    # If there is an error in the table form(atting?), finish the program (function?) and say in which year the error occurs
    if my_df.shape[1] != 2:
        print("error in the year {}".format(i))
        print(my_df.shape)
        quit()

    for j, col in enumerate(my_df.columns):
        my_df.iloc[:, j] = my_df.iloc[:, j].str.replace('"', '')

    my_df['Year'] = i
    year_data.append(my_df)

final_table = pd.concat(year_data, ignore_index=True)

print(final_table)
print(year_data[0])

final_table.to_csv('songlist.csv', 
                   columns=['Year', 'Title', 'Artist(s)'], index=False)
