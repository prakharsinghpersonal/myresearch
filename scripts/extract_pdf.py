#!/usr/bin/env python3
"""
PDF Text Extraction Script for Research Analysis
Extracts text from PDF files to help analyze research content
"""

import sys
import os
import PyPDF2
import re

def extract_pdf_text(pdf_path):
    """Extract text from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            print(f"📄 PDF has {len(pdf_reader.pages)} pages")
            
            for page_num, page in enumerate(pdf_reader.pages, 1):
                page_text = page.extract_text()
                text += f"\n--- PAGE {page_num} ---\n"
                text += page_text
                text += "\n"
                
            return text
            
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return None

def analyze_research_content(text):
    """Analyze research content and extract key information"""
    if not text:
        return {}
    
    analysis = {
        'title': '',
        'authors': '',
        'abstract': '',
        'keywords': '',
        'methodology': '',
        'findings': '',
        'conclusions': ''
    }
    
    # Try to extract title (usually in first few lines)
    lines = text.split('\n')
    if lines:
        # Look for title-like patterns
        for line in lines[:10]:
            line = line.strip()
            if line and len(line) > 10 and len(line) < 200:
                if not analysis['title'] and not any(word in line.lower() for word in ['abstract', 'introduction', 'page']):
                    analysis['title'] = line
                    break
    
    # Try to find abstract
    abstract_pattern = r'abstract[:\s]*([^]*?)(?=\n\n|\n[A-Z]|introduction|$)' 
    abstract_match = re.search(abstract_pattern, text, re.IGNORECASE | re.DOTALL)
    if abstract_match:
        analysis['abstract'] = abstract_match.group(1).strip()
    
    # Try to find keywords
    keywords_pattern = r'keywords?[:\s]*([^]*?)(?=\n\n|\n[A-Z]|$)' 
    keywords_match = re.search(keywords_pattern, text, re.IGNORECASE | re.DOTALL)
    if keywords_match:
        analysis['keywords'] = keywords_match.group(1).strip()
    
    return analysis

def main():
    pdf_path = "research/Research.pdf"
    
    if not os.path.exists(pdf_path):
        print(f"❌ PDF file not found: {pdf_path}")
        sys.exit(1)
    
    print("🔬 Research PDF Analysis Tool")
    print("=" * 40)
    
    # Extract text
    text = extract_pdf_text(pdf_path)
    if not text:
        print("❌ Failed to extract text from PDF")
        sys.exit(1)
    
    # Save extracted text for manual review
    output_file = "research/extracted_text.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"✅ Extracted text saved to: {output_file}")
    
    # Analyze content
    analysis = analyze_research_content(text)
    
    print("\n📊 Content Analysis Results:")
    print("=" * 40)
    
    for key, value in analysis.items():
        if value:
            print(f"\n🔍 {key.upper()}:")
            print(f"   {value[:200]}{'...' if len(value) > 200 else ''}")
    
    print(f"\n📝 Full extracted text available in: {output_file}")
    print("💡 Review the extracted text to manually populate the summary")

if __name__ == "__main__":
    main()
