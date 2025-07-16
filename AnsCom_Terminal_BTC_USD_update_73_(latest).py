import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.widgets import RadioButtons, Button
from matplotlib.lines import Line2D
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from matplotlib.animation import FuncAnimation
import numpy as np
from datetime import datetime, timedelta
# I Have explained everything by comments and the logic i executed
# Number of shares
SHARES = 1 # Number of shares to track (for crypto u can assume a the number of coin)

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.tradingview.com/symbols/BTCUSD/?exchange=CRYPTO")
driver.maximize_window()
time.sleep(3)

# Data for live plotting
profits = []
share_prices = []
timestamps = []
percentage_changes = []
moving_averages = []

# --- [THEME CHANGE] - BLOOMBERG TERMINAL / DARK MODE THEME ---
plot_bgcolor = '#121212'
axes_color = '#181818'
line_color_profit = '#00A2FF'
text_color_primary = '#E0E0E0'
text_color_secondary = '#888888'
grid_color = '#333333'
accent_color_green = '#44D400'
accent_color_red = '#FF3B30'
accent_color_neutral = '#AAAAAA'
fill_color_positive = accent_color_green
fill_color_negative = accent_color_red
sma_color = '#FFC400'

# Apply the new theme using rcParams
plt.rcParams['axes.facecolor'] = axes_color
plt.rcParams['figure.facecolor'] = plot_bgcolor
plt.rcParams['axes.edgecolor'] = grid_color
plt.rcParams['axes.labelcolor'] = text_color_secondary
plt.rcParams['xtick.color'] = text_color_secondary
plt.rcParams['ytick.color'] = text_color_secondary
plt.rcParams['grid.color'] = grid_color
plt.rcParams['text.color'] = text_color_primary
plt.rcParams['font.family'] = ['Consolas', 'Menlo', 'Courier New', 'monospace']
plt.rcParams['font.weight'] = 'normal'
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'normal'

# Initialize matplotlib figure and axis
fig, ax = plt.subplots(figsize=(14, 8), facecolor=plot_bgcolor)

# --- [MODIFIED] BLOOMBERG-STYLE BRANDING WITH BOX ---
brand_fontsize = 24
brand_fontname = 'sans-serif'
brand_weight = 'heavy'
text_zorder = 3
patch_zorder = 2

brand_box = FancyBboxPatch((0.01, 0.925), width=0.215, height=0.065,
                           boxstyle="round,pad=0.01,rounding_size=0.01",
                           facecolor=axes_color, edgecolor=grid_color,
                           transform=fig.transFigure, clip_on=False, zorder=patch_zorder)
fig.patches.append(brand_box)

fig.text(0.018, 0.98, 'AnsCom', transform=fig.transFigure, fontsize=brand_fontsize,
         weight=brand_weight, color=text_color_primary, ha='left', va='top',
         fontname=brand_fontname, zorder=text_zorder)

fig.text(0.122, 0.98, 'Terminal', transform=fig.transFigure, fontsize=brand_fontsize,
         weight=brand_weight, color=sma_color, ha='left', va='top',
         fontname=brand_fontname, zorder=text_zorder)
# --- END MODIFIED SECTION ---

line, = ax.plot([], [], label="Profit ($)", color=line_color_profit, linewidth=2.0, linestyle='-')

ax.set_title(f"AT: (INTRADAY)BTC_USD LIVE TRACKING and Profit Analysis for {SHARES} coin", fontsize=18, color=text_color_primary, weight='bold', pad=25, fontname='Consolas')
ax.set_xlabel("Time", fontsize=14, color=text_color_secondary, labelpad=10)
ax.set_ylabel("Profit ($)", fontsize=14, color=text_color_secondary, labelpad=10)

legend = ax.legend(fontsize=12, loc='upper left', facecolor=axes_color, edgecolor=grid_color, labelcolor=text_color_primary, framealpha=1.0)
for text in legend.get_texts():
    text.set_fontweight('bold')

ax.grid(True, axis='y', linestyle='--', color=grid_color, alpha=0.7, linewidth=0.8)
ax.grid(True, axis='x', linestyle=':', color=grid_color, alpha=0.5, linewidth=0.5)

ax.tick_params(axis='both', which='major', direction='out', length=6, width=1, colors=text_color_secondary, pad=8)
for spine in ax.spines.values():
    spine.set_color(grid_color)

ax.axhline(0, color=sma_color, linestyle='--', linewidth=1.2, alpha=0.8)

bbox_props = dict(boxstyle='round,pad=0.4', facecolor=axes_color, edgecolor=grid_color, alpha=1.0)
text_x_position, text_y_position = 1.01, 0.99

