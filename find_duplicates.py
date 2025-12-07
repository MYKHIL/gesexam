import json
import os
from pathlib import Path

# Dynamically discover all JSON files in the Default questions directory
questions_dir = Path('default-questions')
json_files = sorted(questions_dir.glob('*.json'))

if not json_files:
    print("No JSON files found in 'Default questions' directory.")
    exit(1)

file_map = {}
all_questions = {}

print(f"Discovered {len(json_files)} JSON file(s) in 'Default questions' directory:\n")

for file_path in json_files:
    print(f"  - {file_path.name}")

print(f"\nLoading files...\n")

for file_path in json_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            questions = json.load(f)
            print(f"Loaded {len(questions)} questions from {file_path.name}")
            for q in questions:
                q_hash = json.dumps(q, sort_keys=True)
                if q_hash not in file_map:
                    file_map[q_hash] = []
                file_map[q_hash].append(file_path.name)
                all_questions[q_hash] = q
    except Exception as e:
        print(f"Error loading {file_path.name}: {e}")

duplicates = {q_hash: files for q_hash, files in file_map.items() if len(files) > 1}

total_files = len(json_files)
total_questions = sum(len(questions) for questions in [json.load(open(f)) for f in json_files])
unique_questions = len(all_questions)
duplicate_occurrences = sum(len(files) - 1 for files in file_map.values())

print(f"\n{'='*80}")
print(f"Total JSON files found: {total_files}")
print(f"Total questions across all files: {total_questions}")
print(f"Total unique questions: {unique_questions}")
print(f"Total duplicate occurrences: {duplicate_occurrences}")
print(f"DUPLICATE QUESTIONS FOUND: {len(duplicates)}")
print(f"{'='*80}\n")

if duplicates:
    print("DUPLICATES:\n")
    for i, (q_hash, files_with_dup) in enumerate(duplicates.items(), 1):
        q = all_questions[q_hash]
        print(f"{i}. Question ID {q['id']}: {q['question'][:75]}...")
        print(f"   Found in: {', '.join(sorted(files_with_dup))}")
        print()
else:
    print("✓ No duplicates found!")

