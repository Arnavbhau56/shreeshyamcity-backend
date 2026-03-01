"""  
Seed script to populate database with dummy data from frontend constants
Run this script: python seed_data.py
"""
import os
import django
import sys
from datetime import date, datetime

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from properties.models import Property, PropertyImage, PropertyVideo, Landmark
from users.models import Customer, PropertyBought, InterestedProperty, PaymentHistory, User, TeamMember
from leads.models import Lead, Enquiry, Agent
from blogs.models import Blog

def create_admin_user():
    """Create admin user for login"""
    print("Creating admin user...")
    
    # Delete existing admin user if exists
    User.objects.filter(email='admin@shreeshyamcity.com').delete()
    
    # Create new admin user
    admin = User.objects.create_user(
        username='admin',
        email='admin@shreeshyamcity.com',
        password='Admin@123',
        is_staff=True,
        is_superuser=True
    )
    print(f"[OK] Created admin user: {admin.email}")
    print(f"     Username: admin")
    print(f"     Password: Admin@123")

def clear_existing_data():
    """Clear all existing data"""
    print("Clearing existing data...")
    Property.objects.all().delete()
    Customer.objects.all().delete()
    Lead.objects.all().delete()
    Enquiry.objects.all().delete()
    Agent.objects.all().delete()
    Blog.objects.all().delete()
    TeamMember.objects.all().delete()
    print("[OK] Data cleared")

