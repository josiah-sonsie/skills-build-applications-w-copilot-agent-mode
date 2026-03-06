from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass", team=team)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.team, team)

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username="activityuser", email="a@example.com", password="pass")
        activity = Activity.objects.create(user=user, type="run", duration=30, distance=5.0)
        self.assertEqual(activity.type, "run")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create_user(username="workoutuser", email="w@example.com", password="pass")
        workout = Workout.objects.create(user=user, name="Pushups", description="Do 20 pushups")
        self.assertEqual(workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create_user(username="leaderuser", email="l@example.com", password="pass")
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
