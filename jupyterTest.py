# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt

#%%
msg = "Hello"
print(msg)

# %%
msg2 = "Hello again"
a = 3
b = 2
c = a + b
print(msg2)
print(c)

# %%
msg3 = "Hello a third time"
test = 3
test2 = 88

# %%
## matplotlib practice

# create data
x = np.linspace(0,10,100)
y = 4 + 2*np.sin(2*x)

# figure
fig, simple_chart = plt.subplots()
simple_chart.plot(x,y,linewidth=1.5)
simple_chart.set(xlim=(0,10), xticks=np.arange(1,10),
                 ylim=(0,8), yticks=np.arange(1,8))

plt.title("Sine Function")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# %%

## altair practice
from vega_datasets import data

cars_data = data.cars()
alt.Chart(cars_data).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
).interactive()