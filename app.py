import streamlit as st

# ページ設定
st.set_page_config(page_title="緒方ツールポータル", layout="centered")

# カスタムCSSで見た目を整える
st.markdown("""
    <style>
    .credit { text-align: right; font-size: 14px; color: #666; margin-bottom: -20px; }
    .stButton>button { height: 3em; font-size: 20px !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("🌐 緒方ツールポータル")
st.write("使いたいツールを選択してください")
st.markdown("---")

# アプリのリストとURL
# ※ https://xxxx.streamlit.app の部分を、ご自身の実際のアプリURLに書き換えてください
apps = {
　　"📱 伝送換算アシスト (200-999)": "https://200-999-o244vkvrcu7wufxndezrc5.streamlit.app/",
    "📱 伝送換算アシスト (990h-FD0h)": "https://200-999-o244vkvrcu7wufxndezrc5.streamlit.app/",
    "⚡ 消費電力計算": "https://share.streamlit.io/ogatakun0113-dot/dbm-w-calc/main/app.py",
    "📡 dBm⇄dBμV変換": "https://share.streamlit.io/ogatakun0113-dot/dbm-dbuv-conv/main/app.py",
    "🌐 IPv4サブネット": "https://share.streamlit.io/ogatakun0113-dot/ip-calc/main/app.py",
    "📏 電圧降下計算": "https://share.streamlit.io/ogatakun0113-dot/voltage-drop/main/app.py",
    "⚖️ 質量・重量計算": "https://share.streamlit.io/ogatakun0113-dot/weight-calc/main/app.py",
    "📐 面積・畳換算": "https://share.streamlit.io/ogatakun0113-dot/area-calc/main/app.py",
    "🎨 カラー抵抗識別": "https://share.streamlit.io/ogatakun0113-dot/resistor-color/main/app.py",
}

# 2列でボタンを配置
cols = st.columns(2)
for i, (name, url) in enumerate(apps.items()):
    with cols[i % 2]:
        st.link_button(name, url, use_container_width=True)

st.markdown("---")
st.caption("各ツールを個別に開いて、ブラウザのメニューから「ホーム画面に追加」すると便利です。")
