# app.py
import streamlit as st
import json

st.set_page_config(page_title="汤臣倍健体质测试", layout="centered")
st.title("汤臣倍健体质测试")
st.markdown("请根据您的日常感觉选择每题的答案：")

tizhi_types = [
    '平和质', '气虚质', '阳虚质', '阴虚质', '痰湿质',
    '湿热质', '血瘀质', '气郁质', '特禀质'
]
scores = {t: 0 for t in tizhi_types}

with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

user_answers = []
for idx, q in enumerate(questions):
    st.subheader(f"第{idx+1}题")
    ans = st.radio(q['text'], ['是', '否'], key=idx)
    user_answers.append(ans)

if st.button("提交并查看结果"):
    for q, ans in zip(questions, user_answers):
        selected = 'A' if ans == '是' else 'B'
        for t, v in q['score'].get(selected, {}).items():
            scores[t] += v

    st.success("✅ 您的体质分析结果如下：")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for t, s in sorted_scores:
        st.write(f"{t}：{s} 分")

    st.markdown(f"### 🧬 您最可能的体质类型是：**{sorted_scores[0][0]}**")
