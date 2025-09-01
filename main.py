import streamlit as st 
from streamlit_option_menu import option_menu
# st.title("Vinsup Infotech")
# st.header("Full Stack")
# st.subheader("Python full Stack")
# st.text("My text")
# st.write("`New` Project")


# a = 10
# st.write(a)
# st.code("""public class Main {
#   public static void main(String[] args) {
#     System.out.println("Hello World");
#   }
# }
#         """, language="java")
# st.metric("Python", "20%", "-25")

with st.sidebar:
    data = option_menu(
      
      menu_title = "Vinsup",
      options = ["Home", "About", "Services"]
      
    
    )
if data == "Home":
  st.title("Registration Page")
  st.text_input("Name")
  st.text_input("E-mail")
  st.number_input("Phone Number")
  st.radio("Gender", options= ["Male", "Female"])
  st.selectbox("State", options= ["Tamil Nadu", "Kerala", "Andra Pradesh"])
  st.multiselect("Skills", options= ["HTML", "Java", "Python", "Data Science"])
  st.slider("Age", 0, 100)
  st.date_input("Date of Birth")
  st.file_uploader("Choose your file")
  st.text_area("Write Something")
  st.checkbox("Terms and Conditions")
  st.button("Register")
elif data == "About":
  st.title("About Page")
  col1, col2 = st.columns(2)
  with col1:
    st.write("Gandhi was the youngest child of his father’s fourth wife. His father— Karamchand Gandhi.")
  with col2:
    st.image("https://tse2.mm.bing.net/th/id/OIP.B39-1EvwOFXOffOfIKZT0AHaEK?w=5797&h=3261&rs=1&pid=ImgDetMain&o=7&rm=3")

elif data == "Services":
  st.title("Services Page")

