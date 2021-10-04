
import streamlit as st

st.write("""
# Arabic Open Domain Question Answering

""")
_, col1, _ = st.beta_columns(3)
rtl = lambda w: get_display(f"{arabic_reshaper.reshape(w)}")
with col1:
    st.image("logo.png", width=150)
  
    st.markdown(
    """
<style>
p, div, input, label {
  text-align: center;
}
</style>
    """,
    unsafe_allow_html=True,
)
question = st.text_input("ادخل السؤال هنا", value="")
if "؟" not in question:
    question += "؟"         
run_query = st.button("الاجابة")
if run_query:
    # https://discuss.streamlit.io/t/showing-a-gif-while-st-spinner-runs/5084
    with st.spinner("... جاري البحث "):
        results_dict = get_results(question)

    if len(results_dict) > 0:
        st.write("## :الأجابات هي")
        for result in results_dict["results"][:n_answers]:
            annotate_answer(result)
            f"[**المصدر**](<{result['link']}>)"
    else:
        st.write("## لا يوجد اجابات")
