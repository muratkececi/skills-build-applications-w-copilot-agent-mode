from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access the database
db = client["octofit_db"]

# Create remaining collections
teams = db["teams"]
activity = db["activity"]
leaderboard = db["leaderboard"]
workouts = db["workouts"]

# Insert placeholder documents to ensure collection creation
teams.insert_one({"placeholder": True})
activity.insert_one({"placeholder": True})
leaderboard.insert_one({"placeholder": True})
workouts.insert_one({"placeholder": True})

print("Remaining collections initialized successfully.")
