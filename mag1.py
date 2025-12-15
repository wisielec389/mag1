import streamlit as st

# Magazyn - lista towarów (słowniki)
magazyn = []

# Funkcja do dodawania towaru do magazynu
def dodaj_towar(nazwa, cena, ilosc):
    magazyn.append({'nazwa': nazwa, 'cena': cena, 'ilosc': ilosc})

# Funkcja do usuwania towaru z magazynu
def usun_towar(index):
    if 0 <= index < len(magazyn):
        magazyn.pop(index)

# Ustawienia strony
st.set_page_config(page_title="Magazyn Towarów", page_icon="📦", layout="wide")

# Nagłówek aplikacji
st.title("Prosty Program Magazynu Towarów")

# Sekcja dodawania towaru
st.header("Dodaj Nowy Towar")

nazwa = st.text_input("Nazwa towaru")
cena = st.number_input("Cena towaru (PLN)", min_value=0.0, step=0.01)
ilosc = st.number_input("Ilość towaru", min_value=1, step=1)

if st.button("Dodaj Towar"):
    if nazwa and cena > 0 and ilosc > 0:
        dodaj_towar(nazwa, cena, ilosc)
        st.success(f"Dodano towar: {nazwa}, Cena: {cena} PLN, Ilość: {ilosc}")
    else:
        st.error("Proszę uzupełnić wszystkie pola!")

# Sekcja wyświetlania magazynu
st.header("Stan Magazynu")

if len(magazyn) > 0:
    for i, towar in enumerate(magazyn):
        st.write(f"{i+1}. **{towar['nazwa']}** | Cena: {towar['cena']} PLN | Ilość: {towar['ilosc']}")
        if st.button(f"Usuń {towar['nazwa']}", key=f"usun_{i}"):
            usun_towar(i)
            st.experimental_rerun()  # Odświeżenie strony po usunięciu towaru
else:
    st.write("Brak towarów w magazynie.")

# Opcjonalnie sekcja do usuwania towaru po indeksie
st.sidebar.header("Opcje")
usun_index = st.sidebar.number_input("Wprowadź numer towaru do usunięcia (1-based index)", min_value=1, max_value=len(magazyn), step=1)
if st.sidebar.button("Usuń Towar z Listy"):
    usun_towar(usun_index - 1)
    st.sidebar.success(f"Towar nr {usun_index} został usunięty.")
    st.experimental_rerun()


