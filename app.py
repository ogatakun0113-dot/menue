import streamlit as st

# ページ設定
st.set_page_config(page_title="緒方ツールBOX", layout="centered")

# カスタムCSS
st.markdown("""
    <style>
    .credit { text-align: right; font-size: 14px; color: #666; margin-bottom: -20px; }
    .stButton>button { height: 3.5em; font-size: 18px !important; font-weight: bold !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)
st.title("🌐 緒方ツールBOX")
st.write("使いたいツールを選択してください")
st.markdown("---")

# アプリのリストとURL
# 指定箇所以外は元の順番を維持しています
apps = [
    # 1行目
    ("🔢 伝送値換算(200-999)(DEC)", "https://200-999-o244vkvrcu7wufxndezrc5.streamlit.app/"),
    ("🌐 IPv4サブネット", "https://lan-ip-6a84chs983d8qrywcfi8ek.streamlit.app/"), # 右1列目へ移動
    
    # 2行目
    ("🔢 伝送値換算(990-FD0)(HEX)", "https://990-fd0-br5qdwlqpcg6xgzndxrfxk.streamlit.app/"),
    ("🔍 ポートスキャンツール", "https://port-scan-xxxxx.streamlit.app/"), # 右2列目へ移動
    
    # 3行目
    ("🔢 伝送値換算(3200-FA00)(HEX)", "https://denatus-kouka-aktoharzrfntzg3ujbemx3.streamlit.app/"),
    ("⚡ 消費電力計算", "https://p-e-i-w-ciq65gzsje57g5t2bjibev.streamlit.app/"),
    
    # 4行目
    ("📡 dBm⇄dBμV変換", "https://dbm-dbuv-converter-aeqcnqxhxypoemfnmbecwh.streamlit.app/"),
    ("📏 電圧降下計算", "https://denatus-kouka-mkzokbttfxvxryb4x9kxe6.streamlit.app/"),
    
    # 5行目
    ("📡 W ⇄ dBμV 変換", "https://w-db-v-5oemhzumvdhiaf4shewlhp.streamlit.app/"),
    ("📐 面積・坪・畳 換算", "https://m9ebpan3hnocsbchjgnc3c.streamlit.app/"),
    
    # 6行目
    ("📡 W ⇄ dBm 変換", "https://dxzv2ve2tarf3epbjekvk6.streamlit.app/"),
    ("⚖️ 質量・重量計算", "https://cx6vhj5b5eaum7yrtghzkm.streamlit.app/"),
    
    # 7行目
    ("📡 ＶＳＷＲ計算", "https://y2gpx3glcpxabyvquqwsu8.streamlit.app/"), # 左7列目へ移動
    ("🎨 カラー抵抗計算", "https://lbocbpi8ohzxyhudcamols.streamlit.app/"),

    # 8行目
    ("📡 同軸ケーブルロス計算", "https://coaxial-loss-xxxxx.streamlit.app/"), # 左8列目へ移動
    ("⚡ コンデンサー容量・種類判別", "https://kondensa-fnudpeexwnfu7mz4dgziam.streamlit.app/"),

    # 9行目
    ("📉 アッテネータ計算", "https://attenuator-calc-xxxxx.streamlit.app/"), # 左9列目へ移動
    ("🔌 オームの法則計算", "https://ohm-calc-xxxxx.streamlit.app/"), # 維持

    # 10行目
    ("🔋 バッテリー持続計算", "https://battery-calc-xxxxx.streamlit.app/"), # 維持
    ("", ""), 
]

# 2列でボタンを配置
cols = st.columns(2)
for i, (name, url) in enumerate(apps):
    with cols[i % 2]:
        if name:
            st.link_button(name, url, use_container_width=True)

st.markdown("---")
st.caption("※ボタンを押すと各アプリのページに移動します。")
