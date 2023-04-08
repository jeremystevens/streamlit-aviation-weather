import streamlit as st
import urllib.request
import re

# Define page title and favicon
st.set_page_config(page_title="My Streamlit Website", page_icon=":airplane:")

# Define functions to fetch aviation weather data
@st.cache
def fetch_weather_data(airport_code):
    url = f"https://www.aviationweather.gov/metar/data?ids={airport_code}&format=raw&hours=0&taf=off&layout=off&date=0"
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
    # Find the first instance of the weather data string
    start_index = html.find(f"{airport_code} ")
    if start_index != -1:
        # Remove any newlines and carriage returns from the weather data string
        weather_data = html[start_index:].split("<br>")[0].replace("\n", "").replace("\r", "")
        return weather_data
    else:
        return None

# Define user interface components
st.write("""
         # My Streamlit Website
         """)

airport_code = st.text_input("Enter an airport code:")
if airport_code:
    try:
        weather_data = fetch_weather_data(airport_code)

        if weather_data is not None:
            st.write(f"""
                     ## Latest Aviation Weather at {airport_code}
                     """)
            st.write(weather_data)
        else:
            st.warning("No weather data found for the given airport code.")
    except:
        st.warning("Invalid airport code.")
