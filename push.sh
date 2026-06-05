#!/bin/bash

# Auto-push script
echo "=== Committing changes ==="
git add .

# Check if there are changes to commit
if git diff-index --quiet HEAD --; then
    echo "No changes to commit."
else
    git commit -m "update: auto-commit from validation"
fi

echo "=== Pushing to GitHub ==="
git push origin main
echo "=== Push complete ==="
