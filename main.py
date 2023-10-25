def main():
    st.title("掲示板アプリ")

    # 新規投稿の入力
    new_post_content = st.text_area("管理者以外記述厳禁", height=100)
    new_post_title = st.text_input("ページ")
    
    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_title and new_post_content:
        try:
            new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)
            if "＠" in new_post_title or "＠" in new_post_content:
                st.warning("禁止ワードが含まれています！")
            else:
                save_post(new_post_title, new_post_content)
                st.success("投稿が保存されました！")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")

    # 保存された投稿の表示
    posts = load_posts()
    st.subheader("保存された投稿")

    if not posts:
        st.info("まだ投稿がありません。")
    else:
        for post in posts:
            # 各タイトルにリンクを付けて表示
            post_url = f"<a href='https://maichan-bord-{urllib.parse.quote(post['title'])}.streamlit.app'>{post['title']}</a>"
            st.subheader(post['title'])
            st.write(post['content'])  # 投稿内容
            st.write(post['timestamp'])  # タイムスタンプ
            st.markdown(post_url, unsafe_allow_html=True)  # リンクを表示
