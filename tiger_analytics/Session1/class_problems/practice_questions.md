1. Say you have a list value like this:

    ```python

    spam = ['apples', 'bananas', 'tofu', 'cats']
    ```
    Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an empty list [] is passed to your function.

2. Given a list of numbers, the task is to write a Python program to find the largest number in given list.

    Example:

    ```
    Input : list1 = [10, 20, 4]
    Output : 20
    ```

3. For this exercise, write a Python function (`pig_latin`) that takes a string as input, assumed to be an English word. The function should return the translation of this word into Pig Latin. You may assume that the word contains no capital letters or punctuation.

The rules for translating words from English into Pig Latin are quite simple:

- If the word begins with a vowel (a, e, i, o, or u), add “way” to the end of the word. So “air” becomes “airway” and “eat” becomes “eatway.”
- If the word begins with any other letter, then we take the first letter, put it on the end of the word, and then add “ay.” Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.”