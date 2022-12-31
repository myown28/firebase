#~~~ FIREBASE ~~~
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

ob1 = {
    'id': '1',
    'name': 'pratham',
    'age': '17'
}

data = [ob1]


for record in data:
    doc_ref = db.collection(u'User').document(record['id'])
    doc_ref.set(record)
