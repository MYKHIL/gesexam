#!/usr/bin/env python3
"""
Search Script for GES Promotion Quiz Application
Searches through all JSON files in default-questions folder and index.html
for a user-specified phrase and returns filenames and line numbers.
"""

import os
import json
from pathlib import Path


def search_phrase_in_file(filepath, phrase):
    """
    Search for a phrase in a file and return matching line numbers.
    
    Args:
        filepath: Path to the file to search
        phrase: The phrase to search for (case-insensitive)
    
    Returns:
        List of line numbers where phrase is found (1-indexed)
    """
    matching_lines = []
    phrase_lower = phrase.lower()
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                if phrase_lower in line.lower():
                    matching_lines.append(line_num)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []
    
    return matching_lines


def replace_in_file(filepath, phrase, replacement, line_numbers=None):
    """
    Replace phrase with replacement text in a file.
    
    Args:
        filepath: Path to the file
        phrase: The phrase to replace (case-insensitive search)
        replacement: The text to replace with
        line_numbers: List of specific line numbers to replace (None = all)
    
    Returns:
        Number of replacements made
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        replacements = 0
        phrase_lower = phrase.lower()
        
        for i, line in enumerate(lines, 1):
            # If line_numbers specified, only replace in those lines
            if line_numbers is None or i in line_numbers:
                # Case-insensitive replacement
                if phrase_lower in line.lower():
                    # Find all occurrences (case-insensitive)
                    new_line = line
                    start = 0
                    while True:
                        pos = new_line.lower().find(phrase_lower, start)
                        if pos == -1:
                            break
                        new_line = new_line[:pos] + replacement + new_line[pos + len(phrase):]
                        start = pos + len(replacement)
                        replacements += 1
                    lines[i - 1] = new_line
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return replacements
    except Exception as e:
        print(f"Error replacing in {filepath}: {e}")
        return 0


def show_context(filepath, line_number, phrase, context_lines=2):
    """
    Show context around a specific line for user review.
    
    Args:
        filepath: Path to the file
        line_number: Line number to show
        phrase: The phrase being searched (for highlighting)
        context_lines: Number of lines before/after to show
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        start = max(0, line_number - context_lines - 1)
        end = min(len(lines), line_number + context_lines)
        
        print(f"\n  Context (lines {start + 1}-{end}):")
        for i in range(start, end):
            marker = ">>>" if i == line_number - 1 else "   "
            print(f"  {marker} {i + 1:4d}: {lines[i].rstrip()}")
    except Exception as e:
        print(f"  Error showing context: {e}")


def replace_all_occurrences(all_results, phrase, replacement, script_dir):
    """
    Replace all occurrences of phrase with replacement.
    
    Args:
        all_results: Dictionary of search results
        phrase: The phrase to replace
        replacement: The text to replace with
        script_dir: Script directory path
    
    Returns:
        Total number of replacements made
    """
    total_replacements = 0
    
    # Replace in JSON files
    if "default-questions" in all_results:
        default_questions_dir = script_dir / "default-questions"
        for filename, line_numbers in all_results['default-questions'].items():
            filepath = default_questions_dir / filename
            count = replace_in_file(str(filepath), phrase, replacement)
            if count > 0:
                print(f"  [OK] {filename}: {count} replacement(s)")
                total_replacements += count
    
    # Replace in index.html
    if "index.html" in all_results:
        index_file = script_dir / "index.html"
        count = replace_in_file(str(index_file), phrase, replacement)
        if count > 0:
            print(f"  [OK] index.html: {count} replacement(s)")
            total_replacements += count
    
    return total_replacements


def replace_interactively(all_results, phrase, replacement, script_dir):
    """
    Replace occurrences one by one with user approval.
    
    Args:
        all_results: Dictionary of search results
        phrase: The phrase to replace
        replacement: The text to replace with
        script_dir: Script directory path
    
    Returns:
        Total number of replacements made
    """
    total_replacements = 0
    
    # Process JSON files
    if "default-questions" in all_results:
        default_questions_dir = script_dir / "default-questions"
        for filename, line_numbers in sorted(all_results['default-questions'].items()):
            filepath = default_questions_dir / filename
            print(f"\n[FILE] {filename}")
            
            for line_num in line_numbers:
                show_context(str(filepath), line_num, phrase)
                
                while True:
                    choice = input(f"\n  Replace on line {line_num}? (y/n/q to quit): ").strip().lower()
                    if choice in ['y', 'n', 'q']:
                        break
                    print("  Invalid choice. Please enter 'y', 'n', or 'q'.")
                
                if choice == 'q':
                    print("\n  Replacement cancelled by user.")
                    return total_replacements
                elif choice == 'y':
                    count = replace_in_file(str(filepath), phrase, replacement, [line_num])
                    total_replacements += count
                    print(f"  [OK] Replaced {count} occurrence(s) on line {line_num}")
    
    # Process index.html
    if "index.html" in all_results:
        index_file = script_dir / "index.html"
        line_numbers = all_results['index.html']
        print(f"\n📄 index.html")
        
        for line_num in line_numbers:
            show_context(str(index_file), line_num, phrase)
            
            while True:
                choice = input(f"\n  Replace on line {line_num}? (y/n/q to quit): ").strip().lower()
                if choice in ['y', 'n', 'q']:
                    break
                print("  Invalid choice. Please enter 'y', 'n', or 'q'.")
            
            if choice == 'q':
                print("\n  Replacement cancelled by user.")
                return total_replacements
            elif choice == 'y':
                count = replace_in_file(str(index_file), phrase, replacement, [line_num])
                total_replacements += count
                print(f"  ✓ Replaced {count} occurrence(s) on line {line_num}")
    
    return total_replacements


