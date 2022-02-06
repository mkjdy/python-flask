from app import Author, db

# donna = Author.query.get(3)
donna = Author.query.filter_by(id=3).first()

donna.title = 'Romantic Birds (Edit)'
db.session.commit()
