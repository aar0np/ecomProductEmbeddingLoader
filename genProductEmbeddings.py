from dbConnection          import get_session
from cassandra.query       import SimpleStatement
from langchain.embeddings  import HuggingFaceEmbeddings, SentenceTransformerEmbeddings
import csv
import sys

# build CQL statements
selectProductCQL = "SELECT product_id, name, product_group, images FROM product WHERE product_id = ?"
insertVectorCQL = "INSERT INTO product_vectors (product_id, name, product_group, images, product_vector) VALUES (?,?,?,?,?)"

session = get_session()

# prepare CQL statements
selectProduct = session.prepare(selectProductCQL)
insertVector = session.prepare(insertVectorCQL)

def getProduct(id):
	row = session.execute(selectProduct,[id]).one()
	product = dict()
	product["id"] = id
	product["name"] = row[1]
	product["product_group"] = row[2]
	product["images"] = row[3]

	return product

# initialize the all-MiniLM-L6-v2 model locally
model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

#read file
filename = "data/product_ids.csv"

with open(filename, encoding = 'utf8') as file:
	reader = csv.reader(file)
	next(reader) # skip header line

	for dataline in reader:

		productId = dataline[0]
		product = getProduct(productId)

		vectorEmb = model.embed_query(product["name"])
		#print("id = " + productId)
		#print("name = " + product["name"])
		#print(*vectorEmb)

		session.execute(insertVector,[productId,product["name"],product["product_group"],product["images"],vectorEmb])