live_profit_text = ax.text(text_x_position, text_y_position, '', transform=ax.transAxes, fontsize=13, verticalalignment='top', horizontalalignment='left', color=accent_color_green, weight='bold', bbox=bbox_props)
live_price_text = ax.text(text_x_position, text_y_position - 0.08, '', transform=ax.transAxes, fontsize=13, verticalalignment='top', horizontalalignment='left', color=text_color_primary, weight='bold', bbox=bbox_props)
live_change_text = ax.text(text_x_position, text_y_position - 0.16, '', transform=ax.transAxes, fontsize=11, verticalalignment='top', horizontalalignment='left', color=text_color_secondary, weight='bold', bbox=bbox_props)
live_pct_change_text = ax.text(text_x_position, text_y_position - 0.24, '', transform=ax.transAxes, fontsize=11, verticalalignment='top', horizontalalignment='left', color=line_color_profit, weight='bold', bbox=bbox_props)
live_sma_text = ax.text(text_x_position, text_y_position - 0.32, '', transform=ax.transAxes, fontsize=11, verticalalignment='top', horizontalalignment='left', color=sma_color, weight='bold', bbox=bbox_props)
price_change_by_day_text = ax.text(text_x_position, text_y_position - 0.40, '', transform=ax.transAxes, fontsize=11, verticalalignment='top', horizontalalignment='left', color=text_color_primary, weight='bold', bbox=bbox_props)
total_amount_text = ax.text(text_x_position, text_y_position - 0.48, '', transform=ax.transAxes, fontsize=13, verticalalignment='top', horizontalalignment='left', color=text_color_primary, weight='bold', bbox=bbox_props)
market_status_text = ax.text(text_x_position, 0.20, '', transform=ax.transAxes, fontsize=12, verticalalignment='top', horizontalalignment='left', weight='bold', bbox=bbox_props)
live_indicator_text = ax.text(text_x_position, 0.13, '● Live', transform=ax.transAxes, fontsize=12, verticalalignment='top', horizontalalignment='left', color=accent_color_red, weight='bold', bbox=bbox_props)
live_time_text = ax.text(text_x_position, 0.06, '', transform=ax.transAxes, fontsize=12, verticalalignment='top', horizontalalignment='left', color=text_color_primary, weight='bold', bbox=bbox_props)

prev_price = None
watermark_text = ax.text(0.99, 0.01, 'AnswerCom Terminal', transform=ax.transAxes, fontsize=11, weight='bold', verticalalignment='bottom', horizontalalignment='right', color=text_color_secondary, alpha=0.7)
fill_positive, fill_negative = None, None

# --- [NEW] DRAWING AND ANALYSIS TOOLS ---

