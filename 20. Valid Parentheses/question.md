Can you solve this real interview question? Valid Parentheses - Given a string s containing just the characters &#x27;(&#x27;, &#x27;)&#x27;, &#x27;{&#x27;, &#x27;}&#x27;, &#x27;[&#x27; and &#x27;]&#x27;, determine if the input string is valid.

An input string is valid if:

 1. Open brackets must be closed by the same type of brackets.
 2. Open brackets must be closed in the correct order.
 3. Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = &quot;()&quot;

Output: true

Example 2:

Input: s = &quot;()[]{}&quot;

Output: true

Example 3:

Input: s = &quot;(]&quot;

Output: false

Example 4:

Input: s = &quot;([])&quot;

Output: true

 

Constraints:

 * 1 &lt;= s.length &lt;= 104
 * s consists of parentheses only &#x27;()[]{}&#x27;.