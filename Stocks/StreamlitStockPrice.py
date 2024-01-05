import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime 

plt.style.use('ggplot')



class Main():

    
    def __new__(self):
        tickerSymbol = st.text_input('Please Enter a Valid Stock Ticker!', 'GOOGL')

        start_date = st.sidebar.date_input('start date', datetime.date(2012,1,1))
        end_date = st.sidebar.date_input('end date', datetime.datetime.now())

        st.write(f"""

        # Simple Stock Price App

        Shown are the stock closing price and volume of {tickerSymbol}!

        """)


        tickerData = yf.Ticker(tickerSymbol)

        df = tickerData.history(period='id', start=start_date, end=end_date)

        st.line_chart(df.Close, y='Close')
        st.write()
        st.line_chart(df.Volume, y='Volume')


if __name__ == '__main__':
    Main()