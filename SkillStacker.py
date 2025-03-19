


import os
import re
import PyPDF2

def extract_skills_from_pdf(pdf_path, skills_list):
    technical_skills = set()
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text
        
        # Normalize text to lowercase
        text = text.lower()
        
        # Match predefined technical skills
        for skill in skills_list:
            if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text, re.IGNORECASE):
                technical_skills.add(skill)

    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    
    return technical_skills

def process_resumes(folder_path, skills_list):
    resume_scores = {}

    # Read all PDFs from the folder
    for file in os.listdir(folder_path):
        if file.endswith('.pdf'):
            file_path = os.path.join(folder_path, file)
            matched_skills = extract_skills_from_pdf(file_path, skills_list)
            score = len(matched_skills)
            resume_scores[file] = (score, matched_skills)

    # Sort resumes based on the number of matched skills (descending order)
    sorted_resumes = sorted(resume_scores.items(), key=lambda x: x[1][0], reverse=True)

    # Get top 50 resumes
    top_50 = sorted_resumes[:50]

    return top_50

# List of technical skills to search for
skills = [
    "Python", "Java", "SQL", "Machine Learning", "Data Analysis", "C++", 
    "TensorFlow", "Pandas", "NumPy", "Cloud Computing", "Docker", "Kubernetes"
]

# Folder containing resumes
folder_path = r"C:\Users\sival\Desktop\resumes" 

top_resumes = process_resumes(folder_path, skills)

# Display results
print("\nTop 50 Resumes with Highest Skill Matches:\n")
for rank, (file, (score, matched_skills)) in enumerate(top_resumes, 1):
    print(f"{rank}. {file} – {score} skills matched")
    print(f"   Skills: {', '.join(matched_skills)}\n")


# In[ ]:




