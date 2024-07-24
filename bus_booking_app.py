import streamlit as st
import pandas as pd

# Load your dataset
df = pd.read_csv("red_bus_final_data.csv")

# Streamlit App
def main():
    st.title('Bus Booking App')
    st.write('Explore available buses and book your journey!')

    st.write('### Available Buses:')
    st.dataframe(df)

    # Sidebar filters
    st.sidebar.title('Filter Options')
    
    # Dropdown filter for Route Name
    route_names = df['Bus_Route_Name'].unique()
    selected_route = st.sidebar.selectbox('Select Route Name', route_names)

    # Dropdown filter for Bus Type
    bus_types = df['Bus_Type'].unique()
    selected_bus_type = st.sidebar.selectbox('Select Bus Type', bus_types)

    # Slider filters
    min_rating = st.sidebar.slider('Minimum Rating', min_value=0.0, max_value=5.0, value=0.0, step=0.1)
    max_price = st.sidebar.slider('Maximum Price', min_value=0.0, max_value=500.0, value=500.0, step=10.0)
    seat_filter = st.sidebar.slider('Minimum Seats Available', min_value=0, max_value=50, value=0, step=1)

    # Apply filters
    filtered_df = df[(df['Bus_Route_Name'] == selected_route) &
                     (df['Bus_Type'] == selected_bus_type) &
                     (df['Star_Rating'] >= min_rating) &
                     (df['Price'] <= max_price) &
                     (df['Seat_Available'] >= seat_filter)]

    st.write('### Filtered Buses:')
    st.dataframe(filtered_df)

if __name__ == '__main__':
    main()