def search_in_json_files(directory, phrase):
    """
    Search for phrase in all JSON files in a directory.
    
    Args:
        directory: Path to directory containing JSON files
        phrase: The phrase to search for
    
    Returns:
        Dictionary with results
    """
    results = {}
    phrase_lower = phrase.lower()
    
    # Ensure directory exists
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        return results
    
    # Search all JSON files
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    file_content = f.read()
                    
                # Search line by line
                matching_lines = search_phrase_in_file(filepath, phrase)
                
                if matching_lines:
                    results[filename] = matching_lines
                    
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    return results


def main():
    """Main function to run the search."""
    # Get the script directory
    script_dir = Path(__file__).parent
    default_questions_dir = script_dir / "default-questions"
    index_file = script_dir / "index.html"
    
    print("\n" + "="*70)
    print("GES Promotion Quiz - Phrase Finder")
    print("="*70 + "\n")
    
    # Get phrase from user
    phrase = input("Enter the phrase to search for: ").strip()
    
    if not phrase:
        print("No phrase entered. Exiting.")
        return
    
    print(f"\nSearching for: '{phrase}'")
    print("-" * 70)
    
    all_results = {}
    
    # Search in default-questions folder
    if default_questions_dir.exists():
        print(f"\nSearching in: {default_questions_dir}")
        json_results = search_in_json_files(str(default_questions_dir), phrase)
        if json_results:
            all_results["default-questions"] = json_results
    else:
        print(f"Warning: default-questions folder not found at {default_questions_dir}")
    
    # Search in index.html
    if index_file.exists():
        print(f"Searching in: {index_file}")
        html_results = search_phrase_in_file(str(index_file), phrase)
        if html_results:
            all_results["index.html"] = html_results
    else:
        print(f"Warning: index.html not found at {index_file}")
    
    # Display results
    print("\n" + "="*70)
    print("RESULTS")
    print("="*70)
    
    if not all_results:
        print(f"\nNo matches found for '{phrase}'")
    else:
        total_matches = 0
        
        # Display JSON results
        if "default-questions" in all_results:
            print(f"\n[FOLDER] default-questions/ ({len(all_results['default-questions'])} files)")
            for filename, line_numbers in sorted(all_results['default-questions'].items()):
                print(f"   • {filename}: Lines {', '.join(map(str, line_numbers))}")
                total_matches += len(line_numbers)
        
        # Display HTML results
        if "index.html" in all_results:
            print(f"\n[FILE] index.html")
            line_numbers = all_results['index.html']
            print(f"   Lines: {', '.join(map(str, line_numbers))}")
            total_matches += len(line_numbers)
        
        print("\n" + "-"*70)
        print(f"Total matches found: {total_matches}")
        
        # Offer replace option
        print("\n" + "="*70)
        print("REPLACE OPTIONS")
        print("="*70)
        
        while True:
            replace_choice = input("\nDo you want to replace the found items? (y/n): ").strip().lower()
            if replace_choice in ['y', 'n']:
                break
            print("Invalid choice. Please enter 'y' or 'n'.")
        
        if replace_choice == 'y':
            replacement = input("Enter the replacement text: ").strip()
            
            print("\nReplace mode:")
            print("  1. Replace all occurrences")
            print("  2. Replace one by one (with approval)")
            
            while True:
                mode_choice = input("\nSelect mode (1/2): ").strip()
                if mode_choice in ['1', '2']:
                    break
                print("Invalid choice. Please enter '1' or '2'.")
            
            print("\n" + "="*70)
            print("REPLACING")
            print("="*70)
            
            if mode_choice == '1':
                # Replace all
                print(f"\nReplacing all occurrences of '{phrase}' with '{replacement}'...\n")
                total_replaced = replace_all_occurrences(all_results, phrase, replacement, script_dir)
                print(f"\n✓ Total replacements made: {total_replaced}")
            else:
                # Replace interactively
                print(f"\nReplacing '{phrase}' with '{replacement}' (interactive mode)...")
                total_replaced = replace_interactively(all_results, phrase, replacement, script_dir)
                print(f"\n✓ Total replacements made: {total_replaced}")
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()
