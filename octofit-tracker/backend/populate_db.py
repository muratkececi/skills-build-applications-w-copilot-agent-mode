# populate_db.py

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Kullanıcılar ekleniyor
user1 = User.objects.create(email='user1@example.com', name='User One', password='password1')
user2 = User.objects.create(email='user2@example.com', name='User Two', password='password2')

# Takımlar ekleniyor
team1 = Team.objects.create(name='Team Alpha', members=[user1, user2])

# Aktiviteler ekleniyor
activity1 = Activity.objects.create(user=user1, description='Running', date='2025-04-20T10:00:00Z')
activity2 = Activity.objects.create(user=user2, description='Cycling', date='2025-04-20T11:00:00Z')

# Liderlik tablosu ekleniyor
leaderboard1 = Leaderboard.objects.create(team=team1, score=100)

# Egzersizler ekleniyor
workout1 = Workout.objects.create(name='Morning Yoga', duration=30)
workout2 = Workout.objects.create(name='Evening Cardio', duration=45)

print("Test verileri başarıyla eklendi.")
