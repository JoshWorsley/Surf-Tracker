#!/bin/bash

# Replace with your information
ACCESS_TOKEN="your_access_token"
REPO_OWNER="your_repo_owner"
REPO_NAME="your_repo_name"

# Store the last known commit SHA (initialize if not present)
LAST_COMMIT_SHA=$(cat last_commit.txt 2>/dev/null || echo "")

# Get the latest commit SHA
API_URL="https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/commits"
CURL_OPTIONS="-s -H \"Authorization: token $ACCESS_TOKEN\""
LATEST_COMMIT_SHA=$(curl $CURL_OPTIONS $API_URL | jq -r '.[0].sha')

# Check for errors
if [[ $? -ne 0 ]]; then
  echo "Error fetching data from GitHub API"
  exit 1
fi

# Check if there are new pushes
if [[ "$LATEST_COMMIT_SHA" != "$LAST_COMMIT_SHA" ]]; then
  echo "New push detected: $LATEST_COMMIT_SHA"
  # Add your desired actions here (e.g., send notification, run tests)
  # ...
else
  echo "No new pushes found."
fi

# Update the stored commit SHA
echo "$LATEST_COMMIT_SHA" > last_commit.txt