
"""
Create or update the default admin user.
"""
from app.database import SessionLocal, Base, engine
from app.models.user import User
from app.auth.hashing import hash_password

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    admin = db.query(User).filter(
        User.email.in_(["admin@amazon.local", "admin@example.com"])
    ).first()

    if admin:
        admin.email = "admin@example.com"
        admin.name = "Admin"
        admin.is_admin = True
        admin.hashed_password = hash_password("Admin@123")
        print("Admin account updated: admin@example.com")
    else:
        admin = User(
            name="Admin",
            email="admin@example.com",
            hashed_password=hash_password("Admin@123"),
            is_admin=True,
        )
        db.add(admin)
        print("Admin account created: admin@example.com")

    db.commit()
    print("Password: Admin@123")
finally:
    db.close()
