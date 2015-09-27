import os

from pymongo import MongoClient
import redis

__all__ = [
    'MONGO',
    'REDIS',
]

# setup MONGO
mongo_url = os.getenv('NYL_MONGO_URL')
mongo_db_name = mongo_url.rpartition('/')[-1]
MONGO = MongoClient(mongo_url)['mongo_db_name']

# setup REDIS
redis_url = os.getenv('NYL_REDIS_URL')
redis_db = redis_url.rpartition('/')[-1]
REDIS = redis.StrictRedis.from_url(redis_url, db=redis_db)
