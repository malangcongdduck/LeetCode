class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while True:
            print(sandwiches)
            print(students)
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                students.append(students.pop(0))
                
            #검사
            count = 0
            for i in students:
                if i != sandwiches[0]:
                    count+=1
                    
            if count == len(students):
                return len(students)
            if len(students) == 0 and len(sandwiches) == 0:
                return 0
                    
        