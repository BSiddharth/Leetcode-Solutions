# https://leetcode.com/problems/course-schedule-ii/description/
# git add . && git commit -m "completed course_schedule_ii" && git push && exit

class Node:
    def __init__(self,val) -> None:
        self.val = val 
        self.then = []

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_list = [Node(x) for x in range(numCourses)]

        for prerequisite in prerequisites:
            course_list[prerequisite[1]].then.append(course_list[prerequisite[0]])

        result = [-1 for _ in range(numCourses)]
        current_result_index = numCourses - 1

        checked_list = [False for _ in range(numCourses)]
        
        current_node_set  = set()

        def add_in_result(course_node):
            nonlocal current_result_index

            if checked_list[course_node.val]:
                return True
            checked_list[course_node.val] = True

            if len(course_node.then) == 0:
                checked_list[course_node.val] = True
                result[current_result_index] = course_node.val
                current_result_index -= 1
                return True

            current_node_set.add(course_node.val)

            for next_course in course_node.then:
                if next_course.val in current_node_set:
                    return False
                if not add_in_result(next_course):
                    return False
            
            current_node_set.remove(course_node.val)
            result[current_result_index] = course_node.val
            current_result_index -= 1
            return True
            

        for course in course_list:
            if checked_list[course.val]:
                continue
            if not add_in_result(course):
                return []

        return result
