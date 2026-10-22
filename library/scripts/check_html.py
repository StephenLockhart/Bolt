import sys
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"extra </{tag}> at {self.getpos()}")
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                for t, p in self.stack[i + 1:]:
                    self.errors.append(f"unclosed <{t}> opened at {p}")
                del self.stack[i:]
                return
        self.errors.append(f"unmatched </{tag}> at {self.getpos()}")


def main(paths):
    bad = 0
    for p in paths:
        try:
            src = open(p, encoding="utf-8").read()
        except OSError as e:
            print(f"[SKIP] {p}: {e}")
            bad += 1
            continue
        c = Checker()
        c.feed(src)
        c.close()
        leftover = [f"unclosed <{t}> opened at {pos}" for t, pos in c.stack]
        issues = c.errors + leftover
        if issues:
            bad += 1
            print(f"[FAIL] {p}")
            for i in issues[:10]:
                print("   ", i)
        else:
            print(f"[PASS] {p}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
