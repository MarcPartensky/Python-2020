class Proposition:
    def __init__(self, text):
        self.text = text
    def __call__(self, propositions):
        """Is true given propositions."""
        return None
    def __bool__(self):
        """Is true in itself."""
        return None
    def __inv__(self):
        """Is negation true in itself."""
        return not self

class Axiom(Proposition):
    def __init__(self, text):
        self.text = text
    def __call__(self, propositions):
        return True
    def __bool__(self):
        return True

class Extensionality(Axiom):
    def __init__(self):
        self.text = "∀x∀y(∀z(z∈x⇔z∈y))"
