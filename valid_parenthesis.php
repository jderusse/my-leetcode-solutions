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
    const MATCHES = [
        '(' => ')',
        '[' => ']',
        '{' => '}'
    ];

    public function isValid($s)
    {
        if (empty($s)) return true;
        $s = preg_replace(sprintf('/[^%s]+/', preg_quote(implode('', array_keys(self::MATCHES)).implode('', array_values(self::MATCHES)))), '', $s);

        if (empty($s)) return true;
        if (strlen($s) % 2 !== 0) return false;

        $tracker = new Stack();
        $last = null;
        foreach (str_split($s) as $c) {
            if (isset(self::MATCHES[$c])) {
                if ($last) {
                    $tracker->push($last);
                }
                $last = self::MATCHES[$c];

                continue;
            }

            if ($last !== $c) return false;
            $last = $tracker->pop();
        }

        return $tracker->isEmpty();
    }
}
