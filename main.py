import json
from datetime import datetime
import pytz
import urllib.parse
import streamlit as st

# ...

# 各投稿にgoodとbadの評価を保持するための辞書
post_ratings = {}

def check_post_content(title, content):
    # ...

def save_post(title, content):
    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    post = {"title": title, "content": content, "timestamp": now_str, "good": 0, "bad": 0}
    with open('posts.json', 'a') as file:
        file.write(json.dumps(post))
        file.write('\n')
    post_ratings[title] = {"good": 0, "bad": 0}  # 評価カウンターを初期化

def load_posts():
    with open('posts.json', 'r') as file:
        lines = file.readlines()
        posts = [json.loads(line.strip()) for line in lines]

        # ...

        # 評価カウンターを初期化
        for post in posts:
            post_ratings[post["title"]] = {"good": 0, "bad": 0}

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
            save_post(new_post_title, new_post_content)

    # 投稿一覧を表示
    posts = load_posts()
    if not posts:
        st.info("まだ投稿がありません。")
    else:
        for post in posts:
            # ...

            # GoodボタンとBadボタンを追加
            col1, col2 = st.beta_columns(2)
            if col1.button(f"Good ({post_ratings[post['title']]['good']})"):
                post_ratings[post['title']]['good'] += 1
            if col2.button(f"Bad ({post_ratings[post['title']]['bad']})"):
                post_ratings[post['title']]['bad'] += 1

