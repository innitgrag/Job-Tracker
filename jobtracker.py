#!/usr/bin/env python3
"""
Cold Email Generator for Akshiti Garg
A Python script to generate customized cold emails for software engineering job applications.

Usage:
    python cold_email_generator.py
    
Features:
- Multiple catchy subject line variations
- Customizable email body templates
- Company and hiring manager name customization
- Multiple email versions generation
- File export functionality
"""

import random
import argparse
import sys
from datetime import datetime

class ColdEmailGenerator:
    def __init__(self):
        # Catchy subject line templates
        self.subject_templates = [
            "Passionate BITS Pilani Grad Seeking Software Engineering Opportunities at {company}",
            "Full-Stack Developer from BITS Pilani - Ready to Contribute to {company}",
            "Software Engineer with Production Experience - Interested in {company} Opportunities", 
            "BITS Pilani EEE Grad with Strong Tech Stack - Exploring Roles at {company}",
            "Experienced Developer Seeking Software Engineering Role at {company}",
            "Full-Stack Engineer from BITS Pilani - Excited About {company} Opportunities",
            "Software Developer with 400+ LeetCode Solutions - Interested in {company}",
            "Production-Ready Developer from BITS Pilani Seeking Opportunities at {company}",
            "Recent BITS Pilani Graduate - Software Engineering Enthusiast at {company}",
            "Full-Stack Developer | BITS Pilani | Ready to Join {company} Team"
        ]
        
        # Alternative intro variations
        self.intro_variations = [
            "I hope this email finds you well. My name is Akshiti Garg, and I am a recent B.E. (Hons.) graduate in Electrical and Electronics Engineering from BITS Pilani, Hyderabad Campus (CGPA: 7.92).",
            "I hope you're doing well. I'm Akshiti Garg, a recent graduate from BITS Pilani, Hyderabad Campus with a B.E. (Hons.) in Electrical and Electronics Engineering (CGPA: 7.92).",
            "I trust this message finds you well. My name is Akshiti Garg, and I recently completed my B.E. (Hons.) in Electrical and Electronics Engineering from BITS Pilani, Hyderabad Campus with a CGPA of 7.92."
        ]
        
        # Experience section variations
        self.experience_variations = [
            """**Experience & Skills:**
I bring hands-on experience as a Software Developer Intern at Piramal Finance Limited, where I:
• Implemented 6+ frontend and backend modules using React.js, TypeScript, and Spring Boot
• Integrated 10+ REST APIs and collaborated with cross-functional teams for 3+ production releases
• Built custom monitoring solutions that reduced issue resolution time

Previously, at Cognix Technologies, I developed a Flutter-based food tracking app that reduced manual logging effort by 30% and accelerated feature delivery by 25%.""",

            """**Professional Experience:**
During my internship at Piramal Finance Limited, I gained valuable production experience by:
• Developing 6+ comprehensive frontend and backend modules with React.js, TypeScript, and Spring Boot
• Successfully integrating 10+ REST APIs while working closely with QA, PM, and UX teams
• Creating custom HTTP Metrics Publisher for monitoring, which significantly improved issue resolution times

At Cognix Technologies, I built an innovative Flutter-based food tracking application that enhanced user efficiency by 30% and streamlined development processes.""",

            """**Technical Experience:**
My software development journey includes impactful work at Piramal Finance Limited, where I:
• Delivered 6+ robust frontend and backend solutions using modern tech stack (React.js, TypeScript, Spring Boot)
• Orchestrated integration of 10+ REST APIs, ensuring seamless workflow improvements
• Developed monitoring tools that enhanced system observability and reduced debugging time

Earlier at Cognix Technologies, I architected a Flutter application for athletic nutrition tracking, achieving 30% efficiency gains in manual processes."""
        ]
        
        # Closing variations
        self.closing_variations = [
            "I would welcome the opportunity to discuss how my technical skills and passion for software development can contribute to {company}'s mission. Thank you for considering my application and for your time.",
            "I am excited about the possibility of contributing to {company}'s innovative projects and would love to discuss how my skills align with your team's needs. Thank you for your time and consideration.",
            "I would be thrilled to bring my technical expertise and problem-solving mindset to {company}. I look forward to the opportunity to discuss my qualifications further. Thank you for your consideration."
        ]
        
        # Base email structure
        self.email_structure = """Dear {hiring_manager},

{intro}

I am writing to express my interest in software engineering opportunities at {company}.

{experience}

**Technical Expertise:**
My technical stack includes C++, Java, SQL, Node.js, React.js, Spring Boot, and experience with scalable full-stack applications. I have strong foundations in DSA, OOP, OS, DBMS, and System Design.

**Notable Projects:**
• **PG Pal**: Full-stack platform with secure authentication and advanced filtering (pg-pal.vercel.app)
• **Jobify**: Job matching platform connecting recruiters and candidates

**Problem-Solving Foundation:**
I have solved 400+ problems on LeetCode, demonstrating my commitment to continuous learning and strong algorithmic thinking.

{closing}

Best regards,
Akshiti Garg
📧 akshitigarg1224@gmail.com
📱 +91-8949031109
💼 LinkedIn: [Your LinkedIn Profile]
🔗 GitHub: [Your GitHub Profile]"""

    def generate_email(self, company_name="[Company Name]", hiring_manager="Hiring Manager", variation_index=None):
        """Generate a customized cold email with optional variation control"""
        
        # Select variations (random if not specified)
        if variation_index is None:
            subject = random.choice(self.subject_templates)
            intro = random.choice(self.intro_variations) 
            experience = random.choice(self.experience_variations)
            closing = random.choice(self.closing_variations)
        else:
            # Use modulo to cycle through variations
            subject = self.subject_templates[variation_index % len(self.subject_templates)]
            intro = self.intro_variations[variation_index % len(self.intro_variations)]
            experience = self.experience_variations[variation_index % len(self.experience_variations)]
            closing = self.closing_variations[variation_index % len(self.closing_variations)]
        
        # Format the email
        subject_line = subject.format(company=company_name)
        email_body = self.email_structure.format(
            company=company_name,
            hiring_manager=hiring_manager,
            intro=intro,
            experience=experience,
            closing=closing.format(company=company_name)
        )
        
        return {
            "subject": subject_line,
            "body": email_body
        }
    
    def generate_multiple_versions(self, company_name="[Company Name]", hiring_manager="Hiring Manager", count=3):
        """Generate multiple different versions of the email"""
        versions = []
        for i in range(count):
            email = self.generate_email(company_name, hiring_manager, variation_index=i)
            versions.append({
                "version": i + 1,
                "subject": email["subject"],
                "body": email["body"]
            })
        return versions
    
    def save_email_to_file(self, email_content, filename=None):
        """Save generated email to a text file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"cold_email_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"SUBJECT: {email_content['subject']}\n\n")
            f.write("EMAIL BODY:\n")
            f.write("-" * 50 + "\n")
            f.write(email_content['body'])
        return f"Email saved to {filename}"
    
    def interactive_mode(self):
        """Interactive mode for generating emails"""
        print("=" * 60)
        print("COLD EMAIL GENERATOR - INTERACTIVE MODE")
        print("=" * 60)
        
        while True:
            print("\nOptions:")
            print("1. Generate single email")
            print("2. Generate multiple versions") 
            print("3. Quick generate (random)")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                company = input("Enter company name: ").strip()
                manager = input("Enter hiring manager name (or press Enter for 'Hiring Manager'): ").strip()
                if not manager:
                    manager = "Hiring Manager"
                
                email = self.generate_email(company, manager)
                print(f"\nSUBJECT: {email['subject']}")
                print("\nEMAIL BODY:")
                print("-" * 40)
                print(email['body'])
                
                save = input("\nSave to file? (y/n): ").strip().lower()
                if save == 'y':
                    filename = self.save_email_to_file(email)
                    print(f"✓ {filename}")
            
            elif choice == "2":
                company = input("Enter company name: ").strip()
                manager = input("Enter hiring manager name (or press Enter for 'Hiring Manager'): ").strip()
                if not manager:
                    manager = "Hiring Manager"
                
                try:
                    count = int(input("How many versions? (default: 3): ") or "3")
                except ValueError:
                    count = 3
                
                versions = self.generate_multiple_versions(company, manager, count)
                
                for version in versions:
                    print(f"\n--- VERSION {version['version']} ---")
                    print(f"SUBJECT: {version['subject']}")
                    print("\nEMAIL PREVIEW (first 5 lines):")
                    lines = version['body'].split('\n')[:5]
                    for line in lines:
                        print(line)
                    print("...[content continues]...")
                
                save_version = input(f"\nSave which version? (1-{count} or 'all' or 'none'): ").strip().lower()
                
                if save_version == 'all':
                    for i, version in enumerate(versions):
                        filename = self.save_email_to_file(version, f"email_v{version['version']}.txt")
                        print(f"✓ {filename}")
                elif save_version.isdigit() and 1 <= int(save_version) <= count:
                    selected = versions[int(save_version) - 1]
                    filename = self.save_email_to_file(selected)
                    print(f"✓ {filename}")
            
            elif choice == "3":
                company = input("Enter company name: ").strip()
                email = self.generate_email(company)
                print(f"\nQuick generated email for {company}:")
                print(f"SUBJECT: {email['subject']}")
                print(f"\nPreview: {email['body'][:200]}...")
                
                save = input("\nSave to file? (y/n): ").strip().lower()
                if save == 'y':
                    filename = self.save_email_to_file(email)
                    print(f"✓ {filename}")
            
            elif choice == "4":
                print("Goodbye! Good luck with your job applications! 🚀")
                break
            
            else:
                print("Invalid choice. Please try again.")

def main():
    parser = argparse.ArgumentParser(description='Generate customized cold emails for job applications')
    parser.add_argument('--company', '-c', help='Company name')
    parser.add_argument('--manager', '-m', default='Hiring Manager', help='Hiring manager name')
    parser.add_argument('--versions', '-v', type=int, default=1, help='Number of versions to generate')
    parser.add_argument('--save', '-s', action='store_true', help='Save to file automatically')
    parser.add_argument('--interactive', '-i', action='store_true', help='Run in interactive mode')
    
    args = parser.parse_args()
    
    generator = ColdEmailGenerator()
    
    if args.interactive or len(sys.argv) == 1:
        generator.interactive_mode()
    else:
        if not args.company:
            print("Error: Company name is required. Use --company or -c flag.")
            return
        
        if args.versions > 1:
            versions = generator.generate_multiple_versions(args.company, args.manager, args.versions)
            for version in versions:
                print(f"\n--- VERSION {version['version']} ---")
                print(f"SUBJECT: {version['subject']}")
                print("\nBODY:")
                print(version['body'])
                
                if args.save:
                    filename = generator.save_email_to_file(version, f"email_v{version['version']}.txt")
                    print(f"\n✓ {filename}")
        else:
            email = generator.generate_email(args.company, args.manager)
            print(f"SUBJECT: {email['subject']}")
            print("\nBODY:")
            print(email['body'])
            
            if args.save:
                filename = generator.save_email_to_file(email)
                print(f"\n✓ {filename}")

if __name__ == "__main__":
    main()