class DrawingManager:
    """Manages interactive drawing and analysis on the chart."""
    def __init__(self, ax, fig, data_providers):
        self.ax = ax
        self.fig = fig
        self.get_share_prices, self.get_timestamps = data_providers
        self.active_tool = 'None'
        self.start_point = None
        self.temp_artist = None
        self.drawn_artists = []
        self.is_drawing = False

    def set_tool(self, label):
        """Callback for the RadioButtons to set the active tool."""
        self.active_tool = label.replace(' ', '_') # Use underscore for consistency
        self.start_point = None
        if self.temp_artist:
            self.temp_artist.remove()
            self.temp_artist = None
        self.fig.canvas.draw_idle()

    def on_press(self, event):
        if event.inaxes != self.ax or self.active_tool == 'None':
            return
        self.is_drawing = True
        self.start_point = (event.xdata, event.ydata)

        if self.active_tool in ['Line', 'Pencil']:
            self.temp_artist = Line2D([self.start_point[0]], [self.start_point[1]],
                                      color=sma_color, linestyle='--', linewidth=1.5)
            self.ax.add_line(self.temp_artist)
        elif self.active_tool == 'Measure_%':
            self.temp_artist = Line2D([self.start_point[0]], [self.start_point[1]],
                                      color=accent_color_green, marker='o', markersize=5)
            self.ax.add_line(self.temp_artist)
        self.fig.canvas.draw_idle()

    def on_motion(self, event):
        if not self.is_drawing or not self.start_point or event.inaxes != self.ax:
            return

        if self.active_tool == 'Pencil':
            x, y = self.temp_artist.get_data()
            self.temp_artist.set_data(np.append(x, event.xdata), np.append(y, event.ydata))
        elif self.active_tool in ['Line', 'Measure_%']:
            self.temp_artist.set_data([self.start_point[0], event.xdata], [self.start_point[1], event.ydata])

        self.fig.canvas.draw_idle()

    def on_release(self, event):
        if not self.is_drawing or not self.start_point:
            return
        self.is_drawing = False
        end_point = (event.xdata, event.ydata)

        # Finalize the drawing
        if self.active_tool == 'Pencil' or self.active_tool == 'Line':
            final_line = self.temp_artist
            final_line.set_linestyle('-') # Solid line for final drawing
            self.drawn_artists.append(final_line)
        elif self.active_tool == 'Measure_%' and self.temp_artist:
            self.temp_artist.remove()
            self.calculate_and_draw_measurement(self.start_point[0], end_point[0])

        self.temp_artist = None
        self.start_point = None
        self.fig.canvas.draw_idle()

    def calculate_and_draw_measurement(self, x_start, x_end):
        prices = self.get_share_prices()
        times = self.get_timestamps()
        if not prices or len(prices) < 2: return

        # Find closest data points
        idx_start = np.clip(int(round(x_start)), 0, len(prices) - 1)
        idx_end = np.clip(int(round(x_end)), 0, len(prices) - 1)
        if idx_start == idx_end: return

        # Ensure start is before end
        if idx_start > idx_end:
            idx_start, idx_end = idx_end, idx_start

        price_start, price_end = prices[idx_start], prices[idx_end]
        time_start_str, time_end_str = times[idx_start], times[idx_end]
        time_format = "%H:%M:%S"
        time_start = datetime.strptime(time_start_str, time_format)
        time_end = datetime.strptime(time_end_str, time_format)
        
        # Handle day crossover
        if time_end < time_start:
            time_end += timedelta(days=1)
        
        time_delta = time_end - time_start
        price_delta = price_end - price_start
        pct_change = (price_delta / price_start) * 100 if price_start != 0 else 0

        color = accent_color_green if price_delta >= 0 else accent_color_red
        
        # Draw connecting line on main price plot (using profit scale)
        profit_start = (price_start - prices[0]) * SHARES if prices else 0
        profit_end = (price_end - prices[0]) * SHARES if prices else 0

        line = Line2D([idx_start, idx_end], [profit_start, profit_end],
                      color=color, linestyle=':', marker='o', markersize=4, linewidth=2)
        
        # Create annotation text
        text_content = (f"Δ Price: ${price_delta:,.2f}\n"
                        f"Δ Return: {pct_change:.2f}%\n"
                        f"Δ Time: {str(time_delta)}")
        
        text_y_pos = (profit_start + profit_end) / 2
        text_x_pos = (idx_start + idx_end) / 2
        
        annotation = self.ax.text(text_x_pos, text_y_pos, text_content, color=text_color_primary,
                                  ha='center', va='center', fontsize=10, weight='bold',
                                  bbox=dict(boxstyle='round,pad=0.3', facecolor=plot_bgcolor,
                                            edgecolor=color, alpha=0.9))
        
        self.ax.add_line(line)
        self.drawn_artists.extend([line, annotation])

    def clear_drawings(self, event):
        """Removes all user-drawn artists from the plot."""
        for artist in self.drawn_artists:
            artist.remove()
        self.drawn_artists.clear()
        self.fig.canvas.draw_idle()

# --- END NEW SECTION ---


def is_market_open():
    now = datetime.now()
    return True # Crypto market is 24/7

