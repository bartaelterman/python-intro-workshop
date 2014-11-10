import re

zen = """
The Zen of Python, by TimPeters:

1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7. Readability counts.
8. Special cases aren't special enough to break the rules.
    1. Although practicality beats purity.
9. Errors should never pass silently.
    1. Unless explicitly silenced.
10. In the face of ambiguity, refuse the temptation to guess.
11. There should be one-- and preferably only one --obvious way to do it.
    1. Although that way may not be obvious at first unless you're Dutch.
12. Now is better than never.
    1. Although never is often better than right now.
13. If the implementation is hard to explain, it's a bad idea.
14. If the implementation is easy to explain, it may be a good idea.
15. NameSpaces are one honking great idea -- let's do more of those!
"""

print 'number of sub bullets:'
print len(re.findall('\n +[0-9]+', zen))