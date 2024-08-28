import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('beer_reviews.csv')  

# print("Column names:", df.columns)

# 1. Which brewery produces the strongest beers?
strongest_beer_index = df['beer_abv'].idxmax()

strongest_beer = df.loc[strongest_beer_index]

strongest_brewery = strongest_beer['brewery_name']
strongest_beer_abv = strongest_beer['beer_abv']
strongest_beer_name = strongest_beer['beer_name']
strongest_beer_style = strongest_beer['beer_style']

print(f"The strongest beer is '{strongest_beer_name}', brewed by {strongest_brewery}.")
print(f"It is a {strongest_beer_style} (beer style) with an ABV of {strongest_beer_abv}%.")

# 2. Recommend 3 unique beers
# I Sorted by rating and head(100) to obtain at least top 3 beers, with no duplication of bear_names
top_beers = df.sort_values(by='review_overall', ascending=False).head(100) 
top_unique_beers = top_beers.drop_duplicates(subset='beer_name')
top_unique_beers = top_unique_beers.head(3) # top 3 unique beers

if len(top_unique_beers) < 3:
    print(f'Less than 3 unique beers available. Showing {len(top_unique_beers)} unique beers.') 
else:
    print('The top 3 unique beers to recommend are:')

print(top_unique_beers[['beer_name', 'review_overall']])


# 4. Beer by style

# if 'beer_style' in df.columns:
#     unique_styles = df['beer_style'].dropna().unique() 
#     print(f'\nThere are {len(unique_styles)} unique beer styles in the dataset:')
#     for style in unique_styles:
#         print(style)
# else:
#     print("Column 'beer_style' does not exist in the dataset.")

desired_style = 'Faro' 
beers_by_style = df[df['beer_style'].str.lower() == desired_style.lower()]

# Check if there are any beers matching the style
if beers_by_style.empty:
    print(f'No beers found that match {desired_style} style.')
else:
    beers_by_style_sorted = beers_by_style.sort_values(
        by=['review_aroma', 'review_appearance'], ascending=False)

    best_beer = beers_by_style_sorted.iloc[0]
    print(f'Based on aroma and appearance, the best {desired_style} beer to try is: {best_beer['beer_name']} which has an aroma rating of {best_beer['review_aroma']} and appearance rating of {best_beer['review_appearance']}')


# 3. Factors that impact the quality of beer the most
# Plot ABV vs. Quality
plt.figure(figsize=(10, 6))
plt.scatter(df['beer_abv'], df['review_overall'], alpha=0.5)
plt.title('Relationship between ABV and Quality')
plt.xlabel('ABV (%)')
plt.ylabel('Quality (Overall Review)')
# Plot Aroma vs. Quality
plt.figure(figsize=(10, 6))
plt.scatter(df['review_aroma'], df['review_overall'], alpha=0.5, color='orange')
plt.title('Relationship between Aroma and Quality')
plt.xlabel('Aroma Review Score')
plt.ylabel('Quality (Overall Review)')
# Plot Appearance vs. Quality
plt.figure(figsize=(10, 6))
plt.scatter(df['review_appearance'], df['review_overall'], alpha=0.5, color='green')
plt.title('Relationship between Appearance and Quality')
plt.xlabel('Appearance Review Score')
plt.ylabel('Quality (Overall Review)')

plt.show()

