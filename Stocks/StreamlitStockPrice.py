# import yfinance as yf
import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt
import datetime 
# import numpy as np
from stock_functions import (plot_mean_reversals,)
# import pendulum
# plt.style.use('ggplot')



class Main():

    
    def __new__(self):
        cols = st.columns(5)
        with cols[0]:
            ticker_symbol = st.text_input('Please Enter a Valid Stock Ticker!', 'GOOGL')
        with cols[1]:
            short_ma = st.number_input('Input the short moving average', min_value=1, value=20)
        with cols[2]:
            long_ma = st.number_input('Input the long moving average', min_value=1, value=200)
        with cols[3]:
            show_bbs = st.checkbox(label=f'Add Bollinger Bands (SMA{short_ma})', value=False)

        ticker_name = ticker_symbol
        start_date = st.sidebar.date_input('start date', datetime.date(2018,1,1))
        end_date = st.sidebar.date_input('end date', datetime.datetime.now())

        fig, ax, up_reversals, down_reversals = plot_mean_reversals(ticker_symbol=ticker_symbol, start_date=start_date, end_date=end_date, short_ma=short_ma, long_ma=long_ma, show_bbs=show_bbs)
        
        st.pyplot(fig)


if __name__ == '__main__':
    Main()



        # reversal_points = st.columns(2)
        # ups = pd.DataFrame(up_reversals, columns=['Date','Reversal Price'])
        # downs = pd.DataFrame(down_reversals, columns=['Date', 'Reversal Price'])
        # ups['Type'] = 'Up'
        # downs['Type'] = 'Down'
        # st.write('Mean Reversals:')
        # st.dataframe(pd.concat([ups, downs]).sort_values('Date', ascending=False).set_index('Date'))

        # try:
        #     latest_up = up_reversals[-1]

        #     # if latest_up > latest_down:
        #     #     st.write(f'{ticker_symbol} is in an uptrend')
        #     # else:
        #     #     st.write(f'{ticker_symbol} is in a downtrend')

        #     with reversal_points[0]:
        #         st.write(f"##### Latest Up Reversal:")
        #         st.write(f"{(datetime.datetime.now().date() - latest_up[0].date()).days} Days Ago")
        #         st.write(f"{latest_up[0].date()} : {round(latest_up[1],2)}")
        # except:
        #     st.write(f'No Upwards Mean Reversals Found For {ticker_name}')  
        # try:
                
        #     latest_down = down_reversals[-1]

        #     with reversal_points[1]:
        #         st.write(f"##### Latest Down Reversal:")
        #         st.write(f"{(datetime.datetime.now().date() - latest_down[0].date()).days} Days Ago")
        #         st.write(f"{latest_down[0].date()} : {round(latest_down[1],2)}")
        # except:
        #     st.write(f'No Downwards Mean Reversals Found For {ticker_name}')  
        # Plot Figure
