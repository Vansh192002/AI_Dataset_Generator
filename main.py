import csv
import os
import google.generativeai as genai
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your_credentials_json_file" #Give path to your credentials file, you can get it from google Ai and ML section


criteria = "criteria_file"#path to your criteria file
input_file = "input_file" #path to your input file which contains questions for training dataset (.csv) format
output_file = "output_file" # path to the file you want to store the answers of the questions (.csv) format
model = genai.GenerativeModel('gemini-pro')
with open(criteria, "r", encoding="utf-8") as f:
    criteria = f.read()
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    count = 0
    error_count = 0
    for question in reader:
        question_text = question[0]
        prompt = f"{criteria}\nAnswer the following question:\n{question_text}"
        count += 1
        try:
            response = model.generate_content(contents=prompt)
            writer.writerow([question_text, response.text])
            print(count)
        except Exception as e:
            error_count += 1
            print(f"Error processing question: {question_text}{error_count}")
            
