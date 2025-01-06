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
    # Kullanıcıdan dil seçimi
    language = st.radio("Choose a language / Bir dil seçin:", ("English", "Türkçe"))
    
    # Başlık
    if language == "English":
        st.title("Is It Leap Year or Not?")
    else:
        st.title("Artık Yıl mı Değil mi?")
    
    # Yıl girişi
    year_label = "Enter a year:" if language == "English" else "Bir yıl girin:"
    year = st.number_input(year_label, value=2022, step=1)
    year = int(year)
    is_leap = is_leap_year(year)
    
    # Sonuç
    if language == "English":
        if is_leap:
            st.write(f"{year} is a leap year.")
        else:
            st.write(f"{year} is not a leap year.")
    else:
        if is_leap:
            st.write(f"{year} bir artık yıldır.")
        else:
            st.write(f"{year} bir artık yıl değildir.")

if __name__ == "__main__":
    main()
