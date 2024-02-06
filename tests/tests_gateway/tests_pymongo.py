import pymongo


def main():
    try:
        # Connect to a MongoDB instance
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["mydatabase"]
        collection = db["collection"]

        # Insert a sample document
        sample_doc = {
            "name": "John Doe",
            "age": 30
        }
        collection.insert_one(sample_doc)

        print("PyMongo installation test successful")
    except Exception as err:
        print(f"Error: \n {err}")
    

if __name__ == "__main__":
    main()