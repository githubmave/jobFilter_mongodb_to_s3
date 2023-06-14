import pymongo
import json
from bson.json_util import dumps, loads

# filter job categories collect
def jobcategories_filter(collection):
    jobcategories_data = collection.find(
        {},
        {'_id':1,'key':1,'name':1,'_v':1}
    )
    jobcategories_json = json.loads(dumps(jobcategories_data))
    print('jobcategories json file created')
    return jobcategories_json

# filter cities collection
def cities_filter(collection):
    cities_data = collection.find(
        {},
        {'_id':1, 'country':1,'name':1,'chName':1}
    )
    cities_json = json.loads(dumps(cities_data))
    print('cities json file created')
    return cities_json

# filter job collection
def jobs_filter(collection):
    job_data = collection.aggregate([
        {
            '$lookup':{
                'from':'jobcategories',
                'localField': 'categories',
                'foreignField':'_id',
                'as': 'categories_list'
            }
        },
        {
            '$lookup':{
                'from':'cities',
                'localField':'city',
                'foreignField':'_id',
                'as':'cities'

            }
        },
        {
            '$project':{
                '_id':1,
                'title':1,
                'publishedDate':1,
                'deadline':1,
                'effictivePeriod':1,
                'jobRequired Degree':1,
                'level':1,
                'jobType':1,
                'city':'$cities.name',
                'country':1,
                'categories_list':'$categories_list.key'
            }

        }
    ])
    jobs_json=json.loads(dumps(job_data))
    print('jobs json file created')
    return jobs_json

# filter user collection
def users_filter(collection):
    user_data = collection.aggregate([
        {
          '$lookup':{
                'from':'cities',
                'localField':'city',
                'foreignField':'_id',
                'as': 'cities'
           }
        },
        {
            '$project':{
                '_id':1,
                'interestedFields':1,
                'jobStatus':1,
                'degree':1,
                'currentStatus':1,
                'gender':1,
                'city':'$cities.name',
            }
        }
    ])
    users_json=json.loads(dumps(user_data))
    print('users json file created')
    return users_json