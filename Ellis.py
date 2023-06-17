#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[2]:


# Import dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[3]:


stroke_df = pd.read_csv("Resources/healthcare-dataset-stroke-data-cleaned.csv")
stroke_df


# In[4]:


# Filter the rows based on the conditions (heart disease/urban)
filtered_rows = stroke_df[(stroke_df['Residence_type'] == 'Urban') & (stroke_df['heart_disease'] == 1)]

# Count the number of rows
row_count = len(filtered_rows)

print("The number of people with heart disease who live in an urban residence type is", row_count)

# Filter the rows based on the conditions (heart disease/rural)
filtered_rows = stroke_df[(stroke_df['Residence_type'] == 'Rural') & (stroke_df['heart_disease'] == 1)]

# Count the number of rows
row_count = len(filtered_rows)

print("The number of people with heart disease who live in a rural residence type is", row_count)


# In[5]:


# Data
residence_type = ["Urban", "Rural"]
people_with_HeartDisease = [142, 134]
x_axis = np.arange(len(people_with_HeartDisease))

# Create a bar chart based upon the above data
plt.bar(x_axis, people_with_HeartDisease, color="orchid", align="center")


# In[6]:


# Give the chart a title, x label, and y label
plt.title("Heart Disease vs Residence Type")
plt.xlabel("Residence Type")
plt.ylabel("Number of People with Heart Disease")
plt.show()


# In[7]:


# Create the ticks for bar chart's x axis
tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, residence_type)
plt.show()

# Set the limits of the x axis
plt.xlim(-0.75, len(x_axis)-0.25)
plt.show()

# Set the limits of the y axis
plt.ylim(0, max(people_with_HeartDisease)+10)
plt.show()


# In[8]:


# Labels for the sections of our pie chart
labels = ["Urban", "Rural"]
plt.title('Heart Disease in Urban and Rural Areas')

# The values of each section of the pie chart
sizes = [142, 134]

# The colors of each section of the pie chart
colors = ["darkseagreen", "lightskyblue"]

# Tells matplotlib to separate the "Humans" section from the others
explode = (0.1, 0)

# Creates the pie chart based upon the values above & automatically finds the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=90)
plt.show()


# In[9]:


# Filter the rows based on the conditions (stroke/urban)
filtered_rows = stroke_df[(stroke_df['Residence_type'] == 'Urban') & (stroke_df['stroke'] == 1)]

# Count the number of rows
row_count = len(filtered_rows)

print("The number of people who've had a stroke and live in an urban residence type is", row_count)

# Filter the rows based on the conditions (stroke/rural)
filtered_rows = stroke_df[(stroke_df['Residence_type'] == 'Rural') & (stroke_df['stroke'] == 1)]

# Count the number of rows
row_count = len(filtered_rows)

print("The number of people who've had a stroke and live in a rural residence type is", row_count)


# In[10]:


# Data
residence_type = ["Urban", "Rural"]
people_with_stroke = [135, 114]
x_axis = np.arange(len(people_with_stroke))

# Create a bar chart based upon the above data
plt.bar(x_axis, people_with_stroke, color="salmon", align="center")


# In[11]:


# Give the chart a title, x label, and y label
plt.title("Stroke vs Residence Type")
plt.xlabel("Residence Type")
plt.ylabel("Number of People who've suffered a Stroke")
plt.show()


# In[12]:


# Create the ticks for bar chart's x axis
tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, residence_type)
plt.show()

# Set the limits of the x axis
plt.xlim(-0.75, len(x_axis)-0.25)
plt.show()

# Set the limits of the y axis
plt.ylim(0, max(people_with_stroke)+10)
plt.show()


# In[13]:


# Labels for the sections of our pie chart
labels = ["Urban", "Rural"]
plt.title('Stroke in Urban and Rural Areas')

# The values of each section of the pie chart
sizes = [135, 114]

# The colors of each section of the pie chart
colors = ["burlywood", "darkturquoise"]

# Tells matplotlib to separate the "Humans" section from the others
explode = (0.1, 0)

# Creates the pie chart based upon the values above & automatically finds the percentages of each part of the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=90)
plt.show()


# In[ ]:





# In[ ]:




