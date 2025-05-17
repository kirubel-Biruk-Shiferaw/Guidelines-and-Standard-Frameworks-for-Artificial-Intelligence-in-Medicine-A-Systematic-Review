#Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#Importing the data
data = pd.read_excel('your-path/AGREE Evaluation aggregate.xlsx')
#See the table
data

#Conver the table to dataframe
df = pd.DataFrame(data)
#Scan the columns
print(df.columns)
# Set 'Guideline' as the index
df.set_index('Guideline', inplace=True)

#Plot the aggregate score of the guidelines scaled percentage value 
plt.figure(figsize=(10, 8))
sns.heatmap(data=df, cmap='RdYlGn', annot=True, fmt='.1f', cbar=True)
plt.xlabel('AGREE II Domains')
plt.ylabel('Guidelines')
plt.title('Heatmap of AGREE II Score of Guidelines of AI reporting in Medicine')
plt.show()


plt.figure(figsize=(12, 6))

# Loop through each guideline and create a line plot for each
for index, guideline in enumerate(data['Guideline']):
    plt.plot(data.columns[1:], data.iloc[index, 1:], marker='.', markersize=8, label=guideline)

# Add labels and title
plt.xlabel('AGREE-II Domains', fontsize=12)
plt.ylabel('Score', fontsize=12)
#plt.title('Line Plot of Guidelines Across AGREE-II Domains', fontsize=16)

# Improve legend
plt.legend(loc='best', bbox_to_anchor=(1, 1), fontsize=12)

# Improve x-ticks
plt.xticks(rotation=45, ha='right', fontsize=12)

# Add grid lines for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust layout to make room for the legend
plt.tight_layout()

# Show the plot
plt.show()

#Violin plot for the domains and interpretation as markdown
# Melt the DataFrame to long format
df_melted = data.melt(id_vars='Guideline', var_name='Criterion', value_name='Value')

# Create the violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Criterion', y='Value', data=df_melted, inner='quartile', palette='Set3')
plt.xlabel('Criterion')
plt.ylabel('Value')
plt.title('Violin Plot of Criteria Values')
plt.xticks(rotation=45)
#plt.legend()
plt.tight_layout()
plt.show()


# Plot the scatter plot with bubble size for comarision across the main domains
plt.figure(figsize=(10, 6))

# Scatter plot for Rigor of Development
scatter_rd = plt.scatter(data['D3- Rigour of Development'], data['Guideline'], s=400, c='blue', alpha=0.5, label="Rigor of Development")

# Scatter plot for Stakeholder Involvement
scatter_si = plt.scatter(data['D2- Stakeholder Involvement'], data['Guideline'], s=400, c='green', alpha=0.5, label="Stakeholder Involvement")

# Scatter plot for Applicability
scatter_app = plt.scatter(data['D5- Applicability'], data['Guideline'], s=400, c='orange', alpha=0.5, label="Applicability")

# Set labels and title
plt.xlabel("Domain Score in %")
plt.ylabel("Guidelines")
plt.yticks( data['Guideline'])
#plt.title("Comparison of Domain Scores across Guidelines")
plt.legend(loc='lower left')
plt.tight_layout()

# Add grid
plt.grid(True)

# Show the plot
plt.show()

