from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Initialize the database
db = client["octofit_db"]

# Create collections
users = db["users"]
teams = db["teams"]
activity = db["activity"]
leaderboard = db["leaderboard"]
workouts = db["workouts"]

# Ensure unique index for users collection
users.create_index("email", unique=True)

print("Database and collections initialized successfully.")
