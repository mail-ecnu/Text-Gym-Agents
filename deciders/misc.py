def history_to_str(history):
    history_str = ""
    for d in history:
        history_str += f"state: {d['state']}, action: {d['action']}, reward: {d['reward']}\n"
    return history_str

def get_majority_vote(actions):
    return max(set(actions), key=actions.count)

def test_get_majority_vote():
    assert get_majority_vote([1, 1, 1, 2, 2]) == 1
    assert get_majority_vote([1, 1, 2, 2, 2]) == 2
    assert get_majority_vote([1, 1, 2, 2, 3]) == 1
    assert get_majority_vote([1, 2, 3, 4, 5]) == 1
    assert get_majority_vote([1, 2, 3, 4, 5, 1, 1, 1, 1, 1]) == 1
    assert get_majority_vote([1, 2, 3, 4, 5, 1, 1, 1, 1, 2]) == 1
    assert get_majority_vote([1, 2, 3, 4, 5, 1, 1, 1, 2, 2]) == 1
    assert get_majority_vote([1, 2, 3, 4, 5, 1, 1, 2, 2, 2]) == 2

if __name__ == "__main__":
    test_get_majority_vote()