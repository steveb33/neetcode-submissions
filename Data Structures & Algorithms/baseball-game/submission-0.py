class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tracker = []
        score = 0

        for i in range(len(operations)):
            if operations[i] == '+':
                tracker.append(tracker[-1] + tracker[-2])
            elif operations[i] == 'D':
                tracker.append(tracker[-1]*2)
            elif operations[i] == 'C':
                tracker.pop()
            else:
                tracker.append(int(operations[i]))
        for i in range(len(tracker)):
            score += tracker[i]

        return score