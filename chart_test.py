import sys
import os
import io
from ohlc_sitcom import *
from chart_generator import CustomCandlestick, scale_ohlc_data


# 1. GET DATA (Using the imported mock data function)
original_data = get_ohlc('degenerative-sitcom',cg_key='')

print(original_data)

scale_factor = 1_000_000_000
scaled_data = scale_ohlc_data(original_data, scale_factor)
# 2. CREATE AND PLOT CHART using the imported class
chart = CustomCandlestick(scaled_data, width=0.4)
chart.plot(
    title="",
    xlabel="Time",
    ylabel="Mcap"
)

# 3. SAVE CHART TO MEMORY BUFFER
photo_buffer = chart.show_chart()
