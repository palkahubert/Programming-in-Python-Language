from collections import deque

class AhoCorasick:
    def __init__(self, patterns):
        self.trie = {}
        self.output = {}
        self.fail = {}
        self._build_trie(patterns)
        self._build_fail_links()

    def _build_trie(self, patterns):
        for pattern in patterns:
            node = self.trie
            for char in pattern:
                node = node.setdefault(char, {})
            node['$'] = pattern

    def _build_fail_links(self):
        queue = deque()
        for key in self.trie:
            self.fail[id(self.trie[key])] = self.trie
            queue.append(self.trie[key])

        while queue:
            node = queue.popleft()
            for key, next_node in node.items():
                if key == '$':
                    continue
                queue.append(next_node)

                fail_state = self.fail[id(node)]
                while fail_state and key not in fail_state:
                    fail_state = self.fail.get(id(fail_state))
                self.fail[id(next_node)] = fail_state[key] if fail_state and key in fail_state else self.trie

    def search(self, text):
        results = []
        node = self.trie

        for i, char in enumerate(text):
            while node and char not in node:
                node = self.fail.get(id(node))
            if not node:
                node = self.trie
                continue
            node = node[char]
            if '$' in node:
                results.append((node['$'], i - len(node['$']) + 1))
        return results


patterns = ["he", "she", "his", "hers"]
text = "ahishers"

ac = AhoCorasick(patterns)
matches = ac.search(text)

print("Found patterns:")
for pattern, index in matches:
    print(f"{pattern!r} found on position {index}")

