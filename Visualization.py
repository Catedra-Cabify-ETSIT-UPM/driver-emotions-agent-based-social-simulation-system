#%% [markdown]
import matplotlib.pyplot as plt
import numpy as np


labels = ['SLOW', 'APPROPIATE', 'FAST']
happiness = [10,20,40]
fear = [20, 40, 80]
anger = [5, 10, 20]
anxiety = [2, 4, 8]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, happiness, width, label='Happiness')
rects2 = ax.bar(x + width/2, fear, width, label='Fear')
rects3 = ax.bar(x + width/2, anger, width, label='Anger')
rects4 = ax.bar(x + width/2, anxiety, width, label='Anxiety')



# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Drivers')
ax.set_title('Scores by speed level and emotion.')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

# fig.tight_layout()

plt.show()


# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([['SLOW', 10, 20, 10, 30], ['APPROPIATE', 20, 25, 15, 25], ['FAST', 12, 15, 19, 6]],
                  columns=['Speed', 'Happiness', 'Fear', 'Anger', 'Anxiety'])

df.plot(x='Speed',
        kind='bar',
        stacked=False,
        title='Score by speed level and emotion')

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Happiness = [12, 30, 1]
Fear = [28, 6, 16]
Anger = [29, 3, 24]
Anxiety = [28, 6, 16]

# Set position of bar on X axis
br1 = np.arange(len(Happiness))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Happiness, width = barWidth,
		edgecolor ='grey', label ='Happiness')
plt.bar(br2, Fear, width = barWidth,
		edgecolor ='grey', label ='Fear')
plt.bar(br3, Anger, width = barWidth,
		edgecolor ='grey', label ='Anger')
plt.bar(br4, Anxiety, width = barWidth,
		edgecolor ='grey', label ='Anxiety')

# Adding Xticks
plt.xlabel('Speed', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Happiness))],
		['SLOW', 'APPROPIATE', 'FAST'])

plt.legend()
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Happiness = [12, 30, 1]
Fear = [28, 6, 16]
Anger = [29, 3, 24]
Anxiety = [28, 6, 16]

# Set position of bar on X axis
br1 = np.arange(len(Happiness))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Happiness, width = barWidth,
		edgecolor ='grey', label ='Happiness')
plt.bar(br2, Fear, width = barWidth,
		edgecolor ='grey', label ='Fear')
plt.bar(br3, Anger, width = barWidth,
		edgecolor ='grey', label ='Anger')
plt.bar(br4, Anxiety, width = barWidth,
		edgecolor ='grey', label ='Anxiety')

# Adding Xticks
plt.xlabel('Acceleration', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Happiness))],
		['SLOW', 'APPROPIATE', 'FAST'])

plt.legend()
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Happiness = [12, 30]
Fear = [28, 6]
Anger = [29, 3]
Anxiety = [28, 6]

# Set position of bar on X axis
br1 = np.arange(len(Happiness))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Happiness, width = barWidth,
		edgecolor ='grey', label ='Happiness')
plt.bar(br2, Fear, width = barWidth,
		edgecolor ='grey', label ='Fear')
plt.bar(br3, Anger, width = barWidth,
		edgecolor ='grey', label ='Anger')
plt.bar(br4, Anxiety, width = barWidth,
		edgecolor ='grey', label ='Anxiety')

# Adding Xticks
plt.xlabel('Braking', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Happiness))],
		['GENTLE', 'ABRUPT'])

plt.legend()
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Happiness = [12, 30]
Fear = [28, 6]
Anger = [29, 3]
Anxiety = [28, 6]

# Set position of bar on X axis
br1 = np.arange(len(Happiness))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Happiness, width = barWidth,
		edgecolor ='grey', label ='Happiness')
plt.bar(br2, Fear, width = barWidth,
		edgecolor ='grey', label ='Fear')
plt.bar(br3, Anger, width = barWidth,
		edgecolor ='grey', label ='Anger')
plt.bar(br4, Anxiety, width = barWidth,
		edgecolor ='grey', label ='Anxiety')

# Adding Xticks
plt.xlabel('Steering', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Happiness))],
		['LOW', 'HIGH'])

plt.legend()
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.15
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Happiness = [12, 30]
Fear = [28, 6]
Anger = [29, 3]
Anxiety = [28, 6]

# Set position of bar on X axis
br1 = np.arange(len(Happiness))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Happiness, width = barWidth,
		edgecolor ='grey', label ='Happiness')
plt.bar(br2, Fear, width = barWidth,
		edgecolor ='grey', label ='Fear')
plt.bar(br3, Anger, width = barWidth,
		edgecolor ='grey', label ='Anger')
plt.bar(br4, Anxiety, width = barWidth,
		edgecolor ='grey', label ='Anxiety')

# Adding Xticks
plt.xlabel('Response Time', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Happiness))],
		['LOW', 'HIGH'])

plt.legend()
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Reckless = [12, 30, 1]
Anxious = [28, 6, 16]
Angry = [29, 3, 24]
Careful = [28, 6, 16]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Reckless, width = barWidth,
		edgecolor ='grey', label ='Reckless')
plt.bar(br2, Anxious, width = barWidth,
		edgecolor ='grey', label ='Anxious')
plt.bar(br3, Angry, width = barWidth,
		edgecolor ='grey', label ='Angry')
plt.bar(br4, Careful, width = barWidth,
		edgecolor ='grey', label ='Careful')

# Adding Xticks
plt.xlabel('Speed', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['SLOW', 'APPROPIATE', 'FAST'])

plt.legend()
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Reckless = [12, 30, 1]
Anxious = [28, 6, 16]
Angry = [29, 3, 24]
Careful = [28, 6, 16]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Reckless, width = barWidth,
		edgecolor ='grey', label ='Reckless')
