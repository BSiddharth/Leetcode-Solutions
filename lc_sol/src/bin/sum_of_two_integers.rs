// https://leetcode.com/problems/sum-of-two-integers/description/
// git add . && git commit -m "completed sum_of_two_integers" && git push && exit

fn main() {
    struct Solution;
    impl Solution {
        pub fn get_sum(a: i32, b: i32) -> i32 {
            let mut xored = a ^ b;
            let mut anded = a & b;

            while anded != 0 {
                let old_xored = xored;
                xored = xored ^ (anded << 1);
                anded = old_xored & (anded << 1)
            }
            xored
        }
    }
}
