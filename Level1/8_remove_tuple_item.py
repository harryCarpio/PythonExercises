# Write a Python function to remove an item from a tuple.

def remove_item(a_tuple, item_to_remove):
    for i in range(len(a_tuple)):
        if a_tuple[i] == item_to_remove:
            return a_tuple[:i] + a_tuple[i+1:]
    return a_tuple


t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

item_to_remove = 'corge'
print("Original tuple: {}".format(t))
print("Tuple without '{}' item: {}".format(item_to_remove, remove_item(t, item_to_remove)))
