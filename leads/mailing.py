from django.core.mail import send_mail
from django.conf import settings

def send_enquiry_confirmation(name, email, property_name):
    """Send confirmation email to customer who made an enquiry"""
    subject = 'Thank You for Your Enquiry - Shree Shyam City'
    message = f"""
Dear {name},

Thank you for your interest in {property_name}!

We have received your enquiry and our team will get back to you within 24 hours.

Our property consultant will contact you soon to discuss your requirements and schedule a site visit if needed.

For immediate assistance, please call us at +91 9876543210 or WhatsApp us.

Best Regards,
Shree Shyam City Team
Real Estate Excellence in Dhanbad

---
This is an automated message. Please do not reply to this email.
For queries, contact: hello@shreeshyamcity.com
    """
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def send_lead_notification(name, email, phone, message=''):
    """Send notification to admin about new lead"""
    subject = f'New Lead: {name}'
    email_message = f"""
New lead received!

Name: {name}
Email: {email}
Phone: {phone}
Message: {message}

Please follow up with this lead as soon as possible.
    """
    
    try:
        send_mail(
            subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Error sending notification: {e}")
        return False
