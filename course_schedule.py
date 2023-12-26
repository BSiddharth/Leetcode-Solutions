# https://leetcode.com/problems/course-schedule/description/
# git add . && git commit -m "completed course_schedule" && git push && exit


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ok_set = set()

        all_prerequisites = [[] for _ in range(numCourses)]

        for pair in prerequisites:
            all_prerequisites[pair[0]].append(pair[1])

        def helper(course):
            if course in ok_set:
                return True
            if course in current_set:
                return False
            current_set.add(course)
            for pre_req_courses in all_prerequisites[course]:
                if not helper(pre_req_courses):
                    return False
            ok_set.add(course)
            return True

        for i, course_pre_req in enumerate(all_prerequisites):
            for course in course_pre_req:
                current_set = set()
                if not helper(course):
                    return False
        return True
