import streamlit as st

# ページ設定
st.set_page_config(page_title="緒方ツールポータル", layout="centered")

# カスタムCSS
st.markdown("""
    <style>
    .credit { text-align: right; font-size: 14px; color: #666; margin-bottom: -20px; }
    .stButton>button { height: 3.5em; font-size: 18px !important; font-weight: bold !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("🌐 緒方ツールポータル")
st.write("使いたいツールを選択してください")
st.markdown("---")

# アプリのリストとURL
# 先頭や途中に全角スペースが入らないよう修正済みです
apps = {
    "🔢 伝送換算アシスト": "https://200-999-o244vkvrcu7wufxndezrc5.streamlit.app/",
    "⚡ 消費電力計算": "https://dbm-w-calc-ogata.streamlit.app/",
    "📡 dBm⇄dBμV変換": "https://dbm-dbuv-conv-ogata.streamlit.app/",
    "📏 電圧降下計算": "https://voltage-drop-ogata.streamlit.app/",
    "⚖️ 質量・重量計算": "https://weight-calc-ogata.streamlit.app/",
    "🌐 IPv4サブネット": "https://ip-calc-ogata.streamlit.app/"
}

# 2列でボタンを配置
cols = st.columns(2)
for i, (name, url) in enumerate(apps.items()):
    with cols[i % 2]:
        st.link_button(name, url, use_container_width=True)

st.markdown("---")
st.caption("※ボタンを押すと各アプリのページに移動します。")
