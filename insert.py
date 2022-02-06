from app import Author, db
donna = Author('Donna Reyes', 'Romantic Birds', 'Penguins propose to each other')

db.session.add(donna)
db.session.commit()

donna.id
