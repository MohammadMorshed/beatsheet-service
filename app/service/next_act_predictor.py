import random
from collections import defaultdict
from config import NEXT_ACT_TRAINING_DATA

class NextActPredictor:
    def __init__(self):
        # Transition matrix: maps a current act to possible next acts with their frequencies
        self.transitions = defaultdict(lambda: defaultdict(int))

    def train(self, sequences):
        """
        Train the model using a list of sequences.
        Each sequence is a list of acts or beats.
        """
        for sequence in sequences:
            for i in range(len(sequence) - 1):
                current_act = sequence[i]
                next_act = sequence[i + 1]
                self.transitions[current_act][next_act] += 1

    def predict(self, current_act):
        """
        Predict the next act based on the current one.
        Returns None if no prediction can be made.
        """
        if current_act not in self.transitions:
            return None

        next_acts = self.transitions[current_act]
        total = sum(next_acts.values())

        # Generate a weighted random choice
        rand = random.uniform(0, total)
        cumulative = 0
        for act, count in next_acts.items():
            cumulative += count
            if rand <= cumulative:
                return act

        return None  # Fallback

    def predict_sequence(self, current_act, num_suggestions=5):
        """
        Suggest a sequence of acts starting from the current act.
        """
        suggestions = []
        for _ in range(num_suggestions):
            next_act = self.predict(current_act)
            if not next_act:
                break
            suggestions.append(next_act)
            current_act = next_act
        return suggestions


# Example Usage
if __name__ == "__main__":
    # Example training data (sequences of acts or beats)
    training_data = [
        ["Intro", "Conflict", "Climax", "Resolution"],
        ["Intro", "Setup", "Conflict", "Resolution"],
        ["Setup", "Conflict", "Climax", "Resolution"],
    ]

    predictor = NextActPredictor()
    predictor.train(training_data)

    current_act = "Conflict"
    next_act = predictor.predict(current_act)
    print(f"Based on '{current_act}', the next suggested act is: '{next_act}'")

    sequence = predictor.predict_sequence(current_act, num_suggestions=3)
    print(f"Suggested sequence starting from '{current_act}': {sequence}")


next_act_predictor = NextActPredictor()
next_act_predictor.train(NEXT_ACT_TRAINING_DATA)
