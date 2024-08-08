import streamlit as st

st.title(" title : jagraj")
st.header("header" )
st.subheader("subheader")
st.text("text")


st.markdown("# This is a Heading")
st.markdown("## This is a Subheading")
st.markdown("This is a paragraph with **bold** text and *italic* text.")
st.markdown("[This is a link](https://www.streamlit.io)")

st.success("successful")
st.info("hello world")
st.warning("alert")
st.error("issue occuered")
st.exception(ZeroDivisionError("div is not possible"))

st.write(range(1,10))
st.write(1+2)

st.code("x = 10\n"
        "for i in range(x)\n "
        "   print(i)")


if(st.checkbox("male")):
    st.write("you are male")


radioButton=st.radio("select : ", ("Male", "Female"))
if (radioButton == "Male"):
    st.write ("you are male")

selectBox= st.selectbox("choose : ", ["A", "B","C","D"])
st.write("You have chosen : ", selectBox)


multiSelect = st.multiselect("choose : " , ["a","b","c","d","e","f"])
st.write("you have selected : ", len(multiSelect), "options")


if (st.button("click")):
    st.write("thanks for clicking")


vol= st.slider("select the volume : ", 1,100, step = 5)
st.write("Volume is : ", vol)


username= st.text_input("username : ")
password= st.text_input("password : ", type = "password")



txt= st.text_area("eneter 500 words : ")
st.write(txt)


age = st.number_input("enter the age : ", 1, 100)
if (age):
    st.write("the age is : ", age)

date = st.date_input("date ")

time = st.time_input("time")