def seed_properties():
    """Seed properties from MOCK_PROPERTIES"""
    print("\nSeeding properties...")
    
    properties_data = [
        {
            'title': 'Premium 3BHK Apartment in Hirapur',
            'description': 'Spacious 3BHK apartment with modern amenities in the heart of Hirapur. Close to ISM Dhanbad and top schools.',
            'price': 45.00,
            'location': 'Hirapur',
            'type': 'Apartment',
            'status': 'Ready to Move',
            'listing_type': 'Buy',
            'bedrooms': 3,
            'bathrooms': 2,
            'area': 1200,
            'dimensions': '40x30 ft',
            'facing': 'East',
            'amenities': ['Parking', 'Security', 'Power Backup', 'Lift'],
            'featured': True,
            'new_launch': False,
            'prime_commercial': False,
            'agent_contact': '+91 9876543210',
            'images': [
                'https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&q=80',
                'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80'
            ],
            'landmarks': [
                {'name': 'ISM Dhanbad', 'distance': '2 km', 'category': 'Education'},
                {'name': 'Railway Station', 'distance': '3 km', 'category': 'Transport'}
            ]
        },
        {
            'title': 'Commercial Shop in Bank More',
            'description': 'Prime commercial space in the busiest area of Dhanbad. Perfect for retail business.',
            'price': 75.00,
            'location': 'Bank More',
            'type': 'Commercial',
            'status': 'Ready to Move',
            'listing_type': 'Buy',
            'bedrooms': 0,
            'bathrooms': 1,
            'area': 800,
            'dimensions': '20x40 ft',
            'facing': 'North',
            'amenities': ['Parking', 'Security', 'Power Backup'],
            'featured': True,
            'new_launch': False,
            'prime_commercial': True,
            'agent_contact': '+91 9876543210',
            'images': [
                'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80'
            ],
            'landmarks': [
                {'name': 'Bank More Chowk', 'distance': '0.5 km', 'category': 'Business'},
                {'name': 'City Centre', 'distance': '0.2 km', 'category': 'Lifestyle'}
            ]
        },
        {
            'title': 'Residential Plot in Saraidhela',
            'description': 'Corner plot with excellent connectivity. Ideal for building your dream home.',
            'price': 35.00,
            'location': 'Saraidhela',
            'type': 'Plot',
            'status': 'Ready to Move',
            'listing_type': 'Buy',
            'bedrooms': 0,
            'bathrooms': 0,
            'area': 1500,
            'dimensions': '50x30 ft',
            'facing': 'Corner',
            'amenities': ['Water Supply', 'Electricity'],
            'featured': False,
            'new_launch': True,
            'prime_commercial': False,
            'agent_contact': '+91 9876543210',
            'images': [
                'https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=800&q=80'
            ],
            'landmarks': [
                {'name': 'Big Bazaar', 'distance': '1 km', 'category': 'Lifestyle'},
                {'name': 'PMCH Hospital', 'distance': '2 km', 'category': 'Healthcare'}
            ]
        },
        {
            'title': 'Luxury Villa in Kusum Vihar',
            'description': 'Independent villa with garden and parking. Premium locality with all modern amenities.',
            'price': 85.00,
            'location': 'Kusum Vihar',
            'type': 'Villa',
            'status': 'Ready to Move',
            'listing_type': 'Buy',
            'bedrooms': 4,
            'bathrooms': 3,
            'area': 2500,
            'dimensions': '60x50 ft',
            'facing': 'South',
            'amenities': ['Garden', 'Parking', 'Security', 'Power Backup', 'Modular Kitchen'],
            'featured': True,
            'new_launch': False,
            'prime_commercial': False,
            'agent_contact': '+91 9876543210',
            'images': [
                'https://images.unsplash.com/photo-1600596542815-22b8c153bd30?auto=format&fit=crop&w=800&q=80'
            ],
            'landmarks': [
                {'name': 'Koyla Nagar', 'distance': '1 km', 'category': 'Business'},
                {'name': 'Delhi Public School', 'distance': '1.5 km', 'category': 'Education'}
            ]
        },
        {
            'title': '2BHK Flat for Rent in Dhansar',
            'description': 'Affordable 2BHK flat available for rent. Centrally located with easy access to all amenities.',
            'price': 0.12,
            'location': 'Dhansar',
            'type': 'Apartment',
            'status': 'Ready to Move',
            'listing_type': 'Rent',
            'bedrooms': 2,
            'bathrooms': 1,
            'area': 900,
            'dimensions': '30x30 ft',
            'facing': 'West',
            'amenities': ['Parking', 'Water Supply'],
            'featured': False,
            'new_launch': False,
            'prime_commercial': False,
            'agent_contact': '+91 9876543210',
            'images': [
                'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=800&q=80'
            ],
            'landmarks': [
                {'name': 'Dhansar Thana', 'distance': '0.5 km', 'category': 'Business'},
                {'name': 'Local Market', 'distance': '0.3 km', 'category': 'Lifestyle'}
            ]
        }
    ]
    
    for prop_data in properties_data:
        images = prop_data.pop('images')
        landmarks = prop_data.pop('landmarks')
        
        property_obj = Property.objects.create(**prop_data)
        
        # Add images
        for idx, img_url in enumerate(images):
            PropertyImage.objects.create(property=property_obj, image_url=img_url, order=idx)
        
        # Add landmarks
        for landmark in landmarks:
            Landmark.objects.create(property=property_obj, **landmark)
        
        print(f"[OK] Created property: {property_obj.title}")
    
    print(f"[OK] Seeded {len(properties_data)} properties")

def seed_leads():
    """Seed leads"""
    print("\nSeeding leads...")
    
    leads_data = [
        {'name': 'Amit Kumar', 'email': 'amit@example.com', 'phone': '+91 9876543210', 'source': 'Website', 'status': 'New', 'message': 'Interested in 3BHK apartments'},
        {'name': 'Sneha Roy', 'email': 'sneha@example.com', 'phone': '+91 9876543211', 'source': 'Facebook', 'status': 'Contacted', 'message': 'Looking for commercial space'},
        {'name': 'Rajiv Singh', 'email': 'rajiv@example.com', 'phone': '+91 9876543212', 'source': 'Referral', 'status': 'Closed', 'message': 'Purchased villa in Kusum Vihar'},
        {'name': 'Pooja Verma', 'email': 'pooja@example.com', 'phone': '+91 9876543213', 'source': 'Website', 'status': 'New', 'message': 'Need plot in Saraidhela'},
        {'name': 'Vikram Malhotra', 'email': 'vikram@example.com', 'phone': '+91 9876543214', 'source': 'Instagram', 'status': 'New', 'message': 'Rental property inquiry'},
        {'name': 'Anjali Desai', 'email': 'anjali@example.com', 'phone': '+91 9876543215', 'source': 'Website', 'status': 'Contacted', 'message': 'Investment opportunity'},
    ]
    
    for lead_data in leads_data:
        Lead.objects.create(**lead_data)
        print(f"[OK] Created lead: {lead_data['name']}")
    
    print(f"[OK] Seeded {len(leads_data)} leads")

