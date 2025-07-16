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

💡 Features

⚡ Real-time Live Price Fetching (via Selenium from TradingView)

📊 Profit Tracking in USD (based on number of held shares)

📉 Live Trend Graph with Matplotlib, updating every second

🟢 Market Status, Total Value, % Returns, Price Changes

✏️ Interactive Drawing Tools like:

Pencil – Freehand draw on chart

Line – Draw clean support/resistance or trendlines

Measure % – Select 2 points and auto-calculate % and $ change, including time difference!

📌 Bloomberg-style UI

Custom theming with high-contrast readability

Terminal-style branding ("AnsCom Terminal")

🕒 Dynamic Time Axis, Live Clock, and Smooth Animation

🔧 Technologies Used

Python

Selenium (for scraping live market data)

Matplotlib (for real-time plots and interactive UI)

Numpy, Datetime, FuncAnimation, and other core libraries

📌 No API? No Problem.

Due to the lack of a paid API, I leveraged Selenium to simulate a browser and pull live data from TradingView — ensuring that even without API tokens, this system stays completely real-time and accurate.

🌟 What’s next?

This is just the start. My goal is to keep improving it by adding:

Advanced indicators

Full portfolio simulation

Export capabilities

Ticker selection

And someday... a real connection to the market.
