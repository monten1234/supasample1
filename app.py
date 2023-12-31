# import streamlit as st
# import requests

# SUPABASE_URL = "https://clwmzkijmvdpxsgjwniz.supabase.co"
# SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsd216a2lqbXZkcHhzZ2p3bml6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTMzMDU4MzIsImV4cCI6MjAwODg4MTgzMn0.2kpa137KbwfJTUQ2xQLb13SxYaHkCKgVkWaLc3soRDg"
# BUCKET_NAME = "test1"

# def upload_to_supabase(file_contents, file_name):
#     headers = {
#         "Authorization": f"Bearer {SUPABASE_API_KEY}"
#     }
#     response = requests.post(
#         f"{SUPABASE_URL}/storage/v1/object/public/{BUCKET_NAME}/{file_name}",
#         data=file_contents,
#         headers=headers
#     )
#     if response.status_code == 201:
#         st.success("File uploaded successfully!")
#     else:
#         st.error("File upload failed.")

# def main():
#     st.title("Supabase Storage Uploader")
#     file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg", "pdf"])

#     if file:
#         file_contents = file.read()
#         file_name = file.name

#         upload_to_supabase(file_contents, file_name)

# if __name__ == "__main__":
#     main()

import streamlit as st
import os
from supabase import create_client, Client

url: str = "https://clwmzkijmvdpxsgjwniz.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsd216a2lqbXZkcHhzZ2p3bml6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTMzMDU4MzIsImV4cCI6MjAwODg4MTgzMn0.2kpa137KbwfJTUQ2xQLb13SxYaHkCKgVkWaLc3soRDg"
# Supabaseクライアントを作成
supabase: Client = create_client(url, key)

# Streamlitアプリの設定
st.title("Supabase Storage Uploader")
st.write("Upload a file to Supabase Storage")
# ファイルアップロードのインターフェース
file = st.file_uploader("Choose a file", type=["png", "jpg", "jpeg", "xlsx"])
if file:
    st.write("File selected:", file.name)

    # ファイルのアップロード
    bucket_name = "sumple2"
    object_name = f"aaa/{file.name}"
    # urllib.parse.urljoin('aaa','')
    new_file = file.read()  # アップロードするファイルのバイナリデータ
    upload_result = supabase.storage.from_(bucket_name).upload(object_name, new_file)

    if upload_result:
        get_url = supabase.storage.from_(bucket_name).get_public_url(object_name)
        st.write(get_url)
        st.success("File uploaded successfully!")
    else:
        st.error("File upload failed.")
