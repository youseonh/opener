# # api/datdabase.py
# from mongoengine import connect
# from .models.rank import RankModel

# # MongoDB 데이터베이스
# MONGO_DTATBASE = "graphql-example"
# # MongoDB 주소
# MONGO_HOST = "mongomock://localhost"

# # Database 연결
# conn = connect(MONGO_DTATBASE, host=MONGO_HOST, alias="default")


# # 기초 데이터 Insert 함수 - 임의의 기초 데이터 입력
# def init_db():
#     rank = RankModel(name="kim", mode="3x3", score=2,
#                      isMobile=False, reg_dttm="20200413170848")
#     rank.save()  # Insert (mongoengine에서 제공하는 insert 기능)

#     rank = RankModel(name="choi", mode="3x3", score=128,
#                      isMobile=False, reg_dttm="20200413170848")
#     rank.save()  # Insert

#     rank = RankModel(name="lee", mode="4x4", score=1024,
#                      isMobile=False, reg_dttm="20200413170848")
#     rank.save()  # Insert

#     rank = RankModel(name="heo", mode="4x4", score=16,
#                      isMobile=False, reg_dttm="20200413170848")
#     rank.save()  # Insert
