from app import Author, db

Author.query.filter_by(id=1).delete()
db.session.commit()
