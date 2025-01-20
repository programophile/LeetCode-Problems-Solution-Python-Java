Can you solve this real interview question? Check if a String Is an Acronym of Words - Given an array of strings words and a string s, determine if s is an acronym of words.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, &quot;ab&quot; can be formed from [&quot;apple&quot;, &quot;banana&quot;], but it can&#x27;t be formed from [&quot;bear&quot;, &quot;aardvark&quot;].

Return true if s is an acronym of words, and false otherwise.

 

Example 1:


Input: words = [&quot;alice&quot;,&quot;bob&quot;,&quot;charlie&quot;], s = &quot;abc&quot;
Output: true
Explanation: The first character in the words &quot;alice&quot;, &quot;bob&quot;, and &quot;charlie&quot; are &#x27;a&#x27;, &#x27;b&#x27;, and &#x27;c&#x27;, respectively. Hence, s = &quot;abc&quot; is the acronym. 


Example 2:


Input: words = [&quot;an&quot;,&quot;apple&quot;], s = &quot;a&quot;
Output: false
Explanation: The first character in the words &quot;an&quot; and &quot;apple&quot; are &#x27;a&#x27; and &#x27;a&#x27;, respectively. 
The acronym formed by concatenating these characters is &quot;aa&quot;. 
Hence, s = &quot;a&quot; is not the acronym.


Example 3:


Input: words = [&quot;never&quot;,&quot;gonna&quot;,&quot;give&quot;,&quot;up&quot;,&quot;on&quot;,&quot;you&quot;], s = &quot;ngguoy&quot;
Output: true
Explanation: By concatenating the first character of the words in the array, we get the string &quot;ngguoy&quot;. 
Hence, s = &quot;ngguoy&quot; is the acronym.


 

Constraints:

 * 1 &lt;= words.length &lt;= 100
 * 1 &lt;= words[i].length &lt;= 10
 * 1 &lt;= s.length &lt;= 100
 * words[i] and s consist of lowercase English letters.