def seed_enquiries():
    """Seed enquiries"""
    print("\nSeeding enquiries...")
    
    enquiries_data = [
        {'name': 'John Doe', 'email': 'john@example.com', 'property': 'Luxury 3BHK Apartment', 'message': 'Is this available?', 'status': 'Unread', 'phone': '+91 9876543220'},
        {'name': 'Jane Smith', 'email': 'jane@example.com', 'property': 'Commercial Shop', 'message': 'What is the carpet area?', 'status': 'Read', 'phone': '+91 9876543221'},
        {'name': 'Rahul Verma', 'email': 'rahulv@example.com', 'property': 'Residential Plot', 'message': 'Can I visit the site?', 'status': 'Unread', 'phone': '+91 9876543222'},
    ]
    
    for enq_data in enquiries_data:
        Enquiry.objects.create(**enq_data)
        print(f"[OK] Created enquiry from: {enq_data['name']}")
    
    print(f"[OK] Seeded {len(enquiries_data)} enquiries")

def seed_agents():
    """Seed agents"""
    print("\nSeeding agents...")
    
    agents_data = [
        {
            'name': 'Rahul Sharma',
            'role': 'Senior Consultant',
            'phone': '+91 9876500001',
            'deals': 45,
            'photo': 'https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=100&q=80'
        },
        {
            'name': 'Priya Singh',
            'role': 'Sales Head',
            'phone': '+91 9876500002',
            'deals': 32,
            'photo': 'https://images.unsplash.com/photo-1573496359-936d9dd3a94b?auto=format&fit=crop&w=100&q=80'
        },
        {
            'name': 'Amit Verma',
            'role': 'Legal Advisor',
            'phone': '+91 9876500003',
            'deals': 28,
            'photo': 'https://images.unsplash.com/photo-1559192823-e1d8e87def54?auto=format&fit=crop&w=100&q=80'
        }
    ]
    
    for agent_data in agents_data:
        Agent.objects.create(**agent_data)
        print(f"[OK] Created agent: {agent_data['name']}")
    
    print(f"[OK] Seeded {len(agents_data)} agents")

