"""
Implement a group_by_owners function that

Me

Accepts a dictionary containing the file owner name for each file name.

• Returns a dictionary containing a list of file names for each owner name,
in any order.

For example, for dictionary
(Input.txt 'Randy', 'Code.py: 'Stan', 'Output.txt': 'Randy'] the

group_by_owners function should
return ['Randy [Input.txt', 'output.txt'], 'stan ['Code.py']}.
"""


def group_by_owners(files):
    owners = {v: list() for v in files.values()}
    [owners[v].append(k) for k, v in files.items()]
    return owners


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))

