"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",
    "proud",
    "hopeful",
    "fire",
    "😂",
    "🎉",
    ":)",
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",
    "exhausted",
    "badly",
    "ugh",
    "died",
    "killing",
    "😭",
    "💀",
    ":(",
]

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",
    "Lowkey stressed but kind of proud of myself",
    "I absolutely love getting stuck in traffic",
    "this new song is fire no cap",
    "Exam went badly 😭",
    "Just got the internship!!! 🎉",
    "I'm fine 🙂",
    "Not bad for a Monday",
    "Meeting moved to 3pm",
    "ugh my wifi died again",
    "Exhausted but so proud of my team",
    "that movie was sick",
    "Had lunch, then went back to class",
    "I never feel good after these calls",
    "bruh this homework is killing me 💀",
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"
    "mixed",     # "Lowkey stressed but kind of proud of myself"
    "negative",  # "I absolutely love getting stuck in traffic" (sarcasm)
    "positive",  # "this new song is fire no cap"
    "negative",  # "Exam went badly 😭"
    "positive",  # "Just got the internship!!! 🎉"
    "neutral",   # "I'm fine 🙂" (hard: could be read as passive aggressive)
    "positive",  # "Not bad for a Monday"
    "neutral",   # "Meeting moved to 3pm"
    "negative",  # "ugh my wifi died again"
    "mixed",     # "Exhausted but so proud of my team"
    "positive",  # "that movie was sick" (slang)
    "neutral",   # "Had lunch, then went back to class"
    "negative",  # "I never feel good after these calls"
    "negative",  # "bruh this homework is killing me 💀"
]

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
