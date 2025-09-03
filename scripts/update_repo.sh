#!/bin/bash

# Research Repository Update Script
# This script helps manage updates to the research repository

echo "🔬 Research Repository Update Script"
echo "====================================="

# Check git status
echo "📊 Checking git status..."
git status

# Add all changes
echo "📝 Adding all changes..."
git add .

# Get commit message from user
echo "💬 Enter commit message (or press Enter for default):"
read commit_message

# Use default message if none provided
if [ -z "$commit_message" ]; then
    commit_message="Update research repository"
fi

# Commit changes
echo "💾 Committing changes with message: '$commit_message'"
git commit -m "$commit_message"

# Check if remote exists
if git remote get-url origin >/dev/null 2>&1; then
    echo "🚀 Pushing to GitHub..."
    git push origin main
    echo "✅ Successfully pushed to GitHub!"
else
    echo "⚠️  No remote origin found. Please set up GitHub repository first."
    echo "📖 See GITHUB_SETUP.md for instructions."
fi

echo "�� Update complete!"
