from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)
db = client.get_default_database()

posts = db['posts']
new_blog = {
    'title': 'Feel',
    'author': 'Suân Xơn',
    'content' : '''(Our class is so fun, Best wishes for next C4E classes)
    Tiếu ngạo giang hồ đọc mấy chương
    Thấy bao nhân vật của đời thường
    Mưu thần chước quỷ cầu danh lợi
    Khẩu phật tâm xà mộng bá vương
    Ngậm máu phun người mồm ố bẩn
    Giấu tay ném đá nghệ am tường
    Đôi đàng hắc bạch nào hơn kém
    Cửu kiếm tung hoành trấn bốn phương '''

}
posts.insert_one(new_blog)
