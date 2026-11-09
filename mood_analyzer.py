# mood_analyzer.py
"""
Rule based mood analyzer for short text snippets.

This class starts with very simple logic:
  - Preprocess the text
  - Look for positive and negative words
  - Compute a numeric score
  - Convert that score into a mood label
"""

import re
import string
from typing import List, Tuple, Optional

from dataset import POSITIVE_WORDS, NEGATIVE_WORDS

PUNCTUATION = set(string.punctuation)
NEGATORS = {"not", "never", "no", "isn't", "wasn't", "don't", "didn't", "ain't", "can't", "won't"}
NEGATION_WINDOW = 3


class MoodAnalyzer:
    """
    A very simple, rule based mood classifier.
    """

    def __init__(
        self,
        positive_words: Optional[List[str]] = None,
        negative_words: Optional[List[str]] = None,
    ) -> None:
        # Use the default lists from dataset.py if none are provided.
        positive_words = positive_words if positive_words is not None else POSITIVE_WORDS
        negative_words = negative_words if negative_words is not None else NEGATIVE_WORDS

        # Store as sets for faster lookup.
        self.positive_words = set(w.lower() for w in positive_words)
        self.negative_words = set(w.lower() for w in negative_words)

    # ---------------------------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------------------------

    def preprocess(self, text: str) -> List[str]:
        """
        Convert raw text into a list of tokens the model can work with.

        TODO: Improve this method.

        Right now, it does the minimum:
          - Strips leading and trailing whitespace
          - Converts everything to lowercase
          - Splits on spaces

        Ideas to improve:
          - Remove punctuation
          - Handle simple emojis separately (":)", ":-(", "🥲", "😂")
          - Normalize repeated characters ("soooo" -> "soo")
        """
        cleaned = text.strip().lower()
        tokens = []
        for raw in cleaned.split():
            # Keep text emoticons whole so stripping punctuation can't erase them.
            if raw in self.positive_words or raw in self.negative_words:
                tokens.append(raw)
                continue
            # Pull emoji attached to a word ("sad😭") out as their own tokens.
            parts = re.findall(r"[^\W_]+(?:'[^\W_]+)?|[^\w\s]", raw)
            tokens.extend(p for p in parts if p not in PUNCTUATION)
        return tokens

    # ---------------------------------------------------------------------
    # Scoring logic
    # ---------------------------------------------------------------------

    def score_text(self, text: str) -> int:
        """
        Compute a numeric "mood score" for the given text.

        Positive words increase the score.
        Negative words decrease the score.

        TODO: You must choose AT LEAST ONE modeling improvement to implement.
        For example:
          - Handle simple negation such as "not happy" or "not bad"
          - Count how many times each word appears instead of just presence
          - Give some words higher weights than others (for example "hate" < "annoyed")
          - Treat emojis or slang (":)", "lol", "💀") as strong signals
        """
        # TODO: Implement this method.
        #   1. Call self.preprocess(text) to get tokens.
        #   2. Loop over the tokens.
        #   3. Increase the score for positive words, decrease for negative words.
        #   4. Return the total score.
        #
        # Hint: if you implement negation, you may want to look at pairs of tokens,
        # like ("not", "happy") or ("never", "fun").
        return self._analyze(text)[0]

    def _analyze(self, text: str) -> Tuple[int, List[str], List[str]]:
        """
        Score the text and record which tokens counted each way.

        Enhancement: negation. A negator flips the next sentiment word found
        within NEGATION_WINDOW tokens, so "not happy" counts as negative and
        "not bad" counts as positive.
        """
        score = 0
        positive_hits: List[str] = []
        negative_hits: List[str] = []
        negate_left = 0

        for token in self.preprocess(text):
            if token in NEGATORS:
                negate_left = NEGATION_WINDOW
                continue

            value = 0
            if token in self.positive_words:
                value = 1
            elif token in self.negative_words:
                value = -1

            if value == 0:
                negate_left = max(0, negate_left - 1)
                continue

            if negate_left > 0:
                value = -value
                token = f"not {token}"
                negate_left = 0

            score += value
            (positive_hits if value > 0 else negative_hits).append(token)

        return score, positive_hits, negative_hits

    # ---------------------------------------------------------------------
    # Label prediction
    # ---------------------------------------------------------------------

    def predict_label(self, text: str) -> str:
        """
        Turn the numeric score for a piece of text into a mood label.

        The default mapping is:
          - score > 0  -> "positive"
          - score < 0  -> "negative"
          - score == 0 -> "neutral"

        TODO: You can adjust this mapping if it makes sense for your model.
        For example:
          - Use different thresholds (for example score >= 2 to be "positive")
          - Add a "mixed" label for scores close to zero
        Just remember that whatever labels you return should match the labels
        you use in TRUE_LABELS in dataset.py if you care about accuracy.
        """
        # TODO: Implement this method.
        #   1. Call self.score_text(text) to get the numeric score.
        #   2. Return "positive" if the score is above 0.
        #   3. Return "negative" if the score is below 0.
        #   4. Return "neutral" otherwise.
        score, positive_hits, negative_hits = self._analyze(text)
        # Signals pointing both ways that nearly cancel out read as "mixed".
        if positive_hits and negative_hits and abs(score) <= 1:
            return "mixed"
        if score > 0:
            return "positive"
        if score < 0:
            return "negative"
        return "neutral"

    # ---------------------------------------------------------------------
    # Explanations (optional but recommended)
    # ---------------------------------------------------------------------

    def explain(self, text: str) -> str:
        """
        Return a short string explaining WHY the model chose its label.

        TODO:
          - Look at the tokens and identify which ones counted as positive
            and which ones counted as negative.
          - Show the final score.
          - Return a short human readable explanation.

        Example explanation (your exact wording can be different):
          'Score = 2 (positive words: ["love", "great"]; negative words: [])'

        The current implementation is a placeholder so the code runs even
        before you implement it.
        """
        score, positive_hits, negative_hits = self._analyze(text)

        return (
            f"Score = {score} "
            f"(positive: {positive_hits or '[]'}, "
            f"negative: {negative_hits or '[]'})"
        )
