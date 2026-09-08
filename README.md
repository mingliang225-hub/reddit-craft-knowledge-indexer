# Reddit Craft Community Knowledge Indexer

An open-source, non-commercial research utility designed to help hobbyist and craft communities (e.g., r/Leathercraft, r/handbags) identify recurring troubleshooting questions and synthesize community FAQ documentation.

## Project Purpose
Many niche craft communities receive repetitive questions regarding material durability, common defects, and maintenance. This tool performs local keyword clustering on publicly available posts to generate structured Markdown digests. Community moderators and contributors can use these summaries to update subreddit wikis and troubleshooting guides.

## Compliance with Reddit Responsible Builder Policy
- **Strictly Read-Only**: The script only queries public submissions and comments via standard GET endpoints. It never posts, votes, comments, or sends messages.
- **Privacy & Anonymity**: Author usernames and user IDs are stripped immediately upon ingest. No user profiling is performed.
- **No AI/LLM Training**: Reddit content is never used to train, fine-tune, or evaluate generative AI models.
- **Rate Limiting**: Built-in request pacing strictly adheres to Reddit's API limits (<= 30 req/min) with exponential backoff handling.
- **Content Deletion**: Caches are ephemeral and respect deletion checks.
