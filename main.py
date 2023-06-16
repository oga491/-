import streamlit as st
import json
from datetime import datetime

# ...

def save_post(title, content):
    post = {
        "title": title,
        "content": content,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 投稿された時刻を追加
    }
    with open('posts.json', 'a') as file:
        json.dump(post, file)
        file.write('\n')

def load_posts():
    with open('posts.json', 'r') as file:
        return [json.loads(line) for line in file]

def main():
    st.title("掲示板アプリ")

    # ...

    # 保存された投稿の表示
    posts = load_posts()
    st.subheader("保存された投稿")

    if not posts:
        st.info("まだ投稿がありません。")
    else:
        for post in posts:
            st.text(f"タイトル: {post['title']}")
            st.text(f"投稿内容: {post['content']}")
            if "timestamp" in post:
                st.text(f"投稿時刻: {post['timestamp']}")  # 投稿された時刻を表示
            st.markdown("---")

if __name__ == "__main__":
    main()