def update(frame):
    global prev_price, fill_positive, fill_negative
    try:
        LIVE_UPDATE = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[2]/span[1]").text  # live price(intraday) by which the stock or crypto currency has changed
        LIVE_PRICE = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[1]/span[1]").text   # Live price of that stock or share or coin  
        LIVE_CHANGE = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[1]/div[1]/div/div/div/div[3]/div[1]/div/div[2]/span[2]').text  # precentage by which the stock or crypto currency has changed 

        LIVE_UPDATE = LIVE_UPDATE.replace("+", "").replace("−", "-").strip()
        price_change = float(LIVE_UPDATE.replace(",", ""))
        live_price = float(LIVE_PRICE.replace(",", ""))

        profit = SHARES * price_change
        total_amount = SHARES * live_price
        percentage_change = (price_change / live_price) * 100 if live_price != 0 else 0

        profits.append(profit)
        share_prices.append(live_price)
        current_dt = datetime.now()
        timestamps.append(current_dt.strftime("%H:%M:%S"))
        percentage_changes.append(percentage_change)

        if len(share_prices) >= 5: moving_averages.append(np.mean(share_prices[-5:]))
        elif share_prices: moving_averages.append(np.mean(share_prices))
        else: moving_averages.append(np.nan)

        x_data = np.arange(len(profits))
        line.set_data(x_data, profits)

        min_profit = min(min(profits) if profits else 0, -1)
        max_profit = max(max(profits) if profits else 0, 1)
        padding = (max_profit - min_profit) * 0.2
        ax.set_ylim(min_profit - padding, max_profit + padding)
        ax.set_xlim(0, max(len(profits) - 1, 1))

        max_ticks = 15
        step = max(1, len(timestamps) // max_ticks)
        ax.set_xticks(x_data[::step])
        ax.set_xticklabels(timestamps[::step], rotation=45, ha='right', fontsize=10)

        if fill_positive: fill_positive.remove()
        if fill_negative: fill_negative.remove()
        if len(profits) > 1:
            profits_array = np.array(profits)
            fill_positive = ax.fill_between(x_data, profits_array, 0, where=profits_array >= 0, facecolor=fill_color_positive, alpha=0.25, interpolate=True)
            fill_negative = ax.fill_between(x_data, profits_array, 0, where=profits_array < 0, facecolor=fill_color_negative, alpha=0.25, interpolate=True)

        live_profit_text.set_text(f"Profit: ${profit:.2f}")
        live_price_text.set_text(f"Price: ${live_price:.2f}")
        live_change_text.set_text(f"Day Change: {LIVE_CHANGE}")
        live_pct_change_text.set_text(f"Change %: {percentage_change:.2f}%")
        if not np.isnan(moving_averages[-1]): live_sma_text.set_text(f"SMA (5): ${moving_averages[-1]:.2f}")
        else: live_sma_text.set_text("SMA (5): N/A")
        price_change_by_day_text.set_text(f"Day Price Change: {LIVE_UPDATE}")
        total_amount_text.set_text(f"Total Value:$ {total_amount:,.2f}")

        market_open = is_market_open()
        market_status_text.set_text("Market Status: Open" if market_open else "Market Status: Closed")
        market_status_text.set_color(accent_color_green)
        live_indicator_text.set_color(accent_color_green)
        live_time_text.set_text(f"Time: {current_dt.strftime('%H:%M:%S')}")

        if prev_price is not None:
            if live_price > prev_price: price_color, line_color = accent_color_green, accent_color_green
            elif live_price < prev_price: price_color, line_color = accent_color_red, accent_color_red
            else: price_color, line_color = accent_color_neutral, line_color_profit
        else: price_color, line_color = accent_color_neutral, line_color_profit

        line.set_color(line_color)
        live_price_text.set_color(price_color)
        live_change_text.set_color(price_color if price_change != 0 else accent_color_neutral)
        live_pct_change_text.set_color(price_color if price_change != 0 else line_color_profit)
        price_change_by_day_text.set_color(price_color if price_change != 0 else accent_color_neutral)
        live_profit_text.set_color(accent_color_green if profit >= 0 else accent_color_red)

        prev_price = live_price

    except Exception as e:
        print(f"Error during update: {e}")

    # Return all artists that FuncAnimation should manage
    return (line, fill_positive, fill_negative, live_profit_text, live_price_text,
            live_change_text, live_pct_change_text, live_sma_text, price_change_by_day_text,
            total_amount_text, market_status_text, live_indicator_text, live_time_text)

# --- [NEW] SETUP DRAWING MANAGER AND UI WIDGETS ---

# Create data provider functions for the drawing manager
data_providers = (lambda: share_prices, lambda: timestamps)
drawing_manager = DrawingManager(ax, fig, data_providers)

# Connect the manager's methods to the figure's canvas events
fig.canvas.mpl_connect('button_press_event', drawing_manager.on_press)
fig.canvas.mpl_connect('motion_notify_event', drawing_manager.on_motion)
fig.canvas.mpl_connect('button_release_event', drawing_manager.on_release)

# Create and style the UI for tool selection
tool_ax = fig.add_axes([0.015, 0.01, 0.2, 0.15], frameon=False)
# ##########################################################################
# ############################ THIS BLOCK IS FIXED ###########################
# ##########################################################################
tool_buttons = RadioButtons(
    tool_ax, ('None', 'Pencil', 'Line', 'Measure %'),
    activecolor=sma_color,
    label_props={'color': [text_color_primary], 'fontsize': [10]},
    radio_props={'edgecolor': [grid_color]*4, 's': [40]*4}
)
# ##########################################################################
tool_buttons.on_clicked(drawing_manager.set_tool)

# Create and style the "Clear" button
clear_ax = fig.add_axes([0.18, 0.02, 0.07, 0.04])
clear_button = Button(clear_ax, 'Clear All', color=axes_color, hovercolor=grid_color)
clear_button.label.set_color(text_color_primary)
clear_button.label.set_fontweight('bold')
clear_button.on_clicked(drawing_manager.clear_drawings)

# --- END NEW SECTION ---

# Start live graph animation
ani = FuncAnimation(fig, update, interval=1000, blit=False)

# Graceful termination
try:
    # Adjusted rect to make space for UI at top and bottom
    plt.tight_layout(rect=[0, 0.05, 0.85, 0.94], pad=2.5)
    plt.show()
except KeyboardInterrupt:
    print("Program stopped by the user.")
finally:
    driver.quit()
    print("WebDriver closed.")



# made by Aditya Narayan Singh
# location : REPUBLIC OF INDIA
# DATE:19th March 2025
# code upodated: "72" times
