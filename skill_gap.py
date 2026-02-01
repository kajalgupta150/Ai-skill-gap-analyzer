import pandas as pd

# Step 1: Take user input
target_role = input("Enter your target role: ")

user_skills = input("Enter your skills (comma separated): ")
user_skills = user_skills.split(",")

# Step 2: Read CSV file
data = pd.read_csv("skills_data.csv")

# Step 3: Find role data
role_data = data[data["role"] == target_role]

if role_data.empty:
    print("❌ Role not found. Please check spelling.")
    exit()

# Step 4: Get required skills
required_skills = role_data["required_skills"].values[0]
required_skills = required_skills.split(",")

# Step 5: Clean data
user_skills = [skill.strip() for skill in user_skills]
required_skills = [skill.strip() for skill in required_skills]

# Step 6: Find missing skills
missing_skills = []

for skill in required_skills:
    if skill not in user_skills:
        missing_skills.append(skill)

# Step 7: Show result
print("\n===== AI SKILL GAP REPORT =====")

if missing_skills:
    print("You need to learn:")
    for skill in missing_skills:
        print("-", skill)
else:
    print("🎉 You already have all required skills!")

# Step 8: Learning roadmap
print("\nLearning Roadmap:")

for i, skill in enumerate(missing_skills, start=1):
    print(f"Week {i}: Learn {skill}")
