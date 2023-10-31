import pandas as pd
import datetime
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color = ["#c287e8", "#eecfd4", "#efb9cb", "#e6adec", "#cfd4c5"])

df = pd.read_csv(r'KickstarterData.csv', low_memory = False)
groupby_categ = df['CATEGORY'].value_counts(dropna = TRUE, sort = True)
df_Catego_count = groupby_categ.reset_index()
df_Catego_count.columns = ['Category', 'Counts']

fig1, ax1 = plt.subplots()
ax1.bar(df_catego_count['Category'], df_catego_count['Counts'])
ax1.set_title("Categories of Kickstarter Projects")
ax1.set_xlabel("Categories")
ax1.set_ylabel("Count")
plt.xticks(rotation = 45)

groupby_curr = df['PROJECT_CURRENCY'].value_counts(dropna = True, sort = True)
df_curr_count = groupby_curr.reset_index()
df_curr_count.columns = ['Currency', 'Counts']

fig2, ax2 = plt.subplots()
ax2.barh(df_curr_count['Currency'], df_curr_count['Counts'])
ax2.set_title("Currency Paid For Kickstarter Projects")
ax2.set_xlabel("Currency")
ax2.set_ylabel("Count")
plt.xticks(rotation=45)

groupby_state = df['STATE'].value_counts(dropna=True, sort=True)
df_State_count = groupby_state.reset_index()
df_State_count.columns = ['State', 'Counts']

fig3, ax3 = plt.subplots()
ax3.pie(df_State_count["Counts"], labels=df_State_count["State"], autopct='%1.1f%%')
ax3.set_title('Outcome of Kickstarter Projects')
ax3.axis('equal')

df['LAUNCHED_DATE'] = pd.to_datetime(df['LAUNCHED_DATE'])

df["Year"] = df['LAUNCHED_DATE'].dt.strftime('%Y')

count_launch_years = df["Year"].value_counts(dropna=True, sort=True).sort_values()
df_year_count = count_launch_years.reset_index()
df_year_count.columns = ['Year', 'Counts']

ig4, ax4 = plt.subplots()
ax4.plot(df_year_count['Year'], df_year_count['Counts'])
ax4.set_title('Number of Kickstarter Projects Per Year')
ax4.set_xlabel('Year')
ax4.set_ylabel('Count')

root = tk.Tk()
root.title("Kickstart Project Analytics Between 2009-2015")
root.state('zoomed')

side_frame = tk.Frame(root, bg="#eecfd4")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame,bg="#eecfd4", fg="#eecfd4", font=25)
label.pack(pady=50, padx=20)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.draw()
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.draw()
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

canvas3 = FigureCanvasTkAgg(fig3, lower_frame)
canvas3.draw()
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.draw()
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

root.mainloop()
