import json
from datetime import datetime	from datetime import datetime
import pytz	import pytz
import urllib.parse


# 禁止ワードのリスト	# 禁止ワードのリスト
banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]	banned_words = ["馬鹿", "禁止ワード2", "禁止ワード3"]
@@ -17,24 +18,33 @@ def check_post_content(title, content):
    return title, content	    return title, content


def save_post(title, content):	def save_post(title, content):
    now = datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")	    now = datetime.now(pytz.timezone("Asia/Tokyo"))
    post = {"title": title, "content": content, "timestamp": now}	    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    post = {"title": title, "content": content, "timestamp": now_str}
    with open('posts.json', 'a') as file:	    with open('posts.json', 'a') as file:
        file.write(json.dumps(post))	        file.write(json.dumps(post))
        file.write('\n')	        file.write('\n')


def load_posts():	def load_posts():
    with open('posts.json', 'r') as file:	    with open('posts.json', 'r') as file:
        lines = file.readlines()	        lines = file.readlines()
        return [json.loads(line) for line in lines]	        posts = [json.loads(line.strip()) for line in lines]

        # タイムスタンプを日本時間に変換
        for post in posts:
            timestamp = datetime.strptime(post['timestamp'], "%Y-%m-%d %H:%M:%S")
            timestamp = pytz.timezone("Asia/Tokyo").localize(timestamp)
            post['timestamp'] = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        return posts


def main():	def main():
    st.title("掲示板アプリ")	    st.title("掲示板アプリ")


    # 新規投稿の入力	    # 新規投稿の入力
    new_post_title = st.text_input("タイトル")	    new_post_content = st.text_area("管理者以外記述厳禁", height=100)
    new_post_content = st.text_area("新規投稿", height=100)	    new_post_title = st.text_input("ページ")

    
    # 投稿ボタンが押された場合	    # 投稿ボタンが押された場合
    if st.button("投稿する") and new_post_title and new_post_content:	    if st.button("投稿する") and new_post_title and new_post_content:
        new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)	        new_post_title, new_post_content = check_post_content(new_post_title, new_post_content)
@@ -52,12 +62,12 @@ def main():
        st.info("まだ投稿がありません。")	        st.info("まだ投稿がありません。")
    else:	    else:
        for post in posts:	        for post in posts:
            st.text(post["title"])	            # 各タイトルにリンクを付けて表示
            st.text(post["content"])	            post_url = f"<a href='https://maichan-bord-{urllib.parse.quote(post['title'])}.streamlit.app'>{post['title']}</a>"
            st.text("投稿時刻: " + post.get("timestamp", ""))	            st.subheader(post['content'])
            st.write(post['timestamp'])  # タイムスタンプを表示
            st.markdown(post_url, unsafe_allow_html=True)
            st.markdown("---")	            st.markdown("---")


if __name__ == "__main__":	if __name__ == "__main__":
    main()	    main()


0 comments on commit d40632d
@oga491
 