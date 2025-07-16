# AnsCom-Terminal-MarketOS
AnsCom Terminal is a A real-time crypto profit tracker I built from scratch using Python and data tools like matplotlib It shows live price, % return, and trend graphs — just like a custom TradingView  Terminal and Ui inspired from Bloomberg Terminal. 
However, I didn’t have access to premium APIs for live crypto data or any share/stock data on NASDAQ, NYSE , OTCMKTS OR EURONEXT OR ON NSE/BSE, OR ON HKSE OR SSE .  
So I challenged myself to find a workaround — and ended up using **Selenium** to pull live data directly from **TradingView(whose frequency is fastest)**.

This allowed me to create a system that behaves like a mini trading terminal — made entirely by me.
This project was born purely from curiosity — I wanted to go beyond just watching numbers and truly understand: how do these platforms work under the hood? How are real-time prices fetched? How are profit graphs plotted live? How do drawing tools like those in TradingView function? So I decided not to just use these tools... I wanted to build one.

Since I didn’t have access to paid APIs, I went deep — and built a data scraper using Selenium, pulling live data directly from TradingView to track and analyze crypto movements second-by-second.

🧠 What drove me to build this?

"I just wanted to understand... how do these things work?"From terminal themes to profit plots, to custom UI panels — I built every feature to replicate real-world financial software, while learning the logic behind it.

This wasn't about copying — it was about learning deeply through making. I wanted my hands in the code, my mind in the charts, and my curiosity driving every single feature.

## ⚙️ What This Terminal Can Do (Features)

This is not just a basic graph. Here's what AnsCom Terminal actually does:

- ✅ **Tracks live Bitcoin price** (BTC-USD) every second from TradingView
- 📈 **Calculates your live profit** in dollars for the coin(s) you hold
- 🟢 **Displays a real-time trend graph**, like those seen on Bloomberg terminals
- 🔁 **Live percentage change**, auto-calculated and color-coded (green for up, red for down)
- 📊 **Draw tools built-in**: pencil, line, and % measurement between two points
- 🧠 **Smart annotations**: calculates percentage and price difference between any two clicks
- 📅 Shows the **exact time**, **market status**, and **live trading condition**
- 💡 Includes **SMA (Simple Moving Average)** calculation (5-step)
- 🔥 Custom dark-mode terminal theme (my own design!) that like of Bloomberg Terminal UI
- 🎨 Real-time filled area under the graph — green if you're in profit, red if you're in loss
- 🖼️ Shows profit, price, percentage, SMA, and total value — all live on the screen


Custom theming with high-contrast readability

Terminal-style branding ("AnsCom Terminal")

🕒 Dynamic Time Axis, Live Clock, and Smooth Animation

## 🧰 Technologies Used (Simple Explanation)

| Tool | Why I Used It |
|------|----------------|
| `Selenium` | To grab live BTC price from TradingView (because no APIs were used) |
| `Matplotlib` | To plot the live graphs and design the terminal UI |
| `NumPy` | For profit, SMA, and % calculations |
| `datetime` | For timestamps, market status, time difference between measurements |
| `FancyBboxPatch` | To draw Bloomberg-style boxes around text (for branding) |

## 🧪 How This Actually Works (Behind the Scenes)

Here’s what’s really happening under the hood:

1. **Selenium WebDriver opens TradingView**
   - It automatically opens Chrome, navigates to BTC-USD page
   - It waits a few seconds to load
   - Every 1 second, it grabs:
     - Live price
     - Price change
     - Percentage change

2. **Your profit is calculated**
   - Based on how many coins (`SHARES`) you hold
   - It calculates your net profit and percent return

3. **Matplotlib draws everything**
   - Each second, a new point is added to the graph
   - The entire UI is updated live: price, SMA, percent change, etc.
   - Fill color (green/red) appears under the graph
   - The branding and theme are carefully chosen to mimic Bloomberg

4. **Interactive Tools**
   - You can select from “Pencil”, “Line”, or “Measure %”
   - You can click two points to instantly get:
     - Price difference
     - Time difference
     - % change
   - And yes — you can clear all drawings too 😄

##🌟 What’s next?

## This is just the start. This is underconstruction (although u can run and use the program) and I'm the only one Working here on this terminal. And I would like to add more advance things like stock prediction using machine algorithms and machine learning , An automated chart analyzing. And and automatic order buy and sell execution in upcoming Time For both futures and options and live intraday. it's on the way to  Make it more advanced By life giving the complete access Of buy and sell command to the program . And more feautures like:

Advanced indicators

Full portfolio simulation

Export capabilities

Ticker selection
## How to run it ?
### ✅ Requirements:
- Python 3.8+
- Chrome browser
- ChromeDriver installed (same version as Chrome)
- Libraries: `selenium`, `matplotlib`, `numpy`

### ▶️ Installation:

```bash
pip install selenium matplotlib numpy
