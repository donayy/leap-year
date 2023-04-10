import streamlit as st

def is_leap_year(year):
    """
    Returns True if the given year is a leap year, False otherwise.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def main():
    st.title("Leap Year Checker")
    
    year = st.number_input("Enter a year:")
    is_leap = is_leap_year(year)
    
    if is_leap:
        st.write(f"{year} is a leap year.")
    else:
        st.write(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
