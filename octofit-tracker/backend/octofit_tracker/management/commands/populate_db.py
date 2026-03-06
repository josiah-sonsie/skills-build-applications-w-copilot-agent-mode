from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.db import connection
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='password', team=marvel)
        steve = User.objects.create_user(username='captainamerica', email='steve@marvel.com', password='password', team=marvel)
        bruce = User.objects.create_user(username='batman', email='bruce@dc.com', password='password', team=dc)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='password', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        Activity.objects.create(user=clark, type='run', duration=50, distance=10)

        # Create Workouts
        Workout.objects.create(user=tony, name='Chest Day', description='Bench press and pushups')
        Workout.objects.create(user=steve, name='Leg Day', description='Squats and lunges')
        Workout.objects.create(user=bruce, name='Cardio', description='Treadmill and cycling')
        Workout.objects.create(user=clark, name='Strength', description='Deadlifts and pullups')

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=90)
        Leaderboard.objects.create(user=bruce, points=95)
        Leaderboard.objects.create(user=clark, points=110)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
