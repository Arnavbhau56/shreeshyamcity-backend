import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from blogs.models import Blog
from datetime import date

def seed_blogs():
    print("Seeding blog data...")
    
    # Clear existing blogs
    Blog.objects.all().delete()
    
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
    
    # Create blogs
    created_count = 0
    
    for trend in trends:
        Blog.objects.create(**trend)
        created_count += 1
        print(f"Created: {trend['title']}")
    
    for scheme in schemes:
        Blog.objects.create(**scheme)
        created_count += 1
        print(f"Created: {scheme['title']}")
    
    for area in areas:
        Blog.objects.create(**area)
        created_count += 1
        print(f"Created: {area['title']}")
    
    print(f"\n[SUCCESS] Successfully created {created_count} blog posts!")
    print(f"   - {len(trends)} Property Trends")
    print(f"   - {len(schemes)} Government Schemes")
    print(f"   - {len(areas)} Area Guides")

if __name__ == '__main__':
    seed_blogs()
