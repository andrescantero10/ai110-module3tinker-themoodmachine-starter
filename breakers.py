"""Breaker sentences for Part 3. Run: python breakers.py"""
from mood_analyzer import MoodAnalyzer

BREAKERS = [
    "I love getting stuck in traffic",
    "this is wicked good",
    "that party was sick",
    "I'm fine 🙂",
    "I'm exhausted but proud of myself",
    "I am not happy about this",
    "not bad at all",
    "ain't nobody happy bout this",
    "dis food slaps fr",
    "This food is very good.",
    "im finna cry this test was trash",
    "This test was terrible and I am upset.",
]

analyzer = MoodAnalyzer()
for text in BREAKERS:
    print(f'"{text}" -> {analyzer.predict_label(text)} | {analyzer.explain(text)}')
