import streamlit as st

# 영화 데이터
movies = {
    '액션': ['다크 나이트', '어벤져스', '매드 맥스'],
    '코미디': ['슈렉', '미니언즈', '행오버'],
    '로맨스': ['노트북', '어바웃 타임', '라라랜드'],
    '공포': ['컨저링', '겟 아웃', '그것'],
    'SF': ['인터스텔라', '인셉션', '매트릭스']
}

# 영화 추천 함수
def recommend_movies(genre):
    if genre in movies:
        st.subheader(f"추천하는 {genre} 영화 🎬")
        for movie in movies[genre]:
            st.write(f"- {movie}")
    else:
        st.warning("해당 장르의 영화는 없습니다.")

# 영화 추가 함수
def add_movie(genre, new_movie):
    if genre in movies:
        movies[genre].append(new_movie)
        st.success(f"'{new_movie}'가 {genre} 장르에 추가되었습니다!")
    else:
        st.error("해당 장르가 없습니다.")

# 앱 UI
st.title("🎥 영화 추천 프로그램")
menu = st.sidebar.radio("메뉴를 선택하세요", ["영화 추천받기", "영화 추가하기"])

if menu == "영화 추천받기":
    genre = st.selectbox("장르를 선택하세요", list(movies.keys()))
    if st.button("추천 영화 보기"):
        recommend_movies(genre)

elif menu == "영화 추가하기":
    genre = st.selectbox("영화를 추가할 장르를 선택하세요", list(movies.keys()))
    new_movie = st.text_input("추가할 영화 제목을 입력하세요")
    if st.button("영화 추가"):
        if new_movie.strip():
            add_movie(genre, new_movie.strip())
        else:
            st.warning("영화 제목을 입력해주세요!")

# 현재 영화 데이터 확인
with st.expander("📌 현재 영화 데이터 보기"):
    st.json(movies)
