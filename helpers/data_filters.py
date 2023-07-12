'''
to filter out the data from the request
'''
def apply_filters(df, team, city, winner):
    filters = []
    #  adding filters in the filter list like `df['city'] == cit` 
    if team:
        filters.append((df['team1'] == team) | (df['team2'] == team))
    if city:
        filters.append(df['city'] == city)
    if winner:
        filters.append(df['winner'] == winner)

    
    if filters:
        # filtering out the data based on the filter list 
        filtered_data = df[filters[0]]
        # checking the remaining filters and add those also 
        for f in filters[1:]:
            filtered_data = filtered_data[f]
    # if filter list is empty then just return the whole dataframe
    else:
        filtered_data = df

    return filtered_data
