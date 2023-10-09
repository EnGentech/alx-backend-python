What is asynchronous programming?
Asynchronous programs execute operations in parallel without blocking the main process. That’s a mouthful, but all it means is this: async code is a way to make sure your program doesn’t needlessly spend time waiting when it could be doing other work.

If you’ve read anything about async programming before, you’ve probably heard the chess example a dozen times (a master chess player playing a tournament one game at time, versus all the games at once). While this is classically helpful at illustrating the concept, cooking food provides a more relatable metaphor with some spicier details you should keep in mind.

Synchronous Cooking
How frequently have you cooked breakfast like this?

Step 1: Cook eggs (or toast, for our veg friends)

Step 2: Cook bacon (oatmeal)

Step 3: Eat cold eggs/toast and hot bacon/oatmeal

Hopefully, the answer is “literally never.” Cooking one dish at a time before moving onto the next probably makes for some pretty gross food (and it’s totally inefficient). This is what we call: synchronous cooking. If you have friends that do this regularly, help them immediately.

Asynchronous Cooking
When making a decent-sized meal, it’s rare to want to prepare a single dish at a time. Instead, if you’re making oatmeal and toast, you put the coffee on, then start the water boiling, get out the oatmeal and the bread. When the water is boiling, then you start the oatmeal, and, a few minutes before the oatmeal’s ready, pop the toast in the toaster.

Now, when everything’s ready, you’ve hopefully got hot coffee, toast and oatmeal ready to eat, all about the same time. This is what we call: asynchronous cooking.

Note that cooking everything at the same time doesn’t reduce the cook time of each dish. You still need to let the toast become golden brown, the coffee percolate, and the oatmeal has to… do whatever oatmeal does when it’s ready. Making toast takes the same amount of time asynchronously as it does synchronously.

However, instead of wasting time waiting on each item to be finished, tasks are performed as the stages of cooking progress. This means multiple tasks are started as soon as possible and your valuable time is used efficiently.

Considerations
Another important feature of the async approach is that the order is less important than when we move on to other tasks. If, for example, we were cooking a 3-course meal, the first course precedes the second which precedes the third. In that scenario, we may need to cook those dishes synchronously.