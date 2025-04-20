from pymongo import MongoClient
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Test data for users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe", "password": "password123"},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "password": "password456"}
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]}
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user": "john.doe@example.com", "description": "Ran 5km", "date": "2025-04-20T10:00:00Z"},
            {"user": "jane.smith@example.com", "description": "Cycled 10km", "date": "2025-04-20T11:00:00Z"}
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"team": "Team Alpha", "score": 100}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Morning Yoga", "duration": 30},
            {"name": "Evening Run", "duration": 45}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
