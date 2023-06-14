def get_collection(client,db_name,collection_name):
    if db_name in client.list_database_names():
        db=client[db_name]
        if collection_name in db.list_collection_names():
            collection = db[collection_name]
            print(f'get {collection_name} collection in {db_name} database')
    else:
        raise ValueError("Can't find this collection")
    return collection