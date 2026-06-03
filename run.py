from app import create_app, db
from app.models import User, Saree, Worker
from datetime import datetime

app = create_app()

def seed_database():
    """Seeds default admin and sample data if database is empty."""
    with app.app_context():
        # Create all tables if they don't exist
        db.create_all()
        
        # Check if we already have an admin
        admin_user = User.query.filter_by(role='admin').first()
        if not admin_user:
            print("Seeding database with default accounts and sample data...")
            
            # 1. Create Default Admin
            admin = User(username='hipparagishankar940@gmail.com', role='admin')
            admin.set_password('Shankar@2000')
            db.session.add(admin)
            
            # 2. Create Sample Workers & their User Accounts
            worker_data = [
                {"username": "rajesh", "name": "Rajesh Kumar", "phone": "9876543210", "address": "12, Weaver Street, Surat", "joining_date": datetime(2025, 1, 15)},
                {"username": "amit", "name": "Amit Sharma", "phone": "8765432109", "address": "45, Silk Mills Colony, Surat", "joining_date": datetime(2025, 2, 10)},
                {"username": "priya", "name": "Priya Patel", "phone": "7654321098", "address": "78, Handloom Row, Surat", "joining_date": datetime(2025, 3, 5)}
            ]
            
            for w in worker_data:
                # User account
                u = User(username=w["username"], role='worker')
                u.set_password('worker123')
                db.session.add(u)
                db.session.flush() # Populate u.id
                
                # Worker profile
                worker = Worker(
                    user_id=u.id,
                    name=w["name"],
                    phone=w["phone"],
                    address=w["address"],
                    joining_date=w["joining_date"],
                    status='active'
                )
                db.session.add(worker)
            
            # 3. Create Sample Sarees
            saree_data = [
                {"name": "Banarasi Katan Silk", "category": "Silk", "cost_price": 4500.0, "selling_price": 7500.0, "worker_payment": 800.0},
                {"name": "Surat Jacquard Georgette", "category": "Georgette", "cost_price": 1800.0, "selling_price": 3200.0, "worker_payment": 450.0},
                {"name": "Kanchi Pattu Splendid", "category": "Silk", "cost_price": 6000.0, "selling_price": 9800.0, "worker_payment": 1200.0},
                {"name": "Chanderi Cotton Classic", "category": "Cotton", "cost_price": 1200.0, "selling_price": 2200.0, "worker_payment": 300.0},
                {"name": "Bandhani Premium Crepe", "category": "Crepe", "cost_price": 2500.0, "selling_price": 4500.0, "worker_payment": 600.0}
            ]
            
            for s in saree_data:
                saree = Saree(
                    name=s["name"],
                    category=s["category"],
                    cost_price=s["cost_price"],
                    selling_price=s["selling_price"],
                    worker_payment=s["worker_payment"]
                )
                db.session.add(saree)
                
            db.session.commit()
            print("Database seeding completed successfully!")
        else:
            print("Database already seeded.")

if __name__ == '__main__':
    seed_database()
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
