# Model Card: Mood Machine

> Built with Claude Code as the AI assistant, which wrote the code, ran the tests, and drafted this card.

## 1. Model Overview

**Model type:** I compared both the rule based model and the ML model.

**Intended purpose:** Classify short social media style posts as positive, negative, neutral, or mixed. It's a learning prototype, not something to use on real people.

**How it works (brief):** The rule based model adds a point for positive words, subtracts a point for negative words, flips a word's sign after a negator, and returns "mixed" when signals point both ways and nearly cancel. The ML model learns word patterns from the labeled posts using bag of words and logistic regression.

## 2. Data

**Dataset description:** `SAMPLE_POSTS` has 20 posts: the 6 starter posts plus 14 new ones with slang, emojis, sarcasm, and mixed feelings. Labels: 7 negative, 6 positive, 4 neutral, 3 mixed.

**Labeling process:** Each post got the label a reader would most likely give it. Some were hard:
- "I'm fine 🙂" is labeled neutral, but it could be passive aggressive.
- "that movie was sick" is labeled positive, which depends on knowing the slang.
- "I absolutely love getting stuck in traffic" is labeled negative because it's sarcasm.

**Important characteristics:** Very short posts, casual English, emojis, slang, one sarcastic post, and several mixed posts.

**Possible issues:** 20 posts is tiny. One person's labels decide what's "correct". It's nearly all casual US English, so other dialects and languages are barely covered.

## 3. How the Rule Based Model Works

**Scoring rules:**
- `preprocess` lowercases, strips punctuation, and keeps emoji and emoticons as their own tokens.
- Each positive word is +1 and each negative word is -1, with no weighting.
- Enhancement, negation: "not", "never", "ain't" and similar flip the next sentiment word within 3 tokens.
- Vocabulary added from observed failures: proud, hopeful, fire, 😂, 🎉, :) and exhausted, badly, ugh, died, killing, 😭, 💀, :(
- Labels: both kinds of signal with |score| <= 1 is mixed. Otherwise the sign of the score decides, and 0 is neutral.

**Strengths:** Predictable and easy to explain. `explain()` shows exactly which words counted.

**Weaknesses:** It only knows its word list. It misses sarcasm, unknown slang, and any meaning that depends on context.

## 4. How the ML Model Works

**Features used:** Bag of words using `CountVectorizer`.

**Training data:** `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:** Trained on only the 6 starter posts, it scored 0.60 on the full 20. Trained on all 20, it scored 1.00 on those same 20. Flipping one label, the sarcastic traffic post, changed its answer for "I love getting stuck in traffic" from negative to positive. It's very sensitive to labels.

**Strengths and weaknesses:** It picks up patterns without hand-written rules, but with this little data it mostly memorizes. It also ignores emoji, because the default tokenizer drops them.

## 5. Evaluation

| Model | Evaluated on | Accuracy |
|---|---|---|
| Rule based, baseline (no negation, emoji, or mixed) | same 20 posts | 0.35 |
| Rule based, final | same 20 posts | 0.90 |
| ML | same 20 posts it trained on | 1.00 |
| ML | leave-one-out on the 20 posts | 0.20 (4 of 20) |

The 0.90 and the 1.00 are both too optimistic. The rules were tuned on these posts, and the ML model was scored on its own training data. There's no real test set.

**Correct predictions:**
- "I am not happy about this" is negative, because negation flips "happy". The baseline called it positive.
- "Not bad for a Monday" is positive, because negation flips "bad". The baseline called it negative.
- "Exhausted but so proud of my team" is mixed, because one word counts each way and the score is 0.

**Incorrect predictions:**
- "I absolutely love getting stuck in traffic": rule based says positive because "love" is the only signal it sees. Left unfixed on purpose, since a keyword rule can't detect sarcasm.
- "that movie was sick": rule based says neutral because "sick" isn't in the list. Adding it would break "I feel sick".
- "This food is very good.": the ML model says negative even though it's plain and obvious. The rule based model gets it right.

**Fix I tested (Part 3):** "I am not happy about this" failed because negation was ignored. Adding negation fixed it and "Not bad for a Monday". The limitation is that it only looks 3 tokens ahead and always flips.

## 6. Limitations

- The dataset is tiny and there's no held-out test set.
- Sarcasm: "I love getting stuck in traffic" is still positive in the rule based model.
- Unknown slang is ignored: "dis food slaps fr" is neutral.
- "I'm fine 🙂" is neutral only because 🙂 isn't in the list, not because the model understood the tone.

## 7. Ethical Considerations

**Overt bias:** Errors clustered around informal and dialect-style writing. "This food is very good." and "This test was terrible and I am upset." were right in the rule based model, while "dis food slaps fr" and "im finna cry this test was trash" both came back neutral, with the same kind of meaning. This model underserves people who write in AAVE or heavy slang, because its word list is standard English plus a few hand-picked terms. Not fixed, only documented.

**Covert compliance:** The AI assistant wrote the word list and scoring logic itself, and no separate AI review of them was run. Nothing pushed back on those choices. It should have been flagged earlier that picking words from the failing posts raises the accuracy score without showing the model generalizes. The leave-one-out test and this note are what surfaced that, not the first accuracy number.

**Misuse risk:** A message showing real distress, like "bruh this homework is killing me 💀" versus a serious version of the same words, can't be told apart by this model. It shouldn't be used to judge anyone's mental state, and analyzing personal messages raises privacy concerns.

## 8. Ideas for Improvement

- Add many more labeled posts and hold out a real test set.
- Tune the ML tokenizer so it keeps emoji, and try TF-IDF.
- Use a small transformer model for context.
- Add dialect and slang coverage, reviewed by people who actually write that way.
- Weight stronger words like "hate" more than milder ones.
