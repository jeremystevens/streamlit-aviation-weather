import streamlit as st
import requests
import metar

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
        decoded_data = metar.parse(weather_data.decode())
        st.write(f"""
                 ## Latest Aviation Weather at {airport_code}
                 """)
        st.write(f"Report time: {decoded_data.time}")
        st.write(f"Station: {decoded_data.station}")
        st.write(f"Temperature: {decoded_data.temperature_c}°C / {decoded_data.temperature_f}°F")
        st.write(f"Dew point: {decoded_data.dewpoint_c}°C / {decoded_data.dewpoint_f}°F")
        st.write(f"Visibility: {decoded_data.visibility_km} km / {decoded_data.visibility_mi} mi")
        st.write(f"Wind: {decoded_data.wind_speed_kt} kt, direction {decoded_data.wind_direction}")
    else:
        st.warning("No weather data found for the given airport code.")
