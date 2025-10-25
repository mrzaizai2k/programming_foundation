import pandas as pd
import numpy as np

def process_data():
    # Read the CSV
    biopics = pd.read_csv("biopics.csv", encoding="latin-1")

    # 1️⃣ Remove duplicated rows
    biopics = biopics.drop_duplicates()

    # 2️⃣ Rename 'box_office' → 'earnings'
    biopics = biopics.rename(columns={"box_office": "earnings"})

    # 3️⃣ Remove rows where 'earnings' is NaN
    biopics = biopics.dropna(subset=["earnings"])

    # 4️⃣ Keep only movies released in or after 1990
    biopics = biopics[biopics["year_release"] >= 1990]

    # 5️⃣ Convert 'type_of_subject' and 'country' to categorical
    biopics["type_of_subject"] = biopics["type_of_subject"].astype("category")
    biopics["country"] = biopics["country"].astype("category")

    # 6️⃣ Create 'lead_actor_actress_known' = True if not NaN else False
    biopics["lead_actor_actress_known"] = ~biopics["lead_actor_actress"].isna()

    # 7️⃣ Convert earnings from dollars → millions of dollars
    biopics["earnings"] = biopics["earnings"] / 1_000_000

    # 8️⃣ Reorder columns
    biopics = biopics[
        [
            "title",
            "year_release",
            "earnings",
            "country",
            "type_of_subject",
            "lead_actor_actress",
            "lead_actor_actress_known",
        ]
    ]

    # 9️⃣ Sort rows by earnings (descending)
    biopics = biopics.sort_values(by="earnings", ascending=False).reset_index(drop=True)

    return biopics

'''
you are given dataset called biopics.csv, it has columns title, country, year_release, box office, type_of_subject, lead_actor_actress
write function
def process_data()
    biopics = pd.read_csv("biopics.csv", encoding = "latin-1")
     return biopics.reset_index(drop=true)

can use pandas and numpy only and take in no argumenst, rewrite the function with these features:
- filtered out duplicated rows
- rename the var box_office to earnings
- filter out rows for which earnings are missing (i.e they are NaN)
- keep only movies released in the year 1990 or later
- convert the type pf type_of_subject and country to categorical
- create new var called lead_actor_actress_known that is False if lead_actor_actress is Nan and True otherwise
- Update earnings such they are expressed in millions of dollares instead of dollars
- reorder the column in the data frae such that they are in the following order title, year_release, 
earnings, country, type of subject, lead actor actress, lead actor actress known
- sort the rows in desc by earnings'''
import numpy as np
import pandas as pd

def process_data():
    df = pd.read_csv('./data.csv', encoding="latin-1")
    df = df.drop_duplicates()

    df =df.rename(columns = {"box_office":"earnings"})
    df = df.dropna(subset=["earnings"])
    df = df[df["year_release"]>=1990]
    df["type_of_subject"] = df["type_of_subject"].astype('category')
    df["country"] = df["country"].astype('category')    
    df["lead_actor_actress_known"] = ~df["lead_actor_actress"].isna()
    df['earnings'] = df["earnings"]/1_000_000
    df = df [
        [
            "title",
            "year_release",
        ]
    ]
    
    df = df.sort_values(by="earnings", asceding= False).reset_index(drop=True)
    
    return df
