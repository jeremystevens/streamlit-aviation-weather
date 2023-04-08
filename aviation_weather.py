import streamlit as st
import urllib.request
import re
import string
# Define page title and favicon
st.set_page_config(page_title="Aviation Weather App", page_icon=":airplane:")

# Define functions to fetch aviation weather data
@st.cache
def fetch_weather_data(airport_code):
    url = f"https://www.aviationweather.gov/metar/data?ids={airport_code}&format=raw&hours=0&taf=off&layout=off&date=0"
    with urllib.request.urlopen(url) as response:
        html = response.read().decode()
    # Find the first instance of the weather data string
    start_index = html.find(f"{airport_code} ")
    if start_index != -1:
        # Remove any HTML tags and newlines from the weather data string
        weather_data = re.sub("<.*?>", "", html[start_index:].split("<br>")[0]).replace("\n", "")
        return weather_data
    else:
        return None

# Define user interface components
st.write("""
         # Aviation Weather
         ### enter airport icao below
         """)

airport_code = st.text_input("Enter an airport code:")
if any(char in string.ascii_lowercase for char in airport_code):
    # Convert all lowercase letters to uppercase
    airport_code = airport_code.upper()
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
