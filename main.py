import json
from datetime import datetime
import pytz
import urllib.parse
import streamlit as st

# 禁止ワードのリスト
banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]

# 各投稿にGoodとBadの評価を保持するための辞書のリスト
posts = []

def check_post_content(title, content):
    # 禁止ワードが含まれているかチェック
    for word in banned_words:
        if word in title or word in content:
            st.warning("禁止ワードが含まれています！")
            return "", ""
    return title, content

def save_post(title, content):
    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    post = {"title": title, "content": content, "timestamp": now_str, "good": 0, "bad": 0}
    posts.append(post)  # 新しい投稿をリストに追加

def load_posts():
    # ファイルから読み込む部分を削除し、リストから直接読み込むように変更
    return posts

def main():
    st.title("掲示板アプリ")

    # 新規投稿の入力
    new_post_content = st.text_area("管理者以外記述厳禁", height=100)
    new_post_title = st.text_input("ページ")

    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_title and new_post_content:
        new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)
        if new_post_title and new_post_content:
            # 新しい投稿を保存する前に現在の投稿を読み込む
            posts = load_posts()
            save_post(new_post_title, new_post_content)

    # 投稿一覧を表示
    posts = load_posts()
    if not posts:
        st.info("まだ投稿がありません。")
    else:
        for post in posts:
            # 各タイトルにリンクを付けて表示
            post_url = f"<a href='https://maichan-bord-{urllib.parse.quote(post['title'])}.streamlit.app'>{post['title']}</a>"
            st.subheader(post['title'])  # タイトルを表示
            st.write(post['content'])
            st.write(post['timestamp'])  # タイムスタンプを表示

            # GoodボタンとBadボタンを追加
            col1, col2 = st.columns(2)
            good_button = col1.button(f"Good ({post['good']})", key=f"good_{post['title']}")
            bad_button = col2.button(f"Bad ({post['bad']})", key=f"bad_{post['title']}")
            if good_button:
                post['good'] += 1
            if bad_button:
                post['bad'] += 1

            # 評価カウンターを表示
            st.write(f"Good: {post['good']}, Bad: {post['bad']}")

            # タイトルへのリンクを表示
            st.markdown(post_url, unsafe_allow_html=True)
            st.markdown("---")

if __name__ == "__main__":
    main()
