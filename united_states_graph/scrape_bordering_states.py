#
# scrape_bordering_states.py
# Use BeautifulSoup to create adjacency list of states and their bordering states
# Last Modified: 8/16/2017
# Modified By: Andrew Roberts
#

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

r = requests.get("http://state.1keydata.com/bordering-states-list.php")
soup = BeautifulSoup(r.text, "html.parser")

results = soup.find_all("tr")[3:-10]
state_dict = {"State": [], "Borders": []}

for result in results:
	state_dict["State"].append(result.contents[0].text)
	
	borders_text = result.contents[1].text
	if borders_text != "None":  
		if "(water border)" in borders_text:
			borders_text = borders_text.replace(" (water border)", "")
		if "Arkanssas" in borders_text:
			borders_text = borders_text.replace("Arkanssas", "Arkansas")
		state_dict["Borders"].append([state.strip() for state in borders_text.split(",")])

	else:
		state_dict["Borders"].append([])

state_df = pd.DataFrame(state_dict)
state_df["Previous"] = [np.nan for i in range(len(state_df.index))]
state_df["Distance"] = [np.nan for i in range(len(state_df.index))]
state_df.set_index("State", inplace=True)

state_df.to_pickle("state_df.pickle")



