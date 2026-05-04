import streamlit as st

st.set_page_config(page_title="緒方ツールポータル", layout="centered")

st.title("緒方エンジニアリング・ポータル")
st.markdown("---")

# アプリのリストとURL（ご自身の実際のURLに書き換えてください）
apps = {
    "⚡ 消費電力計算": "https://xxxx-power.streamlit.app",
    "📡 dBm⇄dBμV変換": "https://xxxx-dbm.streamlit.app",
    "🌐 IPv4サブネット": "https://xxxx-net.streamlit.app",
    "📏 電圧降下計算": "https://xxxx-drop.streamlit.app",
    "⚖️ 質量・重量計算": "https://xxxx-mass.streamlit.app",
    "📐 面積・畳換算": "https://xxxx-area.streamlit.app",
    "🎨 カラー抵抗識別": "https://xxxx-resistor.streamlit.app",
}

# 2列でボタンを配置
cols = st.columns(2)
for i, (name, url) in enumerate(apps.items()):
    with cols[i % 2]:
        if st.button(name, use_container_width=True):
            st.markdown(f'<meta http-equiv="refresh" content="0; URL={url}">', unsafe_allow_html=True)
            st.link_button("開く", url)

st.markdown("---")
st.caption("各ツールを個別に開いて「ホーム画面に追加」すると便利です。")

このポータルアプリを一つ作成し、スマホのホーム画面に登録しておけば、いつでも迷わずに全ての計算ツールにアクセスできるようになります。ぜひお試しください！
