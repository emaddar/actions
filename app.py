import streamlit as st
import datetime

def main():
    # Set page title
    st.title("Current Date and Time")

    # Get the current date and time
    current_date_time = datetime.datetime.now()

    # Format the date and time as a string
    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

    # Display the formatted date and time on the app
    st.write("Current date and time:", formatted_date_time)

if __name__ == "__main__":
    main() 