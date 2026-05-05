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
    "🔢 伝送換算アシスト(200-999)": "https://200-999-o244vkvrcu7wufxndezrc5.streamlit.app/",
     "🔢 伝送換算アシスト(990-FD0)": "https://990-fd0-br5qdwlqpcg6xgzndxrfxk.streamlit.app/",
    "📡 無線設備計算": "https://y2gpx3glcpxabyvquqwsu8.streamlit.app/",
    "📡 dBm⇄dBμV変換": "https://dbm-dbuv-converter-aeqcnqxhxypoemfnmbecwh.streamlit.app/",
    "📡 W ⇄dBm 相互変換": "https://dxzv2ve2tarf3epbjekvk6.streamlit.app/",
     "⚡ 消費電力計算": "https://p-e-i-w-ciq65gzsje57g5t2bjibev.streamlit.app/",
    "📏 電圧降下計算": "https://denatus-kouka-mkzokbttfxvxryb4x9kxe6.streamlit.app/",
    "📐 面積・坪・畳 換算": "https://m9ebpan3hnocsbchjgnc3c.streamlit.app/",
    "⚖️ 質量・重量計算": "https://cx6vhj5b5eaum7yrtghzkm.streamlit.app/",
    "🌐 IPv4サブネット": "https://lan-ip-6a84chs983d8qrywcfi8ek.streamlit.app/",
    "🎨 カラー抵抗計算": "https://lbocbpi8ohzxyhudcamols.streamlit.app/",
}

# 2列でボタンを配置
cols = st.columns(2)
for i, (name, url) in enumerate(apps.items()):
    with cols[i % 2]:
        st.link_button(name, url, use_container_width=True)

st.markdown("---")
st.caption("※ボタンを押すと各アプリのページに移動します。")