def seed_blogs():
    """Seed blog posts"""
    print("\nSeeding blogs...")
    
    # Property Trends
    trends = [
        {
            'category': 'property_trends',
            'title': 'Gated Communities: The New Norm',
            'short_description': 'The shift towards gated communities is reshaping the skyline. Discover why families are moving away from standalone houses to integrated townships with 24/7 security and clubhouses.',
            'image': 'https://images.unsplash.com/photo-1460317442991-0ec209397118?auto=format&fit=crop&w=800&q=80',
            'description': 'The shift towards gated communities is reshaping the skyline. Discover why families are moving away from standalone houses to integrated townships with 24/7 security and clubhouses.',
            'date': date(2023, 10, 15),
            'time_to_read': '5 min read',
            'writer': 'Rahul Sharma'
        },
        {
            'category': 'property_trends',
            'title': 'Commercial Real Estate Boom',
            'short_description': 'Bank More and Steel Gate are witnessing unprecedented growth in commercial property values. Is it the right time to invest in retail spaces in Dhanbad?',
            'image': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80',
            'description': 'Bank More and Steel Gate are witnessing unprecedented growth in commercial property values. Is it the right time to invest in retail spaces in Dhanbad?',
            'date': date(2023, 8, 15),
            'time_to_read': '5 min read',
            'writer': 'Priya Singh'
        },
        {
            'category': 'property_trends',
            'title': 'Dhanbad Smart City Projects',
            'short_description': 'An overview of upcoming infrastructure projects including road widening, new flyovers, and drainage systems that will positively impact property appreciation.',
            'image': 'https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&w=800&q=80',
            'description': 'An overview of upcoming infrastructure projects including road widening, new flyovers, and drainage systems that will positively impact property appreciation.',
            'date': date(2023, 11, 20),
            'time_to_read': '4 min read',
            'writer': 'Amit Verma'
        },
        {
            'category': 'property_trends',
            'title': 'Rise of Eco-Friendly Homes',
            'short_description': 'Solar panels, rainwater harvesting, and green spaces are becoming standard requirements for modern homebuyers in Jharkhand.',
            'image': 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=800&q=80',
            'description': 'Solar panels, rainwater harvesting, and green spaces are becoming standard requirements for modern homebuyers in Jharkhand.',
            'date': date(2024, 1, 5),
            'time_to_read': '6 min read',
            'writer': 'Vikram Malhotra'
        }
    ]
    
    # Government Schemes
    schemes = [
        {
            'category': 'government_schemes',
            'title': 'Pradhan Mantri Awas Yojana (PMAY)',
            'short_description': 'A flagship mission by the Government of India to provide affordable housing for all. Benefits include interest subsidies up to ₹2.67 Lakh under CLSS.',
            'image': 'https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&q=80',
            'link': 'https://pmaymis.gov.in/'
        },
        {
            'category': 'government_schemes',
            'title': 'Jharkhand Housing Board Allotment',
            'short_description': 'The state government periodically releases residential plots and flats through a lottery system for different income groups (LIG, MIG, HIG).',
            'image': 'https://images.unsplash.com/photo-1516156008625-3a9d6067fab5?auto=format&fit=crop&w=800&q=80',
            'link': 'https://jharkhandhousing.gov.in/'
        },
        {
            'category': 'government_schemes',
            'title': 'Stamp Duty Concessions',
            'short_description': 'Special provision for women buyers in Jharkhand offering reduced stamp duty rates (₹1 token duty in some cases) on property registration.',
            'image': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=800&q=80',
            'link': 'https://jharkhand.gov.in/revenue'
        }
    ]
    
    # Area Guides
    areas = [
        {
            'category': 'area_guides',
            'title': 'Hirapur',
            'short_description': 'Peaceful residential area known for top schools like Carmel and De Nobili. High demand for 2/3 BHK flats.',
            'image': 'https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&w=800&q=80',
            'lifestyle': 'Quiet, Academic Atmosphere, Green Cover',
            'connectivity': '2.5 km from Railway Station',
            'key_landmarks': ['ISM Dhanbad', 'Carmel School', 'Park Market'],
            'avg_price': '₹3,500 - ₹4,500 / sqft',
            'rental_yield': '3.5%'
        },
        {
            'category': 'area_guides',
            'title': 'Saraidhela',
            'short_description': 'The lifestyle center of Dhanbad with shopping malls, Big Bazaar, and multi-specialty hospitals.',
            'image': 'https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?auto=format&fit=crop&w=800&q=80',
            'lifestyle': 'Urban, Busy, Premium Shopping',
            'connectivity': 'Direct access to GT Road (NH-2)',
            'key_landmarks': ['Big Bazaar', 'PMCH', 'Asian Jalan Hospital'],
            'avg_price': '₹4,000 - ₹5,500 / sqft',
            'rental_yield': '4%'
        },
        {
            'category': 'area_guides',
            'title': 'Bank More',
            'short_description': 'The commercial heart of the city. Ideal for office spaces, showrooms, and high-value investments.',
            'image': 'https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?auto=format&fit=crop&w=800&q=80',
            'lifestyle': 'Commercial, Hustle-Bustle, Central',
            'connectivity': '1.5 km from Railway Station',
            'key_landmarks': ['City Centre', 'Bank More Chowk', 'Railway Station'],
            'avg_price': '₹5,000 - ₹7,000 / sqft',
            'rental_yield': '5-6% (Commercial)'
        },
        {
            'category': 'area_guides',
            'title': 'Govindpur',
            'short_description': 'Rapidly developing due to the GT Road highway connectivity. Best for warehousing and affordable plots.',
            'image': 'https://images.unsplash.com/photo-1599809275372-b7f5d7ebac64?auto=format&fit=crop&w=800&q=80',
            'lifestyle': 'Developing, Semi-Urban, Industrial',
            'connectivity': 'On NH-2 Highway',
            'key_landmarks': ['GT Road', 'Industrial Area', 'Khalsa Hotel'],
            'avg_price': '₹2,000 - ₹3,000 / sqft',
            'rental_yield': '2.5%'
        },
        {
            'category': 'area_guides',
            'title': 'Kusum Vihar',
            'short_description': 'Wide roads, planned layout, and proximity to Koyla Nagar. A preferred choice for the elite.',
            'image': 'https://images.unsplash.com/photo-1600596542815-22b8c153bd30?auto=format&fit=crop&w=800&q=80',
            'lifestyle': 'Planned, Clean, Elite Community',
            'connectivity': 'Well connected to Saraidhela',
            'key_landmarks': ['Koyla Nagar', 'Delhi Public School', 'Koyla Bhawan'],
            'avg_price': '₹3,200 - ₹4,000 / sqft',
            'rental_yield': '3%'
        },
        {
            'category': 'area_guides',
            'title': 'Dhansar',
            'short_description': 'Centrally located with easy access to both the railway station and Bank More. Affordable housing options.',
            'image': 'https://images.unsplash.com/photo-1590059530492-d39f75e35384?auto=format&fit=crop&w=800&q=80',
            'lifestyle': 'Traditional, Community-centric, Accessible',
            'connectivity': 'Central Junction',
            'key_landmarks': ['Dhansar Thana', 'Mining Office', 'Temple'],
            'avg_price': '₹2,800 - ₹3,600 / sqft',
            'rental_yield': '3.5%'
        }
    ]
    
    for trend in trends:
        Blog.objects.create(**trend)
        print(f"[OK] Created blog: {trend['title']}")
    
    for scheme in schemes:
        Blog.objects.create(**scheme)
        print(f"[OK] Created blog: {scheme['title']}")
    
    for area in areas:
        Blog.objects.create(**area)
        print(f"[OK] Created blog: {area['title']}")
    
    print(f"[OK] Seeded {len(trends) + len(schemes) + len(areas)} blogs")

