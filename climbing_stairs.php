<?php

class Solution {
    public function climbStairs(int $n): int 
    {
        // Numbers of distinct ways kered by number of stairs
        $ways = [];
        
        $ways[0] = 1;
        $ways[1] = 1;
        
        for ($i = 2; $i <= $n; $i++) {
            $ways[$i] = $ways[$i-1] + $ways[$i-2];
        }
        
        return $ways[$n];
    }
}
