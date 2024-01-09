// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
// git add . && git commit -m "completed minimum_time_to_make_rope_colorful rust version" && git push && exit

use std::{char, cmp::max};

pub fn min_cost(colors: String, needed_time: Vec<i32>) -> i32 {
    let mut result = 0;
    let mut last_color: char = colors.chars().next().unwrap();
    let mut max_time = 0;
    let mut total_color_time = 0;
    for (i, ch) in colors.chars().enumerate() {
        if last_color != ch {
            result += total_color_time - max_time;
            last_color = ch;
            max_time = 0;
            total_color_time = 0;
        }
        total_color_time += needed_time[i];
        max_time = max(max_time, needed_time[i]);
    }
    result += total_color_time - max_time;
    result
}
