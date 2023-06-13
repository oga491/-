
import streamlit as st
import pyson


def save_post(post):
    with pyson.db('posts.json') as db:
        db.append(post)


def load_posts():
    with pyson.db('posts.json') as db:
        return db


def main():
    st.title("掲示板アプリ")

    # 新規投稿の入力
    new_post = st.text_area("新規投稿", height=100)

    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post:
        save_post(new_post)
        st.success("投稿が保存されました！")

    # 保存された投稿の表示
    posts = load_posts()
    st.subheader("保存された投稿")
    for post in posts:
        st.text(post)
        st.markdown("---")


if __name__ == "__main__":
    main()
