from elasticsearch import Elasticsearch

# Connect to your Elasticsearch cluster
es = Elasticsearch("http://localhost:9200")

# Create an index with a custom analyzer using the standard tokenizer
index_name = "my_index"
es.indices.create(index=index_name, body={
    "settings": {
        "analysis": {
            "analyzer": {
                "my_analyzer": {
                    "tokenizer": "standard"
                }
            }
        }
    }
})

# Index some sample data
sample_text = "Quick brown fox!"
es.index(index=index_name, body={"text": sample_text})

# Now you can search using your custom analyzer
search_query = "fox"
results = es.search(index=index_name, body={"query": {"match": {"text": search_query}}})
print(results)
es.close()