plt.bar(br2, Anxious, width = barWidth,
		edgecolor ='grey', label ='Anxious')
plt.bar(br3, Angry, width = barWidth,
		edgecolor ='grey', label ='Angry')
plt.bar(br4, Careful, width = barWidth,
		edgecolor ='grey', label ='Careful')

# Adding Xticks
plt.xlabel('Acceleration', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['SLOW', 'APPROPIATE', 'FAST'])

plt.legend()
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Reckless = [12, 30]
Anxious = [28, 6]
Angry = [29, 3]
Careful = [28, 6]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Reckless, width = barWidth,
		edgecolor ='grey', label ='Reckless')
plt.bar(br2, Anxious, width = barWidth,
		edgecolor ='grey', label ='Anxious')
plt.bar(br3, Angry, width = barWidth,
		edgecolor ='grey', label ='Angry')
plt.bar(br4, Careful, width = barWidth,
		edgecolor ='grey', label ='Careful')

# Adding Xticks
plt.xlabel('Braking', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['GENTLE', 'ABRUPT'])

plt.legend()
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Reckless = [12, 30]
Anxious = [28, 16]
Angry = [29, 3]
Careful = [28, 6]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Reckless, width = barWidth,
		edgecolor ='grey', label ='Reckless')
plt.bar(br2, Anxious, width = barWidth,
		edgecolor ='grey', label ='Anxious')
plt.bar(br3, Angry, width = barWidth,
		edgecolor ='grey', label ='Angry')
plt.bar(br4, Careful, width = barWidth,
		edgecolor ='grey', label ='Careful')

# Adding Xticks
plt.xlabel('Steering', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['LOW', 'HIGH'])

plt.legend()
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
Reckless = [12, 30]
Anxious = [28, 16]
Angry = [29, 3]
Careful = [28, 6]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Reckless, width = barWidth,
		edgecolor ='grey', label ='Reckless')
plt.bar(br2, Anxious, width = barWidth,
		edgecolor ='grey', label ='Anxious')
plt.bar(br3, Angry, width = barWidth,
		edgecolor ='grey', label ='Angry')
plt.bar(br4, Careful, width = barWidth,
		edgecolor ='grey', label ='Careful')

# Adding Xticks
plt.xlabel('Response Time', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['LOW', 'HIGH'])

plt.legend()
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
AngerStress = [12, 30, 1]
AnxietyStress = [28, 6, 16]
NoStress = [29, 3, 24]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]


# Make the plot
plt.bar(br1, AngerStress, width = barWidth,
		edgecolor ='grey', label ='Anger-Stress')
plt.bar(br2, AnxietyStress, width = barWidth,
		edgecolor ='grey', label ='Anxiety-Stress')
plt.bar(br3, NoStress, width = barWidth,
		edgecolor ='grey', label ='No Stress')


# Adding Xticks
plt.xlabel('Speed', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['SLOW', 'APPROPIATE', 'FAST'])

plt.legend()
plt.show()

# %%
# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
AngerStress = [12, 30, 1]
AnxietyStress = [28, 6, 16]
NoStress = [29, 3, 24]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]


# Make the plot
plt.bar(br1, AngerStress, width = barWidth,
		edgecolor ='grey', label ='Anger-Stress')
plt.bar(br2, AnxietyStress, width = barWidth,
		edgecolor ='grey', label ='Anxiety-Stress')
plt.bar(br3, NoStress, width = barWidth,
		edgecolor ='grey', label ='No Stress')


# Adding Xticks
plt.xlabel('Acceleration', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['SLOW', 'APPROPIATE', 'FAST'])

plt.legend()
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
AngerStress = [12, 30]
AnxietyStress = [28, 6]
NoStress = [29, 3]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]


# Make the plot
plt.bar(br1, AngerStress, width = barWidth,
		edgecolor ='grey', label ='Anger-Stress')
plt.bar(br2, AnxietyStress, width = barWidth,
		edgecolor ='grey', label ='Anxiety-Stress')
plt.bar(br3, NoStress, width = barWidth,
		edgecolor ='grey', label ='No Stress')


# Adding Xticks
plt.xlabel('Braking', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['GENTLE', 'ABRUPT'])

plt.legend()
plt.show()

# %%
# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
AngerStress = [12, 30]
AnxietyStress = [28, 6]
NoStress = [29, 3]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]


# Make the plot
plt.bar(br1, AngerStress, width = barWidth,
		edgecolor ='grey', label ='Anger-Stress')
plt.bar(br2, AnxietyStress, width = barWidth,
		edgecolor ='grey', label ='Anxiety-Stress')
plt.bar(br3, NoStress, width = barWidth,
		edgecolor ='grey', label ='No Stress')


# Adding Xticks
plt.xlabel('Steering', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['LOW', 'HIGH'])

plt.legend()
plt.show()

# %%
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.20
fig = plt.subplots(figsize =(12, 8))

# set height of bar
AngerStress = [12, 30]
AnxietyStress = [28, 6]
NoStress = [29, 3]

# Set position of bar on X axis
br1 = np.arange(len(Reckless))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]


# Make the plot
plt.bar(br1, AngerStress, width = barWidth,
		edgecolor ='grey', label ='Anger-Stress')
plt.bar(br2, AnxietyStress, width = barWidth,
		edgecolor ='grey', label ='Anxiety-Stress')
plt.bar(br3, NoStress, width = barWidth,
		edgecolor ='grey', label ='No Stress')


# Adding Xticks
plt.xlabel('Response Time', fontweight ='bold', fontsize = 15)
plt.ylabel('Drivers', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(Reckless))],
		['LOW', 'HIGH'])

plt.legend()
plt.show()