def seed_customers():
    """Seed customers"""
    print("\nSeeding customers...")
    
    customers_data = [
        {
            'name': 'Rajesh Kumar',
            'email': 'rajesh.kumar@example.com',
            'phone': '+91 9876501001',
            'address': 'Hirapur, Dhanbad',
            'status': 'VIP',
            'total_paid': 4500000.00,
            'pending_amount': 0.00,
            'notes': 'Purchased 3BHK apartment. Very satisfied customer.',
            'avatar_url': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=100&q=80'
        },
        {
            'name': 'Priya Sharma',
            'email': 'priya.sharma@example.com',
            'phone': '+91 9876501002',
            'address': 'Saraidhela, Dhanbad',
            'status': 'Active',
            'total_paid': 1500000.00,
            'pending_amount': 2000000.00,
            'notes': 'Purchased plot. Payment in installments.',
            'avatar_url': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=100&q=80'
        },
        {
            'name': 'Amit Patel',
            'email': 'amit.patel@example.com',
            'phone': '+91 9876501003',
            'address': 'Bank More, Dhanbad',
            'status': 'Active',
            'total_paid': 7500000.00,
            'pending_amount': 0.00,
            'notes': 'Purchased commercial shop. Interested in more properties.',
            'avatar_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=100&q=80'
        }
    ]
    
    for cust_data in customers_data:
        Customer.objects.create(**cust_data)
        print(f"[OK] Created customer: {cust_data['name']}")
    
    print(f"[OK] Seeded {len(customers_data)} customers")

