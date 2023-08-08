# balanced-brackets
a function that takes a string, where each character in the string is a bracket, and returns the Boolean value True if the brackets are balanced; otherwise, returns the Boolean value False

Two brackets are considered matched if an opening bracket (i.e., (, {, [) is followed by a closing bracket (i.e., ), }, ]) of the exact same type. There are 3 types of brackets – parenthesis, that is, (), braces, that is, {}, and square brackets, that is [].

Sample Test Case
1. is_balanced(‘{[()]}’) = True
2. is_balanced(‘{[(])}’) = False
3. is_balanced(‘{{[[(())]]}}’) = True
