import random
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch, helpers

# Connect to Elasticsearch 6.8
es = Elasticsearch("http://localhost:9200")

# Index name
INDEX_NAME = "product-events"

# Sample values
product_sources = ["Online", "Retail", "Wholesale"]
product_types = ["Electronics", "Clothing", "Books", "Toys", "Furniture", "Groceries", "Sports", "Beauty"]

# Generate documents
def generate_documents(start_date, days=60, docs_per_day=500):
    for day in range(days):
        current_date = start_date + timedelta(days=day)
        for _ in range(docs_per_day):
            timestamp = current_date + timedelta(seconds=random.randint(0, 86400))
            yield {
                "_index": INDEX_NAME,
                "_type": "_doc",  # ✅ Required in ES 6.x
                "_source": {
                    "timestamp": timestamp.isoformat(),
                    "ProductSource": random.choice(product_sources),
                    "ProductType": random.choice(product_types),
                    "Amount": round(random.uniform(10.0, 500.0), 2),
                    "UnitsSold": random.randint(1, 100)
                }
            }


# Optional: Delete index if exists
if es.indices.exists(INDEX_NAME):
    es.indices.delete(index=INDEX_NAME)

# Create index with mapping (for better Kibana UX)
# Create index with correct mapping for ES 6.8
es.indices.create(
    index=INDEX_NAME,
    body={
        "mappings": {
            "_doc": {  # ✅ Required in ES 6.x
                "properties": {
                    "timestamp": {"type": "date"},
                    "ProductSource": {"type": "keyword"},
                    "ProductType": {"type": "keyword"},
                    "Amount": {"type": "float"},
                    "UnitsSold": {"type": "integer"}
                }
            }
        }
    }
)


# Generate and index data
print("Indexing documents...")
start_date = datetime.utcnow() - timedelta(days=60)
docs = generate_documents(start_date)
helpers.bulk(es, docs)
print("Done.")
