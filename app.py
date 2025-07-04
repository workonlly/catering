from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Email configuration
EMAIL_ADDRESS = "your-gmail@gmail.com"  # Replace with your Gmail
EMAIL_PASSWORD = "your-app-password"    # Replace with your Gmail App Password
RECIPIENT_EMAIL = "lacleocorporateservices@gmail.com"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/services-extend/corporate-meals")
def corporate_meals():
    return render_template("services-extend/corporate-meals.html")

@app.route("/services-extend/snacks")
def snacks():
    return render_template("services-extend/snacks.html")

@app.route("/services-extend/birthday-party")
def birthdayparty():
    return render_template("services-extend/birthday-party.html")

@app.route("/services-extend/event-catering")
def event_catering():
    return render_template("services-extend/event-catering.html")

@app.route("/services-extend/bhandara")
def bhandara():
    return render_template("services-extend/bhandara.html")

@app.route("/services-extend/stationary")
def stationary():
    return render_template("services-extend/stationary.html")

@app.route("/services-extend/toiletries")
def toiletries():
    return render_template("services-extend/toiletries.html")

@app.route("/vendorzone")
def vendorzone():
    return render_template("vendorzone.html")

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/services-extend/cabservices")
def cabservices():
    return render_template("services-extend/cabservices.html")

@app.route("/services-extend/securityguard")
def securityguard():
    return render_template("services-extend/securityguard.html")

@app.route("/services-extend/corporategifting")
def corporategifting():
    return render_template("services-extend/corporategifting.html")

@app.route("/services-extend/corporatedesktops")
def corporatedesktops():
    return render_template("services-extend/corporatedesktops.html")

@app.route("/services-extend/trophiescertificates")
def trophiescertificates():
    return render_template("services-extend/trophiescertificates.html")

@app.route("/services-extend/payrollservices")
def payrollservices():
    return render_template("services-extend/payrollservices.html")

@app.route("/services-extend/corporatepayslipsolution")
def corporatepayslipsolution():
    return render_template("services-extend/corporatepayslipsolution.html")

    try:
        # Get form data
        company = request.form.get('company', '').strip()
        contact = request.form.get('contact', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        products = request.form.get('products', '').strip()
        certifications = request.form.get('certifications', '').strip()
        
        # Validate required fields
        if not all([company, contact, email, phone, products]):
            return jsonify({
                'success': False, 
                'message': 'Please fill in all required fields.'
            }), 400
        
        # Send email
        success = send_vendor_email(company, contact, email, phone, products, certifications)
        
        if success:
            return jsonify({
                'success': True, 
                'message': 'Thank you! Your vendor application has been submitted successfully. We will contact you soon.'
            })
        else:
            return jsonify({
                'success': False, 
                'message': 'There was an error submitting your application. Please try again or contact us directly.'
            }), 500
            
    except Exception as e:
        print(f"Error in submit_vendor: {str(e)}")
        return jsonify({
            'success': False, 
            'message': 'An unexpected error occurred. Please try again.'
        }), 500

def send_vendor_email(company, contact, email, phone, products, certifications):
    try:
        # Create message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = f'New Vendor Application - {company}'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        
        # Create HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .header {{ background-color: #e67e22; color: white; padding: 20px; text-align: center; border-radius: 8px 8px 0 0; }}
                .content {{ background-color: #f9f9f9; padding: 20px; }}
                .section {{ background-color: white; padding: 15px; border-radius: 5px; margin-bottom: 15px; border-left: 4px solid #e67e22; }}
                .section h3 {{ color: #e67e22; margin: 0 0 10px 0; }}
                .products-box {{ background-color: #f5f5f5; padding: 10px; border-radius: 3px; margin-top: 5px; }}
                .footer {{ background-color: #333; color: white; padding: 15px; text-align: center; border-radius: 0 0 8px 8px; }}
                .highlight {{ background-color: #e8f5e8; padding: 15px; border-radius: 5px; border-left: 4px solid #4CAF50; }}
                a {{ color: #e67e22; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 style="margin: 0;">🏢 New Vendor Application</h1>
                    <p style="margin: 5px 0 0 0;">LaCleo Foods Vendor Registration</p>
                </div>
                
                <div class="content">
                    <div class="section">
                        <h3>🏢 Company Information</h3>
                        <p><strong>Company Name:</strong> {company}</p>
                        <p><strong>Contact Person:</strong> {contact}</p>
                    </div>
                    
                    <div class="section">
                        <h3>📞 Contact Information</h3>
                        <p><strong>Email:</strong> <a href="mailto:{email}">{email}</a></p>
                        <p><strong>Phone:</strong> <a href="tel:{phone}">{phone}</a></p>
                    </div>
                    
                    <div class="section">
                        <h3>📦 Products & Services</h3>
                        <p><strong>Products Supplied:</strong></p>
                        <div class="products-box">{products.replace(chr(10), '<br>')}</div>
                    </div>
                    
                    {f'''
                    <div class="section">
                        <h3>🏆 Certifications</h3>
                        <p>{certifications}</p>
                    </div>
                    ''' if certifications else ''}
                    
                    <div class="highlight">
                        <p style="margin: 0;"><strong>📅 Application Date:</strong> {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}</p>
                    </div>
                </div>
                
                <div class="footer">
                    <p style="margin: 0; font-size: 14px;">
                        This application was submitted through the LaCleo Foods vendor registration form.
                    </p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Create plain text content
        text_content = f"""
New Vendor Application - {company}

Company Information:
- Company Name: {company}
- Contact Person: {contact}

Contact Information:
- Email: {email}
- Phone: {phone}

Products Supplied:
{products}

{f'Certifications: {certifications}' if certifications else ''}

Application Date: {datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}

This application was submitted through the LaCleo Foods vendor registration form.
        """
        
        # Attach parts
        part1 = MIMEText(text_content, 'plain')
        part2 = MIMEText(html_content, 'html')
        
        msg.attach(part1)
        msg.attach(part2)
        
        # Send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        print(f"Vendor email sent successfully for {company}")
        return True
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False


    

if __name__ == "__main__":
    app.run(debug=True)
