import streamlit as st
import requests
import aviationweather as aw

# Define page title and favicon
st.set_page_config(page_title="My Streamlit Website", page_icon=":airplane:")

# Define functions to fetch aviation weather data
@st.cache
def fetch_weather_data(airport_code):
    url = f"https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString={airport_code}&hoursBeforeNow=1"
    response = requests.get(url)
    return response.content

# Define user interface components
st.write("""
         # My Streamlit Website
         """)

airport_code = st.text_input("Enter an airport code:")
if airport_code:
    weather_data = fetch_weather_data(airport_code)

    if len(weather_data) > 0:
        decoded_data = aw.decode_metar(weather_data)
        st.write(f"""
                 ## Latest Aviation Weather at {airport_code}
                 """)
        st.write(decoded_data.summary)
        st.write(decoded_data.conditions)
    else:
        st.warning("No weather data found for the given airport code.")
