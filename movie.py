movies = {'액션':['다크 나이트', '어벤져스', '매드 맥스'], '코미디':['슈렉', '미니언즈', '행오버'], '로맨스':['노트북', '어바웃 타임', '라라랜드'], '공포':['컨저링', '겟 아웃', '그것'], 'SF':['인터스텔라', '인셉션', '매트릭스']}

def recommend_movies(genre):
  if genre in movies:
    print(f"추천하는 {genre} 영화:")
    for movie in movies[genre]:
      print(f"- {movie}")
  else:
    print("죄송합니다. 해당 장르의 영화는 없습니다.")

def add_movie(genre, new_movie):
  if genre in movies:
    movies[genre].append(new_movie)
    print(f"'{new_movie}'가 {genre} 장르에 추가되었습니다!")
  else:
          print("해당 장르가 없습니다.")

print("영화 추천 프로그램에 오신 것을 환영합니다!")

while True:
          print(f"1. 영화 추천받기")
          print("2. 영화 추가하기")
          print('3. 종료')
          choice = input("메뉴를 선택하세요 (1/2/3): ").strip()

          if choice == "1":
              genre = input("장르를 입력하세요 (액션, 코미디, 로맨스, 공포, SF): ").strip()
              recommend_movies(genre)
          elif choice == "2":
              gener = input("장르를 입력하세요 (액션, 코미디, 로맨스, 공포, SF): ").strip()
              new_movie = input("{genre} 장르에 추가할 영화 제목을 입력하세요: ").strip()
              add_movie(genre, new_movie)
          elif choice == "3":
              print(f"프로그램을 종료합니다.")
              break
          else:
            print(f"잘못된 입력입니다. 다시 시도하세요.")


