// https://leetcode.com/problems/contains-duplicate/description/
use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::new();
        for num in nums {
            if seen.contains(&num) {
                return true;
            } else {
                seen.insert(num);
            }
        }

        return false;
    }
}
