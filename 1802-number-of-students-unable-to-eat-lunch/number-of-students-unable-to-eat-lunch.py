from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        length = len(sandwiches)
        i = 0
        while i < length:
            if students[0] == sandwiches[0]:
                sandwiches.popleft()
                students.popleft()
                i = 0
                length -= 1
            else:
                students.append(students.popleft())
                i += 1
        return len(students)
                


        