### extracting tables from webpage using pandas ###


import pandas as pd

naturo = pd.read_html('https://en.wikipedia.org/wiki/List_of_Naruto_episodes')

no_of_table = len(naturo)

print (naturo[1])


print ("no of tables in the page is " + str (no_of_table))



## table extraction using CSV file form website ##

pd.read_CSV('')


## table extraction using pdf file form website ##

pd.read_pdf
