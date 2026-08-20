import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('sample database.csv')
df.info()
print(df.shape)
total_population = df["Population"].sum()
average_population = df["Population"].mean()
highest_population = df["Population"].max()
minimum_population = df["Population"].min()
print("Total Population is", total_population)
print("Average Population is", average_population)
print("Highest Population is", highest_population)
print("Minimum Population is", minimum_population)
top_10 = df.sort_values(by='Population', ascending=False).head(10)
print(top_10[['District', 'State', 'Population']])
highest_district_index = df["Population"].idxmax()
highest_district = df.loc[highest_district_index]
print(highest_district[['District', 'State', 'Population']])
high_population = df[df["Population"] > 100000]
high_population_literacy = df[
    (df["Population"] > 100000) &
    (df["Literacy_Rate"] > 90)
]
print('high population', len(high_population))
print('high population with high literacy', len(high_population_literacy))
state_population = df.groupby("State")["Population"].sum()
print(state_population)
highest_state = state_population.idxmax()
highest_state_population = state_population.max()
print("highest population in state is",highest_state)
print("total population in highest state is",highest_state_population)
top_states = state_population.sort_values(ascending=False).head(10)
print("Top 10 states by population is", top_states)
total_male = df["Male_Population"].sum()
total_female = df["Female_Population"].sum()
print("Total male population is ", total_male)
print("total female population is ", total_female)
male_percentage = (total_male / total_population) * 100
female_percentage = (total_female / total_population) * 100
print("Male percentage is ", male_percentage)
print("Female percentage is ", female_percentage)
if total_male + total_female == total_population:
    print("Total male and female population matches the total population.")
else:
    print("Not matched with total population.")
population_array = df["Population"].to_numpy()
numpy_total = np.sum(population_array)
numpy_average = np.mean(population_array)
numpy_max = np.max(population_array)
numpy_min = np.min(population_array)
print("Numpy total population is", numpy_total)
print("Numpy average population is", numpy_average)
print("Numpy maximum population is", numpy_max)
print("Numpy minimum population is", numpy_min)

plt.figure(figsize=(12, 6))

plt.bar(top_10["District"], top_10["Population"])

plt.title("Top 10 Districts by Population")
plt.xlabel("District")
plt.ylabel("Population")
plt.xticks(rotation=45, ha="center")
plt.tight_layout()

plt.figure(figsize=(12, 6))

plt.bar(top_states.index, top_states.values)

plt.title("Top 10 States by Total Population")
plt.xlabel("State")
plt.ylabel("Total Population")
plt.xticks(rotation=45, ha="center")
plt.tight_layout()

gender_labels = ["Male", "Female"]
gender_population = [total_male, total_female]

plt.figure(figsize=(8, 6))

plt.bar(gender_labels, gender_population)

plt.title("Total Male vs Female Population")
plt.xlabel("Gender")
plt.ylabel("Population")
plt.tight_layout()

plt.figure(figsize=(8, 6))
plt.pie(gender_population, labels=gender_labels, autopct='%1.1f%%', startangle=90, colors=['#1f77b4', '#ff7f0e'])
plt.title("Male vs Female Population Distribution")

plt.show()
state_total = state_population.sum()
if state_total == total_population:
    print("State total population matches the total population.")
else:
    print("State total population does not match the total population.")

print("\n========== KEY FINDINGS ==========")

print("1. Total population:", total_population)
print("2. Average population per district:", average_population)
print("3. Highest population district:",
      highest_district["District"],
      "-", highest_district["Population"])

print("4. Highest population state:",
      highest_state,
      "-", highest_state_population)

print("5. Districts with population above 100,000:",
      len(high_population))

print("6. Districts with population above 100,000 and literacy above 90%:",
      len(high_population_literacy))

print("7. Male population percentage:",
      round(male_percentage, 2), "%")

print("8. Female population percentage:",
      round(female_percentage, 2), "%")