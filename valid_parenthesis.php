<?php
class Stack
{
    private $elements = [];
    
    public function push(string $char)
    {
        array_push($this->elements, $char);
    }
    
    public function pop()
    {
        return array_pop($this->elements);
    }
    
    public function isEmpty(): bool
    {
        return empty($this->elements);
    }
}

class Solution {
    const OPEN = ['(', '[', '{'];
    
    public function isValid($s) 
    {
        if (empty($s)) return true;
        if (strlen($s) < 2) return false;
        
        $tracker = new Stack();
        
        $braces = str_split($s);
        foreach ($braces as $brace) {
            if (in_array($brace, self::OPEN)) {
                $tracker->push($brace);
                
                continue;
            }
            
            $last = $tracker->pop();
            
            if (
                ($last !== '(' && $brace === ')') ||
                ($last !== '[' && $brace === ']') ||
                ($last !== '{' && $brace === '}')
            ) {
                return false;
            }
        }
        
        return $tracker->isEmpty();
    }
}
