import streamlit as st
from avwx import Metar, Station
from avwx.exceptions import InvalidRequest
from avwx.token import Token

# Define page title and favicon
st.set_page_config(page_title="My Streamlit Website", page_icon=":airplane:")

# Define functions to fetch aviation weather data
@st.cache
def fetch_weather_data(airport_code):
    station = Station.from_icao(airport_code)
    report = Metar(station, Token()).report
    return report.raw

# Define user interface components
st.write("""
         # My Streamlit Website
         """)

airport_code = st.text_input("Enter an airport code:")
if airport_code:
    try:
        weather_data = fetch_weather_data(airport_code)

        if len(weather_data) > 0:
            st.write(f"""
                     ## Latest Aviation Weather at {airport_code}
                     """)
            st.write(weather_data)
        else:
            st.warning("No weather data found for the given airport code.")
    except InvalidRequest as e:
        st.warning(str(e))
