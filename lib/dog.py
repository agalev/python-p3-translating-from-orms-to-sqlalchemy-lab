from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def new_from_db(session):
    pass

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    found = session.query(Dog).filter(Dog.name == name).first()
    return found

def find_by_id(session, id):
    found = session.query(Dog).filter(Dog.id == id).first()
    return found

def find_by_name_and_breed(session, name, breed):
    found = session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    return found

def update_breed(session, dog, breed):
    # dog.breed = breed
    updated_dog = session.query(Dog).filter(Dog.id == dog.id).update({Dog.breed: breed})
    session.commit()
    return updated_dog