def seed_team():
    """Seed team members"""
    print("\nSeeding team members...")
    
    team_data = [
        {
            'name': 'Rahul Sharma',
            'role': 'Founder & CEO',
            'image': 'https://images.unsplash.com/photo-1742981365880-698cfb84492d?auto=format&fit=crop&w=600&q=80',
            'bio': 'With over 15 years in the real estate sector, Rahul has been the driving force behind Shree Shyam City\'s rise as a trusted name in Dhanbad.',
            'specialization': ['Strategic Planning', 'Investment Analysis', 'Land Acquisition'],
            'experience': '15+ Years',
            'email': 'rahul@shreeshyamcity.com',
            'phone': '+91 98765 00001',
            'languages': ['English', 'Hindi', 'Bengali'],
            'order': 1
        },
        {
            'name': 'Priya Singh',
            'role': 'Head of Sales',
            'image': 'https://images.unsplash.com/photo-1681164315947-0f117a6dbbf7?auto=format&fit=crop&w=600&q=80',
            'bio': 'Priya ensures every client finds their perfect match with her expert market knowledge.',
            'specialization': ['Residential Sales', 'Client Negotiations', 'Market Research'],
            'experience': '8+ Years',
            'email': 'priya@shreeshyamcity.com',
            'phone': '+91 98765 00002',
            'languages': ['English', 'Hindi', 'Bhojpuri'],
            'order': 2
        },
        {
            'name': 'Amit Verma',
            'role': 'Legal Advisor',
            'image': 'https://images.unsplash.com/photo-1559192823-e1d8e87def54?auto=format&fit=crop&w=600&q=80',
            'bio': 'Ensuring 100% legally verified properties and hassle-free documentation.',
            'specialization': ['Property Law', 'Documentation', 'RERA Compliance'],
            'experience': '12+ Years',
            'email': 'legal@shreeshyamcity.com',
            'phone': '+91 98765 00003',
            'languages': ['English', 'Hindi'],
            'order': 3
        }
    ]
    
    for member_data in team_data:
        TeamMember.objects.create(**member_data)
        print(f"[OK] Created team member: {member_data['name']}")
    
    print(f"[OK] Seeded {len(team_data)} team members")

def main():
    print("=" * 60)
    print("SEEDING DATABASE WITH DUMMY DATA")
    print("=" * 60)
    
    create_admin_user()
    clear_existing_data()
    seed_properties()
    seed_leads()
    seed_enquiries()
    seed_agents()
    seed_blogs()
    seed_customers()
    seed_team()
    
    print("\n" + "=" * 60)
    print("[OK] DATABASE SEEDING COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nSummary:")
    print(f"  Admin User: 1")
    print(f"  Properties: {Property.objects.count()}")
    print(f"  Leads: {Lead.objects.count()}")
    print(f"  Enquiries: {Enquiry.objects.count()}")
    print(f"  Agents: {Agent.objects.count()}")
    print(f"  Blogs: {Blog.objects.count()}")
    print(f"  Customers: {Customer.objects.count()}")
    print(f"  Team Members: {TeamMember.objects.count()}")
    print("\n" + "=" * 60)
    print("ADMIN LOGIN CREDENTIALS")
    print("=" * 60)
    print("Email: admin@shreeshyamcity.com")
    print("Password: Admin@123")
    print("=" * 60)
    print("\nYou can now start the Django server and access the admin portal!")

if __name__ == '__main__':
    main()
