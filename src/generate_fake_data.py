from faker import Faker
import random
from app import db  
from user.models import User, UserRole  
from task.models import Task  


fake = Faker()

def create_fake_users(count=10):
    for _ in range(count):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
            role=random.choice([UserRole.ADMIN, UserRole.USER]),
            verified=True,
        )
        db.session.add(user)
    db.session.commit()

def create_fake_tasks(count=100):
    user_ids = [user.id for user in User.query.all()]
    for _ in range(count):
        task = Task(
            title=fake.sentence(),
            description=fake.text(),
            priority=random.choice(["high", "medium", "low"]),
            status=random.choice(["pending", "completed"]),
            dueDate=fake.future_date(end_date="+30d"),  
            createdAt=fake.past_date(start_date="-30d"),  
            updatedAt=fake.past_date(start_date="-30d"),  
            userId=random.choice(user_ids)
        )
        db.session.add(task)
    db.session.commit()


def generate_fake_data():
    print("Generating fake users...")
    create_fake_users(50)  
    print("Generating fake tasks...")
    create_fake_tasks(200)  
    print("Fake data generation completed.")
