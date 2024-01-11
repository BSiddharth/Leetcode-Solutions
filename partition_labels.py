# https://leetcode.com/problems/partition-labels/description/
# git add . && git commit -m "completed partition_labels" && git push && exit

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start_end_info = {}

        for (i,x) in enumerate(s):
            if x not in start_end_info:
                start_end_info[x] = {}
                start_end_info[x]['start'] = i
                start_end_info[x]['end'] = i
            else:
                start_end_info[x]['end'] = i

        start_end_info = [(start_end_info[x]['start'],start_end_info[x]['end']) for x in start_end_info]

        start_end_info.sort()
        
        result_list = [start_end_info[0][1]]
        for i in range(1,len(start_end_info)):
            last_el_end = result_list[-1]
            if start_end_info[i][0] > last_el_end:
                result_list.append(start_end_info[i][1])
            else:
                if start_end_info[i][1] > result_list[-1]:
                    result_list[-1] = start_end_info[i][1]
        last = -1
        for i in range(len(result_list)):
            result_list[i],last = result_list[i]-last ,result_list[i]
        return result_